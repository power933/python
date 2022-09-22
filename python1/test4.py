import pickle


data = {"고객명":"홍길동","나이":25,"취미":["볼링","축구","야구"]}
files = open("file.pickle","wb")
# w=wb 파일생성 및 저장(인코딩 필요 없음)
pickle.dump(data,files)
#dump : 객체를 생성 및 저장
files.close()

files2 = open("file.pickle","rb")
loadfile = pickle.load(files2)
print(loadfile)

#with를 사용해서 이용되는 pickle
with open("file.pickle","wb") as files : #as : 변수명 만들기와 같은 개념
    pickle.dump(data,files)

with open("file.pickle","rb") as files2:
    loadfile = pickle.load(files2)
print(loadfile)

with open("abc.txt","w") as textfile :
    textfile.write(data)

