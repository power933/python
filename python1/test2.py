
list = [9,12,17,22]
# for i in range(0,30):
#         if i in list :
#             print(i)

for i in range(2,4):
    for j in range(1,10) :
        print(i*j)

data = [2,5,7,3,1]
data = [i+5 for i in data]
print(data)

def aaa(a):
    print("함수 {}".format(a))

aaa(123)

box = "변수값"
def afunction():
    global box3
    print(box)
    box2 = "변수2"
    print(box2)
    box3 = "변수3"
    print(box3)

def bfunction() :
    print(box)
    print(box3)

# afunction()
# bfunction()

for number in range(1,30):
    # print("대기번호" + str(number).zfill(3))
    a = 0
#open("파일명","읽기(r),쓰기(w),수정(a)",언어셋)
# files = open("./data.txt","w",encoding="utf-8")
# print("홍길동",file=files)
# print("이순신",file=files)
# files.close()

# files = open("./data.txt","a",encoding="utf-8")
# print("유관순",file=files)
# files.close()

files = open("./data.txt","r",encoding="UTF-8")
print(files.read())

while True :
    line = files.readline()
    if not line :
        break
    # print(line)
files.close()

