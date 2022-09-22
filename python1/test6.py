class box:
    def __init__(self,data1):
        self.data1 = data1

class box2:
    def __init__(self,data2):
        self.data2 = data2
    
class box3(box,box2):
    def __init__(self,data1,data2,data3):
        self.data3 = data3
        box.__init__(self,data1)
        box2.__init__(self,data2)
        print("데이터값{0},{1},{2}".format(self.data1,self.data2,self.data3))

a = box3("홍길동","강감찬","이순신")  
print(a)