# 维护与展示说明

[返回首页](../README.md)

## 仓库组织

- 首页按“总览 → 单张视觉 → 安装与使用”组织，回应本次五项交付要求。
- 单张预览采用压缩 JPEG，每张链接到完整 PNG；公开仓库只含新版素材，不包含历史原稿。
- 公开版从不含历史原稿和旧Git对象的全新目录建立，避免旧图进入提交历史。\n- 使用相对路径，不绑定维护者电脑。生成底稿、聊天记录、本地配置和临时验收路径不进入仓库。
- 以中文使用者为主，不另造无人维护的翻译、徽章或社区模板；未替所有者选择开源许可证。

## 参考过的仓库模式

| 第一方参考 | 可沿用的模式 | 本仓库的处理 |
| --- | --- | --- |
| [openai/skills](https://github.com/openai/skills) | 用途之后给明确安装入口 | 用真实目录URL调用安装器，不广告不存在的软件包 |
| [anthropics/skills](https://github.com/anthropics/skills) | Skill独立目录、区分工作流和客户端能力 | 完整Skill放入skills子目录；不承诺所有客户端都能生成图片 |
| [obra/superpowers](https://github.com/obra/superpowers) | 解释工作流与实际安装方式 | 展示形象→样式→信息→成图→延展，并说明已核对的Codex入口 |

以上仓库的品牌、徽章与许可未复制为本项目内容。视觉示例使用本项目真实生成的海报和形象。

## 更新后检查

```bash
python3 skills/zopc-commercial-visual-posters/scripts/verify_assets.py
```

替换原图时同步更新 `references/asset-manifest.json` 中的尺寸、大小和指纹；替换样式与角色映射时同步更新 `references/catalog.json` 和预览图。新增输入字段时核对 `scripts/poster_brief.py` 的提示词与校验，避免继承旧活动事实。

发布前检查README、安装说明与单图页的图片链接。图像能解码只证明文件完整，还需要看实际成图和GitHub渲染。
