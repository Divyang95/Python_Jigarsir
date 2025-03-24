from abc import ABC,abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def speed(self,speed):
        pass

    def show(self):
        print("This is vehicle")
class Bike(Vehicle):
    def show(self):
        print("Bike class")
    def speed(self,speed):
        print("my bike speed",speed)

class Car(Vehicle):
    def show(self):
        print("Car class")
    def speed(self,speed):
        print("my car speed",speed)

b1 = Bike()
b1.show()
b1.speed(140)

c1 = Car()
c1.show()
c1.speed(220)
        
