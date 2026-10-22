#!/usr/bin/env python3
"""Verify the portable catalog, asset hashes and historical originals; no network."""
import hashlib
import json
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def verify():
    errors = []
    checked = set()
    def read(relative):
        return json.loads((ROOT / relative).read_text(encoding="utf-8"))
    def asset(relative, metadata=None):
        path = (ROOT / relative).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file():
            errors.append("素材路径无效：" + relative)
            return
        checked.add(relative)
        content = path.read_bytes()
        metadata = metadata or {}
        if metadata.get("sha256") and hashlib.sha256(content).hexdigest() != metadata["sha256"]:
            errors.append("文件指纹不符：" + relative)
        if "bytes" in metadata and len(content) != metadata["bytes"]:
            errors.append("文件大小不符：" + relative)
        if path.suffix.lower() == ".png":
            if content[:8] != b"\x89PNG\r\n\x1a\n" or content[12:16] != b"IHDR":
                errors.append("文件不是有效PNG头：" + relative)
            else:
                width, height = struct.unpack(">II", content[16:24])
                if "width" in metadata and (width, height) != (metadata["width"], metadata["height"]):
                    errors.append("图片尺寸不符：" + relative)

    catalog = read("references/catalog.json")
    manifest = read("references/asset-manifest.json")
    history = read(catalog["historyIndex"])
    mascots, styles = catalog["mascots"], catalog["styles"]
    if {x["id"] for x in mascots} != {f"M{x:02}" for x in range(1, 11)} or len(mascots) != 10:
        errors.append("预设形象应为M01至M10，共10个。")
    if {x["id"] for x in styles} != {f"S{x:02}" for x in range(1, 12)} or len(styles) != 11:
        errors.append("当前样式应为S01至S11，共11个。")
    custom = catalog["custom_example"]
    if custom["id"] != "C01" or custom.get("preset") is not False:
        errors.append("C01必须标记为自定义示范。")
    identities = {x["id"] for x in mascots} | {custom["id"]}
    if {s["example_mascot"] for s in styles} != identities:
        errors.append("11个样式示例需使用各不相同的形象。")
    for item in mascots + styles + [custom]:
        asset(item["reference"])
    for item in manifest["entries"] + manifest["galleryEntries"] + history["items"]:
        asset(item["file"], item)
    for name in [catalog["galleries"]["mascots"], catalog["galleries"]["overview"]] + catalog["galleries"]["styles"]:
        asset(name)
    asset(catalog["brand"]["file"], {"sha256": manifest["logoSha256"]})
    aliases = sum(len(item["aliases"]) for item in history["items"])
    if len(history["items"]) != history["uniqueImages"] or aliases != history["sourceAliases"]:
        errors.append("历史原稿与别名数量不符。")
    if (manifest["historyImages"], manifest["historyAliases"], manifest["historyVersions"]) != (len(history["items"]), aliases, len(history["versions"])):
        errors.append("素材清单的历史数量不符。")
    policy = {"defaultGift": None, "inheritCampaignText": False, "currentSamplesHaveGift": False}
    if catalog.get("templatePolicy") != policy or manifest.get("templatePolicy") != policy:
        errors.append("当前样张策略与无默认赠品要求不符。")
    style_entries = [x for x in manifest["entries"] if x["id"].startswith("S")]
    if len(style_entries) != 11 or any(x.get("giftElement") is not False for x in style_entries):
        errors.append("样式清单没有完整标记无赠券版本。")
    return {"ok": not errors, "errors": errors, "assets_checked": len(checked),
            "presets": len(mascots), "styles": len(styles), "distinct_example_characters": len(identities),
            "historical_images": len(history["items"]), "historical_aliases": aliases,
            "historical_versions": len(history["versions"]),
            "scope": "已核对路径、指纹、文件大小、PNG头及尺寸、编号和目录策略；不替代逐图视觉检查或平台验收。"}

if __name__ == "__main__":
    result = verify()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if result["ok"] else 2)
