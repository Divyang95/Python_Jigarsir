class Student:
    def getStudent(self,fname,lname):
        self.f = fname
        self.l = lname
    def printStudent(self):
        print("First Name is :",self.f)
        print("Last Name is : ", self.l)

s1 = Student()
fn = input("Enter First name : ")
ln = input("Enter last name:")

s1.getStudent(fn,ln)
s1.printStudent(fn,ln)
