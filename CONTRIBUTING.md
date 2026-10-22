# 参与贡献

[返回首页](README.md)

欢迎改进安装文档、修复素材问题或提出新的视觉样式。提交前先说明你要解决的实际问题，并标明影响的形象/样式编号。

## 提交内容

- 说明改动后的行为或展示效果，附脱敏后的前后对比。
- 保留现有编号；新增形象和样式时同步更新目录、素材清单、预览图与中英文README中的数量。
- 图片、Logo和形象素材应有明确来源与可使用依据。不要提交私人聊天、个人路径、账号信息、客户材料或历史原稿。
- 不把准备好的提示词、文件校验或截图误写成图片生成、平台发布或购买流程已经完成。

## 检查

```bash
python3 scripts/check_repository.py
```

确认当前公开包仍然只有已批准的新版素材。图片替换后逐图审稿；文件检查不代替视觉检查。

## English

Describe the problem, affected IDs and resulting behavior. Provide redacted before/after examples when helpful. Keep catalog, manifests, previews and both README variants consistent. Do not add private data or historical originals. Run `python3 scripts/check_repository.py` before submitting.
