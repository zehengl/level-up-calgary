# %%
from pathlib import Path

import librosa
import pandas as pd
import torch
from tqdm import tqdm
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

entries = Path("output/entries.csv")
assert entries.exists(), "entries.csv doesn't exist. Run fetch_yt_id.py if you haven't."
df = pd.read_csv(entries)
df


# %%
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")


# %%
for yt_id in tqdm(df["yt_id"].tolist(), desc="transcribing"):
    speech, _ = librosa.load(f"output/{yt_id}.mp3", sr=16000)
    input_values = tokenizer(speech, return_tensors="pt").input_values
    logits = model(input_values).logits[0]
    pred_ids = torch.argmax(logits, dim=-1)
    transcriptions = tokenizer.decode(pred_ids)
    with open(f"output/{yt_id}.txt", "w") as f:
        f.write(transcriptions)


# %%
