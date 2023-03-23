<div align="center">
    <img src="https://cdn1.iconfinder.com/data/icons/ampola-final-by-ampeross/256/minecraft.png" alt="logo" height="128">
</div>

# level-up-calgary

![coding_style](https://img.shields.io/badge/code%20style-black-000000.svg)
[![pages-build-deployment](https://github.com/zehengl/level-up-calgary/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/zehengl/level-up-calgary/actions/workflows/pages/pages-build-deployment)

A study on [Level Up, Calgary!][3]

## Environment

- Python 3.9

## Getting Started

    python -m venv .venv
    .venv\Scripts\activate
    python -m pip install -U pip
    pip install -r requirements.txt
    python fetch_yt_id.py
    python fetch_yt_mp3.py
    python transcribe.py
    python analyze.py

Use `pip install -r requirements-dev.txt` for development and docs.

## Docs

    mkdocs serve

## Credits

- [Logo][1] by [Ampeross][2]

[1]: https://www.iconfinder.com/icons/86848/minecraft_icon
[2]: https://www.deviantart.com/ampeross
[3]: https://www.calgary.ca/planning/downtown-level-up.html
