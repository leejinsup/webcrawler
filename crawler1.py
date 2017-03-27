#-*- coding: utf-8 -*-
# 뷰티플수프를 이용 이미지파일의 소스를 불러오는 코드

import urllib
from bs4 import BeautifulSoup

# Get all img address at html

for i in range(140, 150, 1):
    stri = str(i)
    html = urllib.urlopen('http://bbs.ruliweb.com/community/board/300143/read/33025'+ stri)
    soup = BeautifulSoup(html, "lxml")

    for link in soup.find_all('img'):
        print(link.get('src'))
