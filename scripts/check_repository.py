#!/usr/bin/env python3
"""Check this public distribution using Python's standard library only."""
import html
import importlib.util
import json
import re
import struct
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills/zopc-commercial-visual-posters"


def public_files():
    result = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT, check=True, capture_output=True,
    )
    return sorted({ROOT / name for name in result.stdout.decode().split("\0") if name})


def anchors(text):
    """GitHub-style anchors for the simple headings maintained in this repo."""
    found = set(re.findall(r'<a\s+(?:name|id)=["\']([^"\']+)', text))
    counts = {}
    fence = chr(96) * 3
    text = re.sub(r"^" + fence + r".*?^" + fence + r"[^\n]*", "", text, flags=re.M | re.S)
    for heading in re.findall(r"^#{1,6}\s+(.+)$", text, flags=re.M):
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        index = counts.get(slug, 0)
        found.add(slug if not index else f"{slug}-{index}")
        counts[slug] = index + 1
    return found


def local_links(path, text):
    targets = re.findall(r'(?:href|src)=["\']([^"\']+)["\']', text)
    targets += [a or b for a, b in re.findall(
        r'!?\[[^\]]*\]\(\s*(?:<([^>]+)>|([^\s)]+))[^)]*\)', text
    )]
    targets += re.findall(r"^\[[^\]]+\]:\s+(\S+)", text, flags=re.M)
    for target in targets:
        parsed = urlsplit(html.unescape(target))
        if parsed.scheme or parsed.netloc:
            continue
        resolved = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
        if not resolved.is_relative_to(ROOT) or not resolved.exists():
            yield f"{path.relative_to(ROOT)}: missing or external local target {target}"
        elif parsed.fragment and resolved.suffix == ".md":
            if unquote(parsed.fragment) not in anchors(resolved.read_text(encoding="utf-8")):
                yield f"{path.relative_to(ROOT)}: missing heading anchor {target}"


def jpeg_size(path):
    data = path.read_bytes()
    if data[:2] != b"\xff\xd8":
        raise ValueError("not a JPEG")
    offset = 2
    while offset + 4 <= len(data):
        if data[offset] != 0xFF:
            offset += 1
            continue
        marker = data[offset + 1]
        offset += 2
        if marker in (0x01, 0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            continue
        length = struct.unpack(">H", data[offset:offset + 2])[0]
        if marker in (0xC0, 0xC1, 0xC2):
            height, width = struct.unpack(">HH", data[offset + 3:offset + 7])
            return width, height
        if length < 2:
            break
        offset += length
    raise ValueError("JPEG dimensions not found")


def check():
    errors = []
    files = public_files()
    spec = importlib.util.spec_from_file_location("skill_assets", SKILL / "scripts/verify_assets.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assets = module.verify()
    errors.extend(assets["errors"])
    catalog = json.loads((SKILL / "references/catalog.json").read_text(encoding="utf-8"))
    if catalog.get("distribution") != {
        "visibility": "public", "scope": "current-only", "historyIncluded": False,
    } or any(assets[name] for name in (
        "historical_images", "historical_aliases", "historical_versions",
    )):
        errors.append("Public distribution must contain current assets only.")

    link_count = 0
    private_path = re.compile(r"/(?:Users|home|private/var/folders)/[A-Za-z0-9_\u4e00-\u9fff-]+/")
    credential = re.compile(
        r"(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}|"
        r"sk-[A-Za-z0-9_-]{30,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)"
    )
    for path in files:
        relative = path.relative_to(ROOT)
        if path.is_symlink() or not path.resolve().is_relative_to(ROOT):
            errors.append(f"Symlink or out-of-repository file: {relative}")
            continue
        if "history" in relative.parts and path.name != "index.json":
            errors.append(f"Historical original is outside the public scope: {relative}")
        if path.suffix.lower() in {".zip", ".env", ".key", ".pem"}:
            errors.append(f"Unexpected archive or private configuration: {relative}")
        if not path.is_file():
            errors.append(f"Tracked file is missing: {relative}")
            continue
        if path.suffix.lower() in {".md", ".json", ".py", ".yml", ".yaml", ".svg"}:
            text = path.read_text(encoding="utf-8")
            if private_path.search(text) or credential.search(text):
                errors.append(f"Possible private host path or credential: {relative}")
            if path.suffix.lower() in {".md", ".svg"}:
                errors.extend(local_links(path, text))
                link_count += len(re.findall(r'\]\(|(?:href|src)=', text))

    for name, other in (("README.md", "README.en.md"), ("README.en.md", "README.md")):
        text = (ROOT / name).read_text(encoding="utf-8")
        if other not in text:
            errors.append(f"{name}: missing reciprocal language link.")
        for marker in ("mascot_presets-10", "poster_styles-11"):
            if marker not in text:
                errors.append(f"{name}: count badge has drifted.")
        for item in catalog["mascots"] + catalog["styles"] + [catalog["custom_example"]]:
            if item["reference"] not in text:
                errors.append(f"{name}: missing original image link for {item['id']}.")

    for name, dimensions in (("hero", (1600, 800)), ("social-preview", (1280, 640))):
        path = ROOT / f"docs/brand/{name}.jpg"
        try:
            if jpeg_size(path) != dimensions:
                errors.append(f"{name}: incorrect JPEG dimensions.")
            if name == "social-preview" and path.stat().st_size >= 1_000_000:
                errors.append("Social preview must be below 1 MB.")
        except (ValueError, OSError, struct.error) as error:
            errors.append(f"{name}: {error}")
    previews = list((ROOT / "docs/previews").rglob("*.jpg"))
    if len(previews) != 24:
        errors.append("Expected 24 lightweight gallery previews.")
    for path in previews:
        try:
            jpeg_size(path)
        except (ValueError, OSError, struct.error) as error:
            errors.append(f"{path.relative_to(ROOT)}: {error}")

    return {
        "ok": not errors, "errors": errors,
        "public_files": len(files), "link_references": link_count,
        "verified_skill_assets": assets["assets_checked"],
        "mascot_presets": assets["presets"], "poster_styles": assets["styles"],
        "historical_originals": assets["historical_images"],
        "scope": "Local links, anchors, asset hashes, public scope, language parity and image headers. "
                 "Does not replace visual review, QR testing or client/platform acceptance.",
    }


if __name__ == "__main__":
    try:
        result = check()
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
        result = {"ok": False, "errors": [str(error)]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if result["ok"] else 1)
