print("Enter 1 for addition | 2 for Subtraction | 3 for Multiplication | 4 for division |  5 to exit ")
while(True):
    Choice = int(input("Enter your Choice : "))
    if Choice == 1:
        a= float(input("Enter the number : "))
        b = float(input("Enter the 2nd number : "))
        print(f"Result : {a+b:.2f}")
    elif Choice == 2 :
        a= float(input("Enter the number : "))
        b = float(input("Enter the 2nd number : "))
        print(f"Result : {a-b:.2f}")
    elif Choice == 3 :
        a= float(input("Enter the number : "))
        b = float(input("Enter the 2nd number : "))
        print(f"Result : {a*b:.2f}")
    elif Choice == 4 :
        a= float(input("Enter the number : "))
        b = float(input("Enter the 2nd number : "))
        if b == 0 :
            print("Division with 0 is not possible ")
        else :
            print(f"Result : {a*b:.2f}")
    elif Choice == 5 :
        print("Exiting..........")
        exit()
    else : 
        print("Invalid entry, try again!")