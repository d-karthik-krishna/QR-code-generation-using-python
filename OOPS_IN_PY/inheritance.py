class Animal:
    def __init__(self,name ):
        self.name = name 
        self.is_Alive = True
        
    def eat(self):
        print(f"{self.name} is eating happily ")
    
    def sleep(self):
        print(f"{self.name} is sleeping peacefully ")
        
class Dog(Animal): # syntax for inheriting in pythoon class subClass(BaseClass)
    def __init__(self,name):
        super().__init__(name)
        print("I BARK BOW BOW")
    
class Cat(Animal):
    pass
    
class Horse(Animal):
    pass

dog = Dog("SKibidi")
cat = Cat("LARRY")
horse = Horse("JUAN")

print()
dog.eat()
print(dog.is_Alive)
dog.sleep()

