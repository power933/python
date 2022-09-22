from bs4 import BeautifulSoup
from requests import *

url = "https://www.koreabaseball.com"
result = get(url)

print(result.raise_for_status())
#status 코드에 대한 문제사항 출력 None(전혀 문제 없음)
html = BeautifulSoup(result.text,"lxml") #lxml : 자동파서(설치필요)
cartoon = html.find("span",attrs={"class":"team-name"})
# atag = cartoon.find_all("span")
print(cartoon)