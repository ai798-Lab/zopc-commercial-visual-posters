#!/usr/bin/env python3
"""Resolve the installed poster catalog without network access or external packages."""
import argparse, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
def read_catalog():
    return json.loads((ROOT / "references/catalog.json").read_text(encoding="utf-8"))
def image_path(value):
    path = ROOT / value
    if not path.is_file():
        raise FileNotFoundError(str(path))
    return str(path.resolve())
def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["mascots", "styles", "style", "history"])
    parser.add_argument("id", nargs="?")
    parser.add_argument("--json", action="store_true", help="Kept for explicit machine-readable invocation; output is always JSON.")
    args = parser.parse_args()
    cat = read_catalog()
    if args.mode == "mascots":
        result = {"gallery": image_path(cat["galleries"]["mascots"]),
                  "items": [{**m, "reference": image_path(m["reference"])} for m in cat["mascots"]],
                  "custom": {"accepted": ["上传形象图", "文字描述物种、颜色、识别特征"], "example": image_path(cat["custom_example"]["reference"]), "exampleIsPreset": False}}
    elif args.mode == "styles":
        result = {"galleries": [image_path(p) for p in cat["galleries"]["styles"]],
                  "overview": image_path(cat["galleries"]["overview"]),
                  "items": [{**s, "reference": image_path(s["reference"])} for s in cat["styles"]],
                  "note": "示例角色和样式独立；最终采用用户先前选定的形象。"}
    elif args.mode == "style":
        selected = next((s for s in cat["styles"] if s["id"] == str(args.id).upper()), None)
        if not selected:
            parser.error("请提供 S01–S11 中的完整样式编号。")
        result = {**selected, "reference": image_path(selected["reference"])}
    else:
        hist = json.loads((ROOT / cat["historyIndex"]).read_text(encoding="utf-8"))
        items = hist["items"]
        if args.id:
            items = [x for x in items if x["id"] == args.id.upper()]
            if not items:
                parser.error("没有这个历史编号。")
        result = {"versions": hist["versions"], "uniqueImages": hist["uniqueImages"],
                  "sourceAliases": hist["sourceAliases"], "historicalOnly": True,
                  "items": [{**x, "file": image_path(x["file"])} for x in items]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
if __name__ == "__main__":
    main()
