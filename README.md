<a name="readme-top"></a>

<div align="center">

<img src="docs/brand/hero.jpg" alt="ZOPC 海报 Skill：真实吉祥物与红黑、宇宙、蓝白三种样式示例" width="100%">

<h1>ZOPC Visual Posters</h1>
<h3>从一个形象，到一整套运营视觉</h3>

<p>为活动、商品、课程与直播制作三维潮玩海报。<br>先选吉祥物，再选样式，填入自己的活动信息。</p>

<p><strong>简体中文</strong> · <a href="README.en.md">English</a></p>

<p><a href="docs/INSTALL.md">开始安装</a> · <a href="docs/POSTERS.md">浏览样式</a> · <a href="docs/MASCOTS.md">查看吉祥物</a> · <a href="https://github.com/ai798-Lab/zopc-commercial-visual-posters/issues/new/choose">反馈与建议</a></p>

[![Assets and docs](https://github.com/ai798-Lab/zopc-commercial-visual-posters/actions/workflows/verify-assets.yml/badge.svg)](https://github.com/ai798-Lab/zopc-commercial-visual-posters/actions/workflows/verify-assets.yml)
[![10 mascot presets](https://img.shields.io/badge/mascot_presets-10-9B7AFF?style=flat-square)](docs/MASCOTS.md)
[![11 poster styles](https://img.shields.io/badge/poster_styles-11-FF934D?style=flat-square)](docs/POSTERS.md)
[![Custom characters supported](https://img.shields.io/badge/custom_characters-supported-5EBEA8?style=flat-square)](skills/zopc-commercial-visual-posters/references/characters.md)

</div>

<details>
<summary>目录 · Table of contents</summary>

- [为什么用这套 Skill](#为什么用这套-skill)
- [安装与使用](#安装与使用)
- [对话制作流程](#对话制作流程)
- [视觉样式库](#视觉样式库)
- [文档与资源](#文档与资源)
- [本地检查](#本地检查)
- [参与贡献](#参与贡献)
- [许可与品牌](#许可与品牌)

</details>

## 为什么用这套 Skill

做一张海报时，先定清楚形象、视觉方向和活动信息；做一整套物料时，再让它们保持连贯。

- **先看真实样张。** 10 个预设吉祥物、11 个编号样式，选之前就能看清效果。
- **角色和样式独立选择。** 熊猫可以用红黑潮玩，也可以用星轨；还可以上传自己的吉祥物，或用文字描述新角色。
- **按活动内容制作。** 标题、品牌、日期、价格与入口都以本次资料为准，不沿用示例里的旧活动信息。
- **首张完成后继续延展。** 同一形象与样式可以用于详情页、权益图、直播预告、倒计时和横版封面。

这是一套可对话的设计工作流。实际出图需要当前客户端可用的图片生成/编辑能力；包内 Python 脚本负责目录、信息与素材检查。

[回到顶部 ↑](#readme-top)

## 安装与使用

**1. 在 Codex 对话里安装**

```text
$skill-installer install https://github.com/ai798-Lab/zopc-commercial-visual-posters/tree/main/skills/zopc-commercial-visual-posters
```

**2. 新开对话，开始选择**

```text
使用 $zopc-commercial-visual-posters，帮我做一张运营海报。
先给我看吉祥物和样式。
```

也可以直接给出选择和内容：

```text
使用 $zopc-commercial-visual-posters。
形象选 M03 机器人，样式选 S08 红黑潮玩。
标题：周末 AI 工具分享会
副标题：把问题带来，一起解决
平台与比例：小红书，3:4
品牌：实验室朋友
引导：收藏这场分享
不要价格、赠品和二维码。
```

[完整安装步骤](docs/INSTALL.md) · [手动安装与常见问题](docs/SUPPORT.md)

## 对话制作流程

**选视觉形象 → 看编号样式 → 选择样式 → 补充活动信息 → 生成并检查 → 决定是否延展**

已有明确选择和文案时，从缺少的信息继续，不重新问一遍。用户选择使用上传原图但尚未收到图片时，会等待原图。无价格、无日期、无 Logo 或无二维码都是有效选择。

需要可用二维码时使用当次提供的真实原码，并在成品中单独检查；生成结果交付到本地，不自动发布到外部平台。

[回到顶部 ↑](#readme-top)

## 视觉样式库

### 吉祥物总览

10 个预设形象保持统一潮玩质感，各自保留物种特征。C01 小象是自定义示范，不计入预设数量。

[![M01–M10 吉祥物与自定义入口](docs/previews/mascots-overview.jpg)](skills/zopc-commercial-visual-posters/assets/galleries/mascots.png)

[逐个查看形象与识别特征 →](docs/MASCOTS.md)

### 海报总览

S01–S11 分别保留字体、材质、色彩与空间气氛。每张示例使用不同吉祥物，最终制作采用用户自己选择的形象。

[![11 个带编号的海报样式，每张使用不同吉祥物](docs/previews/posters-overview.jpg)](skills/zopc-commercial-visual-posters/assets/galleries/styles-all.png)

[逐张查看完整海报 →](docs/POSTERS.md)

### 吉祥物单图

<details>
<summary>展开 10 个预设吉祥物的单张预览与 PNG 原图</summary>

<table>
<tr>
<td align="center" width="33%"><a href="skills/zopc-commercial-visual-posters/assets/mascots/M01.png"><img src="docs/previews/mascots/M01.jpg" alt="M01 橙色柴犬" width="210"></a><br><strong>M01 橙色柴犬</strong><br><a href="skills/zopc-commercial-visual-posters/assets/mascots/M01.png">查看 PNG 原图</a></td>
<td align="center" width="33%"><a href="skills/zopc-commercial-visual-posters/assets/mascots/M02.png"><img src="docs/previews/mascots/M02.jpg" alt="M02 熊猫" width="210"></a><br><strong>M02 熊猫</strong><br><a href="skills/zopc-commercial-visual-posters/assets/mascots/M02.png">查看 PNG 原图</a></td>
<td align="center" width="33%"><a href="skills/zopc-commercial-visual-posters/assets/mascots/M03.png"><img src="docs/previews/mascots/M03.jpg" alt="M03 机器人" width="210"></a><br><strong>M03 机器人</strong><br><a href="skills/zopc-commercial-visual-posters/assets/mascots/M03.png">查看 PNG 原图</a></td>
</tr>
<tr>
<td align="center" width="33%"><a href="skills/zopc-commercial-visual-posters/assets/mascots/M04.png"><img src="docs/previews/mascots/M04.jpg" alt="M04 柯基" width="210"></a><br><strong>M04 柯基</strong><br><a href="skills/zopc-commercial-visual-posters/assets/mascots/M04.png">查看 PNG 原图</a></td>
<td align="center" width="33%"><a href="skills/zopc-commercial-visual-posters/assets/mascots/M05.png"><img src="docs/previews/mascots/M05.jpg" alt="M05 奶牛猫" width="210"></a><br><strong>M05 奶牛猫</strong><br><a href="skills/zopc-commercial-visual-posters/assets/mascots/M05.png">查看 PNG 原图</a></td>
<td align="center" width="33%"><a href="skills/zopc-commercial-visual-posters/assets/mascots/M06.png"><img src="docs/previews/mascots/M06.jpg" alt="M06 兔子" width="210"></a><br><strong>M06 兔子</strong><br><a href="skills/zopc-commercial-visual-posters/assets/mascots/M06.png">查看 PNG 原图</a></td>
</tr>
<tr>
<td align="center" width="33%"><a href="skills/zopc-commercial-visual-posters/assets/mascots/M07.png"><img src="docs/previews/mascots/M07.jpg" alt="M07 棕熊" width="210"></a><br><strong>M07 棕熊</strong><br><a href="skills/zopc-commercial-visual-posters/assets/mascots/M07.png">查看 PNG 原图</a></td>
<td align="center" width="33%"><a href="skills/zopc-commercial-visual-posters/assets/mascots/M08.png"><img src="docs/previews/mascots/M08.jpg" alt="M08 企鹅" width="210"></a><br><strong>M08 企鹅</strong><br><a href="skills/zopc-commercial-visual-posters/assets/mascots/M08.png">查看 PNG 原图</a></td>
<td align="center" width="33%"><a href="skills/zopc-commercial-visual-posters/assets/mascots/M09.png"><img src="docs/previews/mascots/M09.jpg" alt="M09 水獭" width="210"></a><br><strong>M09 水獭</strong><br><a href="skills/zopc-commercial-visual-posters/assets/mascots/M09.png">查看 PNG 原图</a></td>
</tr>
<tr>
<td align="center" width="33%"><a href="skills/zopc-commercial-visual-posters/assets/mascots/M10.png"><img src="docs/previews/mascots/M10.jpg" alt="M10 小恐龙" width="210"></a><br><strong>M10 小恐龙</strong><br><a href="skills/zopc-commercial-visual-posters/assets/mascots/M10.png">查看 PNG 原图</a></td>
<td></td>
<td></td>
</tr>
</table>

**C01｜自定义小象示范**

<a href="skills/zopc-commercial-visual-posters/assets/custom-example/C01.png"><img src="docs/previews/mascots/C01.jpg" alt="C01 自定义小象，支持换成自己的角色" width="220"></a>

自定义可以上传已有形象，或描述物种、颜色和识别特征。

</details>

### 海报单图

<details>
<summary>展开 11 张独立海报，点击图片打开完整 PNG</summary>

<table>
<tr>
<td align="center" width="33%"><a href="skills/zopc-commercial-visual-posters/assets/styles/S01.png"><img src="docs/previews/styles/S01.jpg" alt="S01 星光开盒" width="260"></a><br><strong>S01 星光开盒</strong><br>示例：棕熊<br><a href="skills/zopc-commercial-visual-posters/assets/styles/S01.png">查看 PNG 原图</a></td>
<td align="center" width="33%"><a href="skills/zopc-commercial-visual-posters/assets/styles/S02.png"><img src="docs/previews/styles/S02.jpg" alt="S02 年度通行证" width="260"></a><br><strong>S02 年度通行证</strong><br>示例：水獭<br><a href="skills/zopc-commercial-visual-posters/assets/styles/S02.png">查看 PNG 原图</a></td>
<td align="center" width="33%"><a href="skills/zopc-commercial-visual-posters/assets/styles/S03.png"><img src="docs/previews/styles/S03.jpg" alt="S03 暖光开门" width="260"></a><br><strong>S03 暖光开门</strong><br>示例：柯基<br><a href="skills/zopc-commercial-visual-posters/assets/styles/S03.png">查看 PNG 原图</a></td>
</tr>
<tr>
<td align="center" width="33%"><a href="skills/zopc-commercial-visual-posters/assets/styles/S04.png"><img src="docs/previews/styles/S04.jpg" alt="S04 巨型字雕" width="260"></a><br><strong>S04 巨型字雕</strong><br>示例：小恐龙<br><a href="skills/zopc-commercial-visual-posters/assets/styles/S04.png">查看 PNG 原图</a></td>
<td align="center" width="33%"><a href="skills/zopc-commercial-visual-posters/assets/styles/S05.png"><img src="docs/previews/styles/S05.jpg" alt="S05 银色旗舰" width="260"></a><br><strong>S05 银色旗舰</strong><br>示例：自定义小象示范<br><a href="skills/zopc-commercial-visual-posters/assets/styles/S05.png">查看 PNG 原图</a></td>
<td align="center" width="33%"><a href="skills/zopc-commercial-visual-posters/assets/styles/S06.png"><img src="docs/previews/styles/S06.jpg" alt="S06 Builder工作台" width="260"></a><br><strong>S06 Builder工作台</strong><br>示例：企鹅<br><a href="skills/zopc-commercial-visual-posters/assets/styles/S06.png">查看 PNG 原图</a></td>
</tr>
<tr>
<td align="center" width="33%"><a href="skills/zopc-commercial-visual-posters/assets/styles/S07.png"><img src="docs/previews/styles/S07.jpg" alt="S07 宇宙巨物" width="260"></a><br><strong>S07 宇宙巨物</strong><br>示例：机器人<br><a href="skills/zopc-commercial-visual-posters/assets/styles/S07.png">查看 PNG 原图</a></td>
<td align="center" width="33%"><a href="skills/zopc-commercial-visual-posters/assets/styles/S08.png"><img src="docs/previews/styles/S08.jpg" alt="S08 红黑潮玩" width="260"></a><br><strong>S08 红黑潮玩</strong><br>示例：熊猫<br><a href="skills/zopc-commercial-visual-posters/assets/styles/S08.png">查看 PNG 原图</a></td>
<td align="center" width="33%"><a href="skills/zopc-commercial-visual-posters/assets/styles/S09.png"><img src="docs/previews/styles/S09.jpg" alt="S09 蓝紫星轨" width="260"></a><br><strong>S09 蓝紫星轨</strong><br>示例：兔子<br><a href="skills/zopc-commercial-visual-posters/assets/styles/S09.png">查看 PNG 原图</a></td>
</tr>
<tr>
<td align="center" width="33%"><a href="skills/zopc-commercial-visual-posters/assets/styles/S10.png"><img src="docs/previews/styles/S10.jpg" alt="S10 蓝白毛绒" width="260"></a><br><strong>S10 蓝白毛绒</strong><br>示例：奶牛猫<br><a href="skills/zopc-commercial-visual-posters/assets/styles/S10.png">查看 PNG 原图</a></td>
<td align="center" width="33%"><a href="skills/zopc-commercial-visual-posters/assets/styles/S11.png"><img src="docs/previews/styles/S11.jpg" alt="S11 紫色聚光舞台" width="260"></a><br><strong>S11 紫色聚光舞台</strong><br>示例：橙色柴犬<br><a href="skills/zopc-commercial-visual-posters/assets/styles/S11.png">查看 PNG 原图</a></td>
<td></td>
</tr>
</table>

</details>

当前样张均已去掉整块“赠 21 天实战营 ×2”。公开包仅含新版素材与使用说明，不包含历史原稿。

[回到顶部 ↑](#readme-top)

## 文档与资源

| 想了解什么 | 从这里开始 |
| --- | --- |
| 安装、目录位置与首次调用 | [安装使用步骤](docs/INSTALL.md) |
| 吉祥物的外形与单张视觉 | [吉祥物图册](docs/MASCOTS.md) |
| 每个海报的字体、气氛与原图 | [海报样式图册](docs/POSTERS.md) |
| 安装后没有出现、图片无法生成 | [使用帮助](docs/SUPPORT.md) |
| Skill 具体工作方式 | [SKILL.md](skills/zopc-commercial-visual-posters/SKILL.md) |
| 目录、角色与样式映射 | [素材索引](skills/zopc-commercial-visual-posters/references/catalog.json) |
| 维护素材、检查和预览图 | [维护说明](docs/MAINTAINING.md) |
| 本次信息架构的参考与取舍 | [仓库展示调研](docs/REPOSITORY-DESIGN.md) |

## 本地检查

辅助脚本使用 Python 3 标准库；实际图片生成由客户端提供。

在仓库根目录检查全部素材、文档链接与公开范围：

```bash
python3 scripts/check_repository.py
```

只检查 Skill 素材：

```bash
python3 skills/zopc-commercial-visual-posters/scripts/verify_assets.py
```

同样的检查会在 GitHub 的推送与 Pull Request 中运行。它验证文件和目录，不替代成图审稿或平台发布验收。

## 参与贡献

欢迎提交素材问题、安装问题和样式建议。请说明使用环境、形象编号、样式编号，以及预期和实际情况；示例请先移除个人或客户信息。

[报告问题](https://github.com/ai798-Lab/zopc-commercial-visual-posters/issues/new?template=bug-report.yml) · [提出样式建议](https://github.com/ai798-Lab/zopc-commercial-visual-posters/issues/new?template=style-request.yml) · [贡献指南](CONTRIBUTING.md)

## 许可与品牌

由 **[ai798 Lab](https://github.com/ai798-Lab)** 维护。当前仓库尚未指定开源许可证，也未附带图片模型服务或额度；品牌与素材的授权状态见 [使用与授权说明](docs/USAGE-RIGHTS.md)。

[回到顶部 ↑](#readme-top)
