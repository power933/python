from bs4 import BeautifulSoup
from os import *    #운영체제가 기본으로 제공하는 모듈

# htmlcode = BeautifulSoup("<div><span>테스트</span></div>")
# soup = BeautifulSoup("<span><b><i>테스트</i></b></span>")
# print(soup.prettify)

dictory="html"
print(getcwd()) #현재 경로
mkdir(dictory) #mkdir : 디렉토리생성
