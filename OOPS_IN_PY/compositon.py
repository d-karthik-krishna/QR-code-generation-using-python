#Compositon : the composed object directly owns its components, which cannot exist independently 

class Engine:
    def __init__(self,HP):
        self.HP = HP

class Wheels:
    def __init__(self,size):
        self.size = size

class Car:
    def __init__(self,make, model, HP,W_size):
        self.make = make
        self.model = model 
        self.engine = Engine(HP)
        self.wheels = [Wheels(W_size) for wheel in range(4)]
        
    def display_Car(self):
        return f"{self.make} {self.model} {self.engine.HP}(hp) {self.wheels[0].size}inches"
        
        
car1 = Car(make="Ford",model="Mustang",HP=8500,W_size=18) # can be initialized W/O using the keyword args 

print(car1.display_Car())