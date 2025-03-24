
    
#init method does not need to call manually it calls automatically when we make class of that object
#whatever argument passed in init that number of argument also passed in object
#same another magic method __str__(self): gives string when print object at that time string mwthod called
class Point:
    def __init__(self,x,y):
        print("init called")
        self.x = x
        self.y = y
    def __str__(self):
        print("str called")
        return "{0},{1}".format(self.x,self.y)
    def __add__(self,obj):
        print("add called")
        x = self.x + obj.x
        y = self.y + obj.y
        return Point(x,y)

p1 = Point(10,20)
print(p1)
p2 = Point(30,40)
print(p2)
print("Addition of 2 objects :", p1+p2)
