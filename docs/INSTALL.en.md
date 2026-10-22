# Installation and use

[中文](INSTALL.md) · [README](../README.en.md)

## Requirements

Use a Codex environment that supports local skills. Creating images also requires an available image generation or editing capability in your client and account. This package does not include a model service or credits.

Catalog, brief and asset checks require Python 3, with no third-party Python packages. Normal use is conversational; users do not need to write JSON.

## Install through Codex

Paste this into a Codex conversation:

```text
$skill-installer install https://github.com/ai798-Lab/zopc-commercial-visual-posters/tree/main/skills/zopc-commercial-visual-posters
```

Wait for the complete directory to download. Open a new conversation and invoke:

```text
Use $zopc-commercial-visual-posters to create an event poster.
Show me the mascot and style galleries first.
```

If it does not appear, restart Codex. If a skill with the same name is already installed, inspect and back up the existing version before updating it.

## Manual installation

1. [Download the repository ZIP](https://github.com/ai798-Lab/zopc-commercial-visual-posters/archive/refs/heads/main.zip).
2. Extract it and locate `skills/zopc-commercial-visual-posters`.
3. Copy that complete folder to your local skill directory. The current documented user location is `~/.agents/skills/`; a project-scoped location is `.agents/skills/` in that project.
4. Start a new conversation, or restart Codex if the skill is not visible.

Do not copy only `SKILL.md` or install the same skill into multiple discovery locations.

## Use

Choose M01–M10 or provide a custom character. Then choose S01–S11 and supply the activity title, main points, platform, size and call to action. Supply price, dates, logos and QR assets only when needed. Existing information should not be requested again.

The skill generates and reviews the first poster, then asks whether you want related campaign materials. If a whole suite was authorized initially, it works within that scope.

Instructions and example artwork currently use Chinese. This is English documentation of the same package.

## Check the installed assets

From the installed skill folder:

```bash
python3 scripts/verify_assets.py
python3 scripts/catalog.py mascots
python3 scripts/catalog.py styles
```

Asset checks validate files and indexes. They do not generate images or prove that a poster is visually correct.

Installation locations and discovery follow [official OpenAI skill documentation](https://developers.openai.com/codex/skills). Last checked: 2026-10-22.
