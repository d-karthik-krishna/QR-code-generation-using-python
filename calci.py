'''
Syntax for if 

if condition:
    statement(s)
else :
    statement(s)
NOTE : indentations are very imp in py
else if = elif in py

if :
    ksjfh
elif cond: 
    sfh
else :
    fls
'''
'''
food = input("y/n? ")

if food == "y":
    print("FoOd")
else :
    print("Fuck of Nigga No food for you")
'''

op = input("Enter the operation you want to perform (+ - * / %) ")
a = float(input("Enter the first number : "))
b = float(input("Enter the Second number : "))

if op == "+" :
    print(f"Result is {a+b}")
elif op == "-":
    print(f"Result is {a-b}")
elif op == "*":
    print(f"Result is {a*b}")
elif op == "/":
    if b==0:
        print("Division by 0 is not possible")
    else :
        print(f"Result is {round(a/b,2)}")
elif op == "%":
    if b==0:
        print("Division by 0 is not possible")
    else :
        print(f"Result (reminder )is {round(a%b,2)}")
else :
    print("Enter a correct operator ")