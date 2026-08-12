class Company:
    class Employee:
        def __init__(self,name,position):
            self.name = name 
            self.position = position
            
        def get_det(self):
            return f"{self.name} at {self.position}"
        
    def __init__(self,compName):
        self.compName = compName
        self.empl = []
        
    def Add_empployee(self,name,position):
        new_emp = self.Employee(name,position)
        self.empl.append(new_emp)
        
    def list_employees(self):
        return [employee.get_det()  for employee in self.empl]
    
"""class NonProfit:
    class Employee:
        print("This is the 2nd class")"""

company = Company("INDIA COMPANY")
company.Add_empployee("karthik","HR")
company.Add_empployee("krishna","project manager")
company.Add_empployee("eren jeagar","GOAT")

print(company.list_employees())
print()
for employees in company.list_employees():
    print(employees,"\n")
