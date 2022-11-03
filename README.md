<div align="center">
    <img src="https://cdn1.iconfinder.com/data/icons/ampola-final-by-ampeross/256/minecraft.png" alt="logo" height="196">
</div>

# level-up-calgary

![coding_style](https://img.shields.io/badge/code%20style-black-000000.svg)

A study on Level Up, Calgary!

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

Use `pip install -r requirements-dev.txt` for development.
It will install `pylint` and `black` to enable linting and auto-formatting.
It will also install `jupyterlab` for notebook experience.

## Docs

    mkdocs serve

## Credits

- [Logo][1] by [Ampeross][2]

[1]: https://www.iconfinder.com/icons/86848/minecraft_icon
[2]: https://www.deviantart.com/ampeross
