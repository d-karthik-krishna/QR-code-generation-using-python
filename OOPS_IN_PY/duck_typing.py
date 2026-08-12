# this is another way to achieve polymorphism 
# object must have the minimum necessary attributes/methods
# "If it looks like a duck and quacks like a duck, it must be a duck"

class Animal:
    alive = True
    
class Dog(Animal):
    def speak(self):
        print("BOW BOW")
        
class Cat(Animal):
    def speak(self):
        print("MEOW MEOW")


class Car(Animal):
    
    #def horn(self):
        #print("HONK")
        
    alive = False
    def speak(self):
        print("HONK")

animals = [Dog(),Cat(),Car()] #if you add car here, it wont work, because it doesnt have a speak method, if you add the speak methhod insted of horn, it will work, hence if it looks like a duck, it is a duck

for animal in animals :
    animal.speak()
    print(animal.alive)