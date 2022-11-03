# %%
import pandas as pd
import youtube_dl
from pathlib import Path


# %%
entries = Path("output/entries.csv")
assert entries.exists(), "entries.csv doesn't exist. Run fetch_yt_id.py if you haven't."
df = pd.read_csv(entries)
df


# %%
opts = {
    "outtmpl": "output/%(id)s",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
        },
    ],
}
with youtube_dl.YoutubeDL(opts) as ydl:
    ydl.download(df["yt_id"])


# %%
