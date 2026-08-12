# Data Class = A special kind of class that's designed mostly for holding data
#                        without writing a lot of the boilerplate code for regular classes.
#                        They automatically generate: _init__, __repr__, __eq_
#                       (Python 3.7+)

from dataclasses import dataclass
from dataclasses import field
@dataclass 
class Person:
    name: str
    age: int
    password: str = field(repr=False) #field is a spcl member class used to define on how the member classes behave, this line of code helps us hide the details only this attribute that is password will be hidden
    is_alive: bool = True
   # we didnt declarae the magic methods for this, reducing the code lines 
    
    def __post_init__(self):
        if self.age<0:
            raise ValueError("Age cannot be negative")
   
person1 = Person("name",30,"p11")
print(person1)
person2 = Person("hheheh",45,"sdfk")
print(person2)
print(person2 == person1)
print(person1.is_alive == person2.is_alive)
#person3 = Person("Name",-7)
#print(person3)
#person2.age = 40 throws an error showing that they are not mutable
#print(person2)