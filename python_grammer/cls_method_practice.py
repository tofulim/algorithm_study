class Dot :
    x,y="0","0"
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    @classmethod
    def class_method(cls, x,y):
        print("cm started",x,":",y)
    
    @staticmethod
    def static_method(x,y):
        print("sm started",x,":",y)

a=Dot(1,2)

print(a.x,":",a.y,type(a.x))
Dot.class_method(2,3)
Dot.static_method(3,4)
a.class_method(4,5)