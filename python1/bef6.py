from bs4 import BeautifulSoup
from requests import *

url = "https://www.koreabaseball.com/TeamRank/TeamRank.aspx"
result = get(url)
result.raise_for_status()
#해당 사이트에 접속하여 devtool로 볼 경우 데이터가 확인이 되지만
#실제 크롤링 후 스크래핑 시 데이터가 확인 안될 경우는 AJAX 및 JS로
#직접 태그가 생성되도록 제작되어있음. 이럴경우 스크래핑 하기가 어려워짐

html = BeautifulSoup(result.text,"lxml")

baseball = html.find("div",attrs={"id":"cphContents_cphContents_cphContents_udpRecord"})
team = baseball.find("tbody")
tr = team.find_all("tr")

z = 0
for a in tr :
    td = tr[z].find_all("td")
    print(td[1])
    z+=1
    

