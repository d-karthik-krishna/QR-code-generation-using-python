#  polymorphism means a single obejct can have more than one form

# Ways to activate polymorphism :
    # inheritance
    # Duck typing
    
    
from abc import ABC,abstractmethod

class shape:
    @abstractmethod
    def area(self):
        pass
        

class Circle(shape):
    def __init__(self,r):
        self.r = r
    
    def area(self):
        return 3.14*self.r**2

class Square(shape):
    def __init__(self,l):
        self.l = l
        
    def area(self):
        return self.l*self.l

class Triangle:
    def __init__(self,b,h):
        self.h = h
        self.b = b
        
    def area(self):
        return 0.5*self.b*self.h


shapes = [Circle(5), Square(5), Triangle(6,7)]
i=0
for shape in shapes :
    print(f"Area of shape number {i+1} is {shape.area()}")
    i+=1