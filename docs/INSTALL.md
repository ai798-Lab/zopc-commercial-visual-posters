# 安装与使用步骤

[返回首页](../README.md) · [吉祥物单图](MASCOTS.md) · [海报单图](POSTERS.md)

## 准备条件

使用支持本地 Skill 的 Codex 环境。制作海报还需要当前环境可用的图片生成/编辑能力，是否可用取决于你的客户端与账号。此 Skill 本身不附带模型、付费额度或独立的图片服务。

目录显示、信息检查与素材核验脚本需要 Python 3，不需要第三方 Python 包。日常使用直接用自然语言，不需要编写 JSON。

## 方法一：让 Codex 安装

1. 打开 Codex 对话。
2. 粘贴下面整段请求，让安装器安装这个 Skill 目录：

```text
$skill-installer install https://github.com/ai798-Lab/zopc-commercial-visual-posters/tree/main/skills/zopc-commercial-visual-posters
```

3. 等待安装完成。请等待整个 Skill 目录下载完成，以便图册与原图可以正常显示。
4. 新开对话，输入：

```text
使用 $zopc-commercial-visual-posters，帮我做一张运营海报。
```

如果尚未显示，重启 Codex 后再试。若同名 Skill 已经安装，安装器可能停止以免覆盖；先检查现有版本，再决定保留备份或更新。

## 方法二：下载后手动安装

1. 打开 [仓库主页](https://github.com/ai798-Lab/zopc-commercial-visual-posters)，点击 **Code → Download ZIP**；也可 [直接下载 ZIP](https://github.com/ai798-Lab/zopc-commercial-visual-posters/archive/refs/heads/main.zip)。
2. 解压后进入 `skills`，找到 `zopc-commercial-visual-posters`。打开这个文件夹，应直接看到 `SKILL.md`、`agents`、`assets`、`references` 和 `scripts`。
3. 将这个完整文件夹放进本地 Skill 目录。官方当前支持的用户级位置是 `~/.agents/skills/`；只用于一个项目时，可放进该项目的 `.agents/skills/`。不要在多个位置重复安装同名 Skill。
4. 新开对话调用。如果尚未出现，重启 Codex。

最终目录示例：

```text
~/.agents/skills/
└── zopc-commercial-visual-posters/
    ├── SKILL.md
    ├── agents/
    ├── assets/
    ├── references/
    └── scripts/
```

保留完整目录结构，不要只复制 `SKILL.md`，也不要把整个仓库外层目录误当作 Skill。

## 使用流程

1. **选择形象。** 看 M01–M10 总览后回复编号，或上传/描述自定义形象。选择使用原图但没有收到附件时，会等待原图。
2. **选择样式。** 看 S01–S11 图册后选编号。示例角色不会覆盖你已选的角色。
3. **补充信息。** 给标题、主要内容、平台与比例、一个行动引导；价格、日期、Logo和二维码按需要提供。已知内容不重复问。
4. **生成检查。** 查看真实海报，核对文字、角色、布局和素材。Logo和可用二维码使用真实原文件。
5. **决定是否延展。** 首张完成后再选详情页、权益图、直播预告、倒计时或横版封面；若一开始已要求整套，会按授权范围完成。

当前可选样张没有固定的实战营赠券、价格、折扣、日期或二维码，这些内容只有当次明确提供时才加入。

## 可直接复制的请求

```text
使用 $zopc-commercial-visual-posters。
我要先看吉祥物总览，再选海报样式。
```

```text
使用 $zopc-commercial-visual-posters。
吉祥物选 M02 熊猫，海报选 S08 红黑潮玩。
标题：AI 创作周末营
副标题：带一个想法来，带一个作品走
比例：3:4
品牌：我的工作室
引导：了解活动安排
不要价格、赠品和二维码。
```

```text
使用 $zopc-commercial-visual-posters。
用我上传的吉祥物，保留它的颜色、耳朵和尾巴。
海报样式我想先看完整编号图册。
```

## 检查安装是否完整

进入安装后的 Skill 文件夹运行：

```bash
python3 scripts/verify_assets.py
```

输出 `"ok": true` 表示目录、素材指纹、图片头/尺寸与索引一致。它不替代视觉审稿或平台验收。

查看当前素材：

```bash
python3 scripts/catalog.py mascots
python3 scripts/catalog.py styles
```

如果能显示图册但不能生成图片，需要检查当前环境的图片生成能力。Python脚本不会代替图片模型，准备好提示词也不代表已出图。

## 官方参考

安装目录、发现方式及安装器用法，以 [OpenAI 官方 Skill 文档](https://developers.openai.com/codex/skills) 为准。本说明核对日期：2026-10-22。
