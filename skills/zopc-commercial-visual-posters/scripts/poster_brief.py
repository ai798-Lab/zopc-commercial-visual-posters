#!/usr/bin/env python3
"""Validate a selected poster brief or prepare image_gen arguments; never generates images."""
import argparse, json, re, sys
from pathlib import Path
from datetime import date
from decimal import Decimal, InvalidOperation

ROOT = Path(__file__).resolve().parent.parent
def load_catalog():
    return json.loads((ROOT / "references/catalog.json").read_text(encoding="utf-8"))
def amount(value):
    return Decimal(re.sub(r"[,，￥¥\s]", "", str(value)))
def resolve_user_path(value, base):
    path = Path(value).expanduser()
    return path.resolve() if path.is_absolute() else (base / path).resolve()
def validate(brief, base):
    catalog = load_catalog()
    errors, warnings = [], []
    style = next((s for s in catalog["styles"] if s["id"] == brief.get("style_id")), None)
    mascot = next((m for m in catalog["mascots"] if m["id"] == brief.get("mascot_id")), None)
    if style is None:
        errors.append("请先选择 S01–S11 样式。")
    if brief.get("mascot_id") == "custom":
        custom = brief.get("custom") or {}
        if custom.get("mode") not in {"uploaded", "description"}:
            errors.append("请明确自定义形象来源：uploaded 使用上传原图，或 description 使用文字创作；不能省略来源模式。")
        if custom.get("mode") == "uploaded" and not custom.get("image"):
            errors.append("用户选择使用上传原图，但尚未收到形象图片；不能改用文字重画代替。")
        if not custom.get("description") and not custom.get("image"):
            errors.append("自定义形象需要图片或明确的文字描述。")
        if custom.get("image") and not resolve_user_path(custom["image"], base).is_file():
            errors.append("自定义形象图片不存在。")
    elif mascot is None:
        errors.append("请先选择 M01–M10，或选择 custom 并提供形象资料。")
    if not brief.get("title") or not str(brief["title"]).strip():
        errors.append("缺少主标题。")
    size = brief.get("size", {"width": 1086, "height": 1448})
    if not all(isinstance(size.get(k), int) and size[k] > 0 for k in ("width", "height")):
        errors.append("尺寸必须包含正整数 width 和 height。")
    price = brief.get("price") or {}
    nums = {}
    for key in ("sale", "original", "discount_zhe"):
        if price.get(key) not in (None, ""):
            try:
                nums[key] = amount(price[key])
                if nums[key] < 0:
                    errors.append("价格或折扣不能为负数。")
            except (InvalidOperation, ValueError):
                errors.append("无法识别价格字段：" + key)
    if "original" in nums and nums["original"] <= 0:
        errors.append("原价需大于0，不能作为零值折扣依据。")
    if "discount_zhe" in nums and not Decimal(0) < nums["discount_zhe"] <= Decimal(10):
        errors.append("折扣应在0到10折之间。")
    if {"sale", "original", "discount_zhe"}.issubset(nums) and nums["original"] > 0:
        calculated = nums["sale"] / nums["original"] * 10
        if abs(calculated - nums["discount_zhe"]) > Decimal("0.06"):
            errors.append("售价、原价与折扣互相矛盾；请核对，不能沿用样张折扣。")
    if "discount_zhe" in nums and not {"sale", "original"}.issubset(nums):
        warnings.append("折扣缺少完整计算依据，需确认它是用户明确提供的真实活动信息。")
    qr = brief.get("qr") or {"mode": "none"}
    if qr.get("mode", "none") not in {"none", "provided"}:
        errors.append("二维码模式仅支持 none 或 provided。")
    if qr.get("mode") == "provided":
        if not qr.get("image") or not resolve_user_path(qr["image"], base).is_file():
            errors.append("扫码版需要用户当前的二维码原图文件。")
    if qr.get("mode", "none") == "none" and re.search(r"扫码|识别二维码|长按识别", str(brief.get("cta", ""))):
        errors.append("无二维码版的行动文案仍要求扫码，请重排为合适的无二维码引导。")
    brand = brief.get("brand") or {}
    if brand.get("logo") and not resolve_user_path(brand["logo"], base).is_file():
        errors.append("Logo原文件不存在。")
    event = brief.get("event") or {}
    if event.get("date") and brief.get("as_of") and brief.get("purpose", "new") != "historical":
        try:
            if date.fromisoformat(event["date"]) < date.fromisoformat(brief["as_of"]):
                errors.append("这是新活动，但日期已经过去；请确认新日期或明确为历史重制。")
        except ValueError:
            errors.append("用于核对过期的 date/as_of 字段需为 YYYY-MM-DD；展示文案可用 event.label。")
    return {"ok": not errors, "errors": errors, "warnings": warnings}, catalog, style, mascot
def make_prompt(brief, base):
    report, catalog, style, mascot = validate(brief, base)
    if not report["ok"]:
        return report
    references = [str((ROOT / style["reference"]).resolve())]
    if brief["mascot_id"] == "custom":
        character = brief["custom"].get("description", "保持用户上传形象的识别特征")
        if brief["custom"].get("image"):
            references.append(str(resolve_user_path(brief["custom"]["image"], base)))
    else:
        character = mascot["identity"]
        references.append(str((ROOT / mascot["reference"]).resolve()))
    lines = [str(brief["title"])]
    for key in ("subtitle", "supporting_copy"):
        if brief.get(key):
            lines.append(str(brief[key]))
    lines.extend(str(x) for x in brief.get("highlights", []) if str(x).strip())
    event = brief.get("event") or {}
    event_text = event.get("label") or " ".join(str(event.get(k, "")) for k in ("date", "time", "location")).strip()
    if event_text:
        lines.append(event_text)
    price = brief.get("price") or {}
    if price.get("sale") not in (None, ""):
        unit = "/" + str(price["unit"]) if price.get("unit") else ""
        lines.append(str(price.get("currency", "¥")) + str(price["sale"]) + unit)
    if price.get("original") not in (None, ""):
        lines.append("原价 " + str(price.get("currency", "¥")) + str(price["original"]))
    if price.get("discount_zhe") not in (None, ""):
        lines.append(str(price["discount_zhe"]) + "折")
    if brief.get("gift"):
        lines.append(str(brief["gift"]))
    if brief.get("cta"):
        lines.append(str(brief["cta"]))
    brand = brief.get("brand") or {}
    if brand.get("name"):
        lines.append(str(brand["name"]))
    qr = brief.get("qr") or {"mode": "none"}
    size = brief.get("size", {"width": 1086, "height": 1448})
    prompt = (
        "Use case: ads-marketing. 制作一张精致的三维潮玩运营海报，"
        f"尺寸 {size['width']}×{size['height']}。目标平台：" + str(brief.get("platform") or "通用运营物料") + "。参考图1仅负责样式："
        + style["id"] + " " + style["name"] + "，" + style["summary"] + "。"
        "如有参考图2，它只负责用户选择的角色身份。最终角色：" + character + "。"
        "即使样式参考里的动物不同，也必须使用该用户选择，不能混入其物种或颜色。"
        "保留统一潮玩质感与自然光影，按活动内容调整动作、道具与构图；真实接触和完整识别特征。"
        "本次需要渲染的全部文字严格为下面清单，逐字准确，安排清楚的主次、换行与留白："
        + json.dumps(lines, ensure_ascii=False)
        + "。清单以外的参考图品牌、日期、价格、折扣、21天和赠送数量均不能继承。"
        "不要照抄参考里的二维码或旧活动入口。文字、卡片、权益条居中与安全边距按透视和实际尺寸处理。"
        "真实Logo和二维码由后续文档图层插入，不描画原标志或可用码。"
    )
    if brief.get("layout"):
        prompt += "本次版式安排：" + str(brief["layout"]) + "。"
    if brief.get("scene"):
        prompt += "本次角色动作、道具与场景：" + str(brief["scene"]) + "。"
    if not brief.get("gift"):
        prompt += "本次没有赠送权益文案，删除参考中的赠送券或权益条并重排，不保留空牌或旧赠送信息。"
    if not price:
        prompt += "本次没有价格模块，删除参考中的售价、原价与折扣标记并重排。"
    if not brand.get("name") and not brand.get("logo"):
        prompt += "本次未指定品牌，不继承样式示例的ZOPC或ai798Lab字标。"
    if brand.get("logo"):
        prompt += "给用户真实Logo在安全区域预留低干扰空间；保持整套坐标一致。"
    if qr.get("mode", "none") == "none":
        prompt += "这是无二维码版：没有二维码、占位白框或扫码箭头；底部重新形成完整的信息/行动区。"
    else:
        prompt += "这是扫码版：为用户原二维码留出合理区域和静区，但本图不绘制二维码；后续必须解码核验。"
    prompt += "不增加虚构事实或无意义小字，不出现水印。"
    assets = {}
    if brand.get("logo"):
        assets["logo"] = str(resolve_user_path(brand["logo"], base))
    if qr.get("mode") == "provided":
        assets["qr"] = str(resolve_user_path(qr["image"], base))
    return {**report, "selected": {"mascot_id": brief["mascot_id"], "style_id": style["id"]},
            "image_gen": {"prompt": prompt, "referenced_image_paths": references, "transparent_background": False},
            "platform": brief.get("platform", ""), "layout": brief.get("layout", ""), "scene": brief.get("scene", ""),
            "composition_assets": assets, "exact_text": lines, "execution": "任务已准备；尚未调用图片生成，也未导出成品。"}
def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["init", "validate", "prompt"])
    parser.add_argument("brief", nargs="?")
    args = parser.parse_args()
    if args.action == "init":
        result = {"mascot_id": None, "style_id": None, "purpose": "new", "as_of": None,
                  "title": "", "subtitle": "", "highlights": [], "cta": "",
                  "size": {"width": 1086, "height": 1448}, "platform": "", "layout": "", "scene": "", "event": {},
                  "brand": {}, "price": None, "gift": "", "qr": {"mode": "none"},
                  "custom": {"mode": None, "image": "", "description": ""}}
    else:
        if not args.brief:
            parser.error("请提供填写完成的 brief.json 文件。")
        source = Path(args.brief).expanduser().resolve()
        brief = json.loads(source.read_text(encoding="utf-8"))
        result = validate(brief, source.parent)[0] if args.action == "validate" else make_prompt(brief, source.parent)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result.get("ok") is False:
        sys.exit(2)
if __name__ == "__main__":
    main()
