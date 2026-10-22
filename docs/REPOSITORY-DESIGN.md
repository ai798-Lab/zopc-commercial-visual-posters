# 仓库展示的参考与取舍

[返回首页](../README.md) · [维护说明](MAINTAINING.md)

调研日期：2026-10-22。主要参照用户指定的 [Lobe Icons](https://github.com/lobehub/lobe-icons)，借鉴阅读顺序和信息分层；文案、图像、数据与品牌全部使用 ZOPC 自己的资料。

## 成熟项目怎样组织信息

| 第一方项目 | 首屏与阅读顺序 | 语言、徽章与视觉 | 可借鉴的做法 | 不照搬的部分 |
| --- | --- | --- | --- | --- |
| [Lobe Icons](https://github.com/lobehub/lobe-icons) | 居中品牌区、简短定位、文档与反馈入口、徽章、折叠目录；随后说明价值、快速开始、样式展示、开发与贡献 | 英文主 README；徽章按包、检查与社区等目的分组；真实图标示例 | 让入口集中、先说明价值再展开资料，长目录与图册分层 | 品牌、图标、口号、用户数、软件包命令、奖项、赞助与许可证 |
| [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 品牌说明和真实界面后，区分安装路径，再给功能、示例与故障排查 | 英文主文档配多语言入口；状态徽章与截图共同提供事实 | 区分安装方式与生成能力，把常见问题放入独立文档 | 运行平台、模型与算力要求、云服务和发行承诺 |
| [Netron](https://github.com/lutzroeder/netron) | 简短用途、真实截图、平台安装入口与使用方式 | 英文 README；适合不同背景的品牌图；首页没有大量徽章 | 用途、效果、下一步比装饰数量重要 | 桌面软件下载方式、支持格式与平台兼容承诺 |
| [OpenAI Plugins](https://github.com/openai/plugins) | 交代目录用途，再说明结构与安装、贡献约定 | 英文主文档；以实际目录说明能力 | 明确分发单元与辅助资料的边界 | 不把当前 Skill 改装成插件，不复制其清单与安装命令 |

另核查过 [openai/skills](https://github.com/openai/skills)：调研当日其 README 已标记弃用并指向 Plugins，因此不把它作为仍在维护的安装规范来源。Codex 安装入口以 [官方 Skill 文档](https://developers.openai.com/codex/skills) 为准。

## 对应到这个项目

| 信息层 | 这次的具体处理 | 为何适合 ZOPC |
| --- | --- | --- |
| 品牌区 | 原创宽版首图、项目名、一句话定位、中英文切换 | 用户先看见实际可做出的视觉 |
| 主要入口 | 安装、样式、吉祥物与反馈集中在标题下面 | 不用先读完整图册才能找到安装 |
| 事实徽章 | 自动检查状态、10 个预设、11 个样式、自定义角色 | 数量来自当前目录，状态来自真实工作流 |
| 价值与开始 | 角色和样式可独立选择，给可复制调用示例 | 不暗示 Python 自己会出图 |
| 视觉样式库 | 两张总览直接展示，两个单图图册可展开；每张链接原始 PNG | 保留五项交付，控制首页长度与图片负担 |
| 文档分层 | 安装、图册、帮助、维护与研究独立 | 初次使用者和维护者的信息需求不同 |
| 社区入口 | 问题与建议表单、贡献指南、PR 模板 | 收集环境、编号和实际情况 |
| 后续维护 | 检查素材指纹、路径、公开范围与品牌图 | 减少断链或误带历史原稿的风险 |

## 内容与发布边界

- 默认中文，补充英文 README 与安装说明；不宣称图内文字或 Skill 交互已全部英文化。
- 首图与分享预览只组合当前真实样张、吉祥物和品牌原文件。SVG 保留可编辑布局，JPEG 用于实际展示。
- 使用相对路径；公开内容仅含当前版本，历史原稿与私人资料不进入公开提交。
- 不补造下载量、评价、认证、版本发布或服务承诺。未选择开源许可证，不复制参考项目的 MIT 授权。
- 未建立单独官网，因此不填写无关网址；未建立可用的私密安全收件渠道，因此不放置虚构邮箱。
- 原有 Skill 行为和素材文件不随本次首页装修改变。

## 展示规格与验收

首图为 1600×800 JPEG；单独制作的分享预览为 1280×640 JPEG，小于 1 MB，依据 [GitHub 官方社交预览文档](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview)。Topics 按 [GitHub 官方分类规则](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics) 选择具体词。

自动检查只核对文件、编号、指纹与链接。发布还需要在 GitHub 真实页面查看首图、语言切换、折叠图册与图片加载，并等待工作流运行；Settings 中的分享预览上传须单独核实。
