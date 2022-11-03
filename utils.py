from pathlib import Path

import pandas as pd


def get_entries():
    entries = Path("output/entries.csv")
    assert (
        entries.exists()
    ), "entries.csv doesn't exist. Run fetch_yt_id.py if you haven't."
    df = pd.read_csv(entries)
    return df
