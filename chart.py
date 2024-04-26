import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd

res = req.get("https://music.bugs.co.kr/chart")

soup = bs(res.text, "lxml")

ranking = soup.select(".ranking > strong")
title = soup.select(".title > a")
artist = soup.select(".artist >a:nth-child(1)")

rankingList = [r.text.strip() for r in ranking]
titleList = [t.text.strip() for t in title]
artistList = [a.text.strip() for a in artist]

chart_df = pd.DataFrame({
    'Ranking' : rankingList,
    'Title': titleList,
    'Artist' : artistList
})

chart_df.to_json("bugsChart100.json", force_ascii=False, orient="records")
