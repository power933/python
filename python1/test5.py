class box :
    def __init__(self,a,b,c) :
        self.a = a
        self.b = b
        self.c = c
        print("값은{0},{1},{2}".format(self.a,self.b,self.c))

    def abc(self):
        print(self.c)
class box2(box) :
    def __init__(self,a,b,c):
        box.__init__(self,a,b)
        self.data3 = c
    def abcd(self) :
        print("값은 {0},{1},{2}")


cl = box(5,6,7)
cl.abc()