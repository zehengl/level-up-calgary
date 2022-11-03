# %%
import youtube_dl

from utils import get_entries

df = get_entries()
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
