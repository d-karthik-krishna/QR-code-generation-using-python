#class variable = Shared among all instances of a class
# declared outside a constructor 
# Allows you to share data among all objects created from that class

class Student:
    name = "karthik"
    year = 1002
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
s1 = Student("KK",21)
s2 = Student("sdh",1000)
print(f"{s1.name} , {s1.age}\n{s2.name} , {s2.age}")

print(s1.year)

print(Student.name)