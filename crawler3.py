#-*- coding: utf-8 -*-
# 뷰티플수프를 연습 파일
# 범위내 게시판 검색하여 유효한 게시물그림을 다운로드함
# 파일이름 저장은 게시물제목 + 처리순서

import re
import urllib
from bs4 import BeautifulSoup
fileNo = 0
boardurl = "http://bbs.ruliweb.com/community/board/300143/read/33084"

for i in range(500, 599, 1):
    stri = str(i)
    html = urllib.urlopen(boardurl + stri)
    soup = BeautifulSoup(html, "lxml")

    #img 태그를 모읍니다
    img_tag = soup.find_all("img")

    #img_tag는 클래스이므로 문자열로 변환해 줍니다.
    str_img = str(img_tag)

    #정규식을 이용하여 문자열에서 그림주소부분을 모두찾기함
    img_url1 = re.findall('https?://i\d.ruliweb.com/img/[^"]+', str_img)

    #파일명=타이틀태그의스트링, 파일내용=그림주소컨텐츠
    print soup.title.string
    for j in img_url1:
        contents = urllib.urlopen(j).read()
        file("./imgcollector/" + soup.title.string + str(fileNo), 'w').write(contents)
        fileNo = fileNo + 1

