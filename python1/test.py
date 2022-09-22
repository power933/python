print("테스트")

username = "홍길동"
a = 19
b = 4
if(a>b): username = "이순신"

#숫자는 항상 형변환(str)시켜서 출력해야함
print(username +"님 환영합니다 포인트는" + str(b)+"점 입니다" )

print(10%3) #나누기
print (10//3) #소수점 출력 없이 정수 출력
print(2**3) #제곱근
i = 5
# for i in range(10):
    # print(i)

x = False
if(not x & 3>2>1) : print("123")

print(abs(-100)) #abs : 절대값
print(pow(2,3)) #pow : 제곱근
print(max(10,8)) #max : 최대값 , min : 최소값

import imp
from math import *
print(floor(7.1))
print(ceil(7.1))

import math #import 2가지 방법.
print(math.floor(7.1))
print(math.ceil(7.1))

from random import *
print((int)(random()*10))
print(randrange(1,10)) #범위내 임의 숫자 생성(미만)
print(randint(1,2)) #범위내 임의숫자(이하)

msg = '''잘 지내?'''
# ''' : 문자열 출력
print(msg)

gender = "910830-1234567"
print("성별 : " + gender[7])
print("생일 : "+ gender[2:6]) #0부터 시작

if(gender[7] == "1") : 
    print("남자")
elif(gender[7] == "2") : print("여자")
else :print("새천년어른이")
word = "Mojo Incoming"
print(word.upper()) #전부 대문자로
print(word.lower()) #전부 소문자로
print(word[0].islower())
print(len(word))    # .length
z = word.index('o')
print(z)
z = word.index("o", z+1) # z+1 : 설정없을시 첫번째, +1 : 그 다음 o 찾아라
print(z)

print("{}님 회원등급은 {}입니다".format("유관순","5"))

qqq = ["이순신","유관순"]
# .appen, .insert, .extend, pop() : 값을 뒤에서부터, sort()

infodata = {"mid":"hong", "mname":"홍길동"}
print(infodata["mname"] + infodata.get("mid")) #두개가 같음
infodata["tel"] = "01012345678"
del infodata["mid"]

list = {1,2,3,4,1,2,3} #셋 : 중복값 출력 안함
print(list)