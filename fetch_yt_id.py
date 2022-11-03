# %%
import urllib.parse
from pathlib import Path

import pandas as pd
import requests
from bs4 import BeautifulSoup

output = Path("output")
output.mkdir(exist_ok=True)


# %%
url = "https://www.calgary.ca/planning/downtown-level-up.html"
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")

entries = []
divisions = soup.find_all("div", {"class": "heading"})[2:]
for division in divisions:
    iframes = division.findNext("div").find_all("iframe")
    division = division.text.strip()
    for iframe in iframes:
        school = iframe.parent.parent.parent.find("h2").text.strip()
        yt_id = urllib.parse.urlparse(iframe.get("data-src")).path.rpartition("/")[-1]
        entry = dict(
            division=division,
            school=school,
            yt_id=yt_id,
        )
        entries.append(entry)

df = pd.DataFrame(entries)
df


#%%
df.to_csv(output / "entries.csv", index=False)


# %%
