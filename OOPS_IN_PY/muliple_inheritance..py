# class C(A,B)
class Prey:
    def flee(self):
        print("This animal flees")

class Predator:
    def hunt(self):
        print("This animal hunts")

class Rabbit(Prey):
    def __init__(self):
        self.flee()
        print("I am a rabbit!")
    

class Fish(Prey,Predator):#multiple inheritance : A single class inherits properties from multiple base classes
    def __init__(self):
        print("If I am smaller then")
        self.flee()
        print("If i am larger than other then")
        self.hunt
        print("I am a fish ")

class Hawk(Predator):
    def __init__(self):
        self.hunt()
        print("I am a hawk")
        
        
rabbit = Rabbit()
print()
hawk = Hawk()
print()
fish = Fish()
