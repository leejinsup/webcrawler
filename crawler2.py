#파이썬과 정규식을 이용 이미지를 저장하는 코드
import re
import urllib
fileNo = 0
racingGirlUrl = 'http://gall.dcinside.com/list.php?id=racinggirl&no='
for no in range(170715, 170720):
        url = racingGirlUrl + str(no)
        f = urllib.urlopen(url)
        html = f.read()
        imageUrlList = re.findall("http://image.dcinside.com/download.php[^']+", html)
        print imageUrlList
        for url in imageUrlList:
                print fileNo
                contents = urllib.urlopen(url).read()
                file(str(fileNo), 'w').write(contents)
                fileNo = fileNo + 1
