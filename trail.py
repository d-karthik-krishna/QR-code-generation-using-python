import time
#is used for comments
print("Nigga")
print(3+4)
 
# 'f' in print is used to format the print statements 
# {} is used to bring the variable inside the print statements

#these are strings in Python
Name = "Karthik"
print(Name)
print(f"Hello {Name}") 
food = "Potato"
print(f"You look like a {food}")

#these are integers
age = 67
print(f"\nyou are {age} old nigga")

# float
price = 6.9
cgpa = 9.04

print(f"The price of the item is {price}\nYoure CGPA is {cgpa}")

#boolean

is_true = False
is_False = False

print(f"Are you a student ?\n{is_true}")

if is_true:
    print("You are a student")
else :
    print("You are not a student")
print("\n\n")   
print("Timer is running below") 
Time = 10
for x in reversed(range(0,Time)):
    print(x)
    time.sleep(1)
print("Time is up")