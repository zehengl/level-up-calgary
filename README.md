# level-up-calgary

![coding_style](https://img.shields.io/badge/code%20style-black-000000.svg)
[![GitHub Pages](https://github.com/zehengl/level-up-calgary/actions/workflows/gh-deploy.yml/badge.svg)](https://github.com/zehengl/level-up-calgary/actions/workflows/gh-deploy.yml)

A study on [Level Up, Calgary!][1]

## Environment

- Python 3.9

## Getting Started

    python -m venv .venv
    .venv\Scripts\activate
    python -m pip install -U pip
    pip install -r requirements.txt

> Configure `--extra-index-url` if CUDA is available, e.g. `pip install --trusted-host download.pytorch.org --extra-index-url https://download.pytorch.org/whl/cu118 -r requirements.txt`.
>
> Use `requirements-dev.txt` for development and docs.

## Usage

1.  Create a `.env` file and specify the `REQUESTS_CA_BUNDLE` path if you are `unable to get local issuer certificate`

        # .env
        REQUESTS_CA_BUNDLE="..."

2.  Run Scripts

        python fetch_yt_id.py
        python fetch_yt_mp3.py
        python transcribe.py
        python analyze.py

## Docs

    mkdocs serve

[1]: https://www.calgary.ca/planning/downtown-level-up.html
