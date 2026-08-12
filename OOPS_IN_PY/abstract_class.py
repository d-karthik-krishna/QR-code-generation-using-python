# A class that cannt br instantiated on its own is called as an abstract classes

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
# vehicle = Vehicle()   we cannot use abstract class's methods

class Car(Vehicle):# once a class is inheriting an abstract class, it has to implement all its methods inside the inherited class
    def go(self):
        print("YOu can drive a car")
    def stop(self):
        print("You can stop a car")
    
        
car = Car()
car.go()
car.stop()

class Boat(Vehicle):

    def go(self):
        print("You can sail a boat")
    def stop(self):
        print("The boat has been anchored ")
        
boat = Boat()
boat.go()
boat.stop()
