from functools import partial
from tkinter import *


root = Tk()
root.title("펜션 티몬 크롤링")
root.geometry("640x180")

msg = Label(root, text="쿠팡 크롤링 주소 형식")
msg2 = Label(root, text="ex)https://search.tmon.co.kr/search/?keyword=가평펜션")

src = Text(root,width=50,height=3,padx=5) #크롤링 주소
src.insert(END,"") #사용자가 입력한 주소값을 전달받기 위한 코드
src.place(x=50,y=50)

from crawling_def import *
def textload():
    url = src.get("1.0",END)
    crawlings(url)


#btn = Button(root, width=10,height=3, text="크롤링 시작", command=partial(crawlings,"홍길동"))
btn = Button(root, width=10,height=3, text="크롤링 시작", command=textload)
btn.place(x=450,y=50)



# btn.pack(side="right")
# src.pack(side="left")
msg.pack()
msg2.pack()
root.mainloop()