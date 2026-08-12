#object  = something which describes an class
# class = blueprint of classes or it is an structure and layout of an object
# methods are something which are declared using classes andd obections, whereas functions dont use classes and objects 
 
class Car:
    def __init__(self, model, year, colour, for_sale): #this is a constructor 
        self.model = model
        self.year = year 
        self.colour = colour
        self.for_sale = for_sale
        
    def start(self):
        print("Car is starting")
        print(f"You have started {self.model} and it is (true if for sale ){self.for_sale}")
        
car1 = Car("mustang",99,"blue",False)
print(car1)

print(car1.model)        

#methods are actions that an object can perform
car1.start()