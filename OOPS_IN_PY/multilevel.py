#A
#b(A)
#c{b}


class Animal:
    def __init__(self,name):
        self.name = name 
        print(f"My name is {self.name}")
    def eats(self):
        print("I eat ")
    
    
class Prey(Animal):
    def flee(self):
        print("This animal flees")

class Predator(Animal):
    def hunt(self):
        print("This animal hunts")

class Rabbit(Prey):#multilevel
    def __init__(self):
        self.flee()
        print("I am a rabbit!")
        self.eats()
    

class Fish(Prey,Predator):#multiple inheritance : A single class inherits properties from multiple base classes / hybrid
    def __init__(self):
        print("If I am smaller then")
        self.flee()
        print("If i am larger than other then")
        self.hunt
        print("I am a fish ")
        self.eats()

class Hawk(Predator):
    def __init__(self):
        self.hunt()
        print("I am a hawk")
        self.eats()
        
class Lion(Predator):
    pass
        
rabbit = Rabbit()
print()
hawk = Hawk()
print()
fish = Fish()
lion = Lion("SIMBA")