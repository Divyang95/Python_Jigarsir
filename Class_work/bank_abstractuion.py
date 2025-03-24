from abc import ABC,abstractmethod

class RBI(ABC):

    @abstractmethod
    def intrest(self,roi):
        pass

    def show(self):
        print("This is RBI")
class HDFC(RBI):
    def show(self):
        print("HDFC class")
    def intrest(self,roi):
        print("my HDFC ROI",roi)

class Kotak(HDFC):
    def show(self):
        print("Kotak class")
    def intrest(self,roi):
        print("my Kotak ROI",roi)

h1 = HDFC()
h1.show()
h1.intrest(5)

c1 = Kotak()
c1.show()
c1.intrest(2)
