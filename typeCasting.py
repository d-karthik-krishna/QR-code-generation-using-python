name = " nigga"
age = 99
gpa = 9.25
student = False

# prints the data type of the variables ',' is used like how we use in C
print("name is of type : ",type(name))
print("age is of type : ",type(age))
print("Gpa is of type : ",type(gpa))
print("Student value of type ",type(student))

#explicit type casting
age = float(age)
student = str(student)
gpa = int(gpa)
print("\n")
print("Below is using explicit typecasting")
print("name is of type : ",type(name))
print("age is of type : ",type(age))
print("Gpa is of type : ",type(gpa))
print("Student value of type ",type(student))

age = bool(age)#if age is not 0 then the value of this will be True only


#implicit type casting
print("\n\n")
z = 2
y = 2.0
z = z/y

print(z)