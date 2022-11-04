# %%
from pathlib import Path

import matplotlib.pyplot as plt
from wordcloud import WordCloud

from utils import get_entries

df = get_entries()
df


# %%
texts = []
for yt_id in df["yt_id"]:
    transcription = Path(f"output/{yt_id}.txt")
    assert transcription.exists(), f"transcription {yt_id} doesn't exist."
    with open(transcription) as f:
        text = f.read()
    texts.append(text)


wc = WordCloud(
    background_color="white",
    colormap="plasma",
    random_state=2022,
).generate(" ".join(texts).lower())


fig = plt.figure()
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
fig.savefig("output/wordcloud", bbox_inches="tight", dpi=600)


# %%
