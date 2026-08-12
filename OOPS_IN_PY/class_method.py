#Class method = allow operations related to the class itself
#Take (cls) as the parameter, which represents the class itself

class Student:
    
    count = 0
    
    def __init__(self,name,GPA):
        self.name = name
        self.GPA = GPA
        Student.count +=1
    
    #instance method 
    def get_info(self):
        return f"{self.name} has a GPA of {self}.GPA"
    
    #class method
    @classmethod
    def get_count(cls):
        return f"Total number of students {cls.count}"
    
s1 = Student("Karthik",9)
s2 = Student("Krishna",8.5)

print(Student.count)
print(Student.get_count())