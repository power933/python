import matplotlib.pyplot as mpt # 그래프 모듈

x= [10,20,30,40]
y = [15,25,35,45]
mpt.plot(x,y,label="테스트 그래프",color="red")
mpt.legend()
for idx,txt in enumerate(y) :
    mpt.text(x[idx],y[idx],txt)
mpt.show()