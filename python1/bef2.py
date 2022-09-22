from bs4 import BeautifulSoup
from os import *    #운영체제가 기본으로 제공하는 모듈
from requests import *
url = get("https://naver.com")
print("응답코드 : ",url.status_code)
if url.status_code == codes.ok:
    print(url.text)
    print("웹사이트 정상적인 페이지")
else :
    print("보안코드에 문제가 있음")

