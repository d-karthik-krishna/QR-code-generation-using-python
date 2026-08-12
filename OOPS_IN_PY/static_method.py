#static method dont need self to declare them 

class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position= position 
        
    def get_info(self):
        return f"{self.name} is a {self.position}"
    
    @staticmethod
    def is_valid(position):
        valid_positions = ["cahsier","Cook","Manager"]
        return position in valid_positions
    
emp1 = Employee("Karthik","Cook")
print(emp1.get_info())
print(Employee.is_valid("Cook"))