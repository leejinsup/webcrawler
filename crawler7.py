#-*- coding: utf-8 -*-
# 뷰티플수프를 연습 파일 2
# 범위내 네이버 뉴스 파싱
# 기사본문 뽑아내기

import re
import urllib
from bs4 import BeautifulSoup

boardurl = "http://news.naver.com/main/read.nhn?mode=LPOD&mid=sec&oid=001&aid=0009138651"

html = urllib.urlopen(boardurl)
soup = BeautifulSoup(html, "lxml")

textsoup = str(soup)

timep = re.compile('\d{4}[-]\d{2}[-]\d{2}\s\d{2}[:]\d{2}')
article_time = timep.findall(textsoup)

print article_time

regex = '<!-- 본문 내용 -->[\w\W]+<!-- // 본문 내용 -->'
result = re.findall(regex, textsoup)
print type(result)
print("\n".join(result))
