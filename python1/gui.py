from tkinter import *

def abc():
    print("테스트 인쇄")


root = Tk()
root.title("연습 프로그램") #프로그램 타이틀 이름
root.geometry("500x500") #가로크기 * 세로크기
root.resizable(False,False) #사이즈 조절


txt = Entry(root,width=30)
txt.pack()
txt.insert(0,"테스트")

#Text(1="첫번째 행",0="열의 첫번째 위치", END="마지막 단어까지")
txt2 = Text(root,width=30,height=2)
txt2.pack()
txt2.insert(END,"ㅁㄴㅇ")

def aaa():
    url = txt.get()
    print(url)
    url2 = txt2.get(0.1,END)
    print(url2)

btn = Button(root,width=8, height=2,text="크롤링", command=aaa)
btn.pack()
btn1 = Button(root,text="클릭", command=abc)
btn2 = Button(root,padx=10,pady=2,text="클릭2")
btn1.pack()
btn2.pack()
root.mainloop()