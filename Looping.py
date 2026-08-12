name = input("Enter your name : ")
print(f"Your name is {name}")
#else
print("\nYour name is ",name)

age = input("Enter your age")
print(f"your age is {age}")

#age = age+1 doesnt work as the input is always taken in string datatype

age = int(age)
age = age +1
print(f"your age is {age}")

Age = int(input("\nEnter your new Age : "))# best to use, do the same for other numerical datatypes also
print(f"your age is {Age}")

Age = Age + 1
print(f"your age is {Age}")

for x in range(0,26,2):#increments by 2 the last digit, if it is -1 prints in reverse order 
    print(x,end=" ")
    