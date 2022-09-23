from tkinter.messagebox import *
import requests
from bs4 import BeautifulSoup
from re import *
from sqlite3 import *
from dbconnect import *
from datetime import *


def crawlings(data) : 
    # showinfo(data)
    if len(data)==1 or len(data)<20 :
        showinfo("경고", "크롤링할 url을 입력해야 합니다")
    else :
        #try :
            
            #today = datetime.now().replace(microsecond=0)
            url = data
            check = requests.get(url.strip())
            ck = check.raise_for_status()
            #url : https://browse.auction.co.kr/search?keyword=%ED%8E%9C%EC%85%98%EC%98%88%EC%95%BD
            print("123123")
            print(check)
            if str(ck)=="None" :
                html = BeautifulSoup(check.text,"lxml")
                div = html.find("div",attrs={"module-design-id":"17"})
                div2= div.find_all("div",attrs={"class":"section--itemcard"})
                # titles = div2[0].find("span",attrs={"class":"test--title"})
                # money = div2[0].find("strong",attrs={"class":"text--price_seller"})
                #DB접속 정보를 로드

                con = connect.cursor()
                print(con)
                for z in div2 :
                    
                    titles = z.find("span",attrs={"class":"text--title"})
                    money = z.find("strong",attrs={"class":"text--price_seller"})
                    money = sub(",","",money.text)
                    print(titles.text,money)
                    now_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    sql = "insert into pension values('0','"+titles.text+"','"+money+"','"+now_date+"')"

                       # con.execute(sql,(titles.text,money,today))
                    con.execute(sql)
                    connect.commit()




                showinfo("성공","정상적으로 모든 데이터를 스크래핑 완료했습니다.")
        #except :
          #  showinfo("실패","주소를 다시 확인해주세요")

        # url = str(data) 
        # check = requests.get(url)
        # check.raise_for_status()

