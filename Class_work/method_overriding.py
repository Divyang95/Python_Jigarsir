class A:
    def show(self):
        print("Show from class A")
class B(A):7
    def show(self):
        super().show()
        print("show from class B")
class C(A):
    def show(self):
        super().show()
        print("show from class C")
class D(C,B):
    def show(self):
        super().show()
        print("show from class D")

d1 = D()
d1.show()

#its drawback of class inheritance now if we want to call show method of class b then we have to make object of B and same for object of A
#it means we have to make object of all then what use of inheritance we introduced inheritance because we want to call all methods each parent
#there are two way you use super().show() in child class then when we call that metho using the child class then both child class method and parent class method calls automatically
#but if we want to call only parent class method then use Parent.show(obj)
