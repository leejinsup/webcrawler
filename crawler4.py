#-*- coding: utf-8 -*-
# 뷰티플수프를 연습 파일 2
# 범위내 네이버 뉴스 파싱

import re
import urllib
from bs4 import BeautifulSoup

boardurl = "http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=001&aid=0009136"

for i in range(801, 850, 1):
    stri = str(i)
    html = urllib.urlopen(boardurl + stri)
    soup = BeautifulSoup(html, "lxml")

    article_time = str(soup.find_all('span', {'class':'t11'}))
    article_title = soup.title

    timep = re.compile('\d{4}[-]\d{2}[-]\d{2}\s\d{2}[:]\d{2}')
    authorp = re.compile('[기][자]')

    article_time = timep.findall(article_time)
    author = authorp.findall(soup.string)

    print article_time,str(i),article_title
