# import modules
import pandas as pd
import numpy as np
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = Request('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
res = urlopen(req)
html = res.read().decode('cp949')

bs = BeautifulSoup(html, 'html.parser')
tags = bs.findAll('div', attrs={'class': 'tit3'})
crawlDatas = ['test']

for tag in tags :
    # 검색된 태그에서 a 태그에서 텍스트를 가져옴
    #print(tag.a.text)
    crawlDatas.append(tag.a.text)

# DataFrame 초기화
df = pd.DataFrame()

df["영화제목"] = crawlDatas
print(df)

df.to_excel('./test2.xlsx', sheet_name= 'Sheet1')