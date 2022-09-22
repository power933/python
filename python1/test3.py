
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.naver.com")
object = BeautifulSoup(html, "html.parser")

files = open("naver.html","w",encoding="utf-8")
print(object,file=files)
files.close()
