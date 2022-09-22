from dataclasses import asdict
from urllib.request import urlopen
from bs4 import BeautifulSoup
from os import *    
from requests import *
from tkinter import *
from idlelib.iomenu import encoding
import urllib.request

root = Tk()
root.title("웹페이지 크롤링")
root.geometry("500x100")
root.resizable(False,False)

url = Text(root,width=40,height=2)
url.pack()
url.insert(END,"url을 입력하세요")

def pageload() :
    urladdr = url.get(0.1,END)
    check = get(urladdr)
    if check.status_code == codes.ok:
        html = urlopen(urladdr)
        object = BeautifulSoup(html,"html.parser")
        files =  open("test.html","w",encoding="utf-8") 
        print(object,file=files)
        files.close()
        print("정상완료 되었습니다")
    else:
        print("오류")

btn = Button(root,text="웹크롤링",command=pageload)
btn.pack()

root.mainloop()
