#switch case in python is known as match case 

def calci(choice):
    match choice:
        case 1:
            return "addtion"
        case 2:
            return "subtraction"
        case 3:
            return "multiplication"
        case 4:
            return "division"
        case _: #instead of default 
            return "invalid"
        
ch = int(input("Enter your choice : "))
print(calci(ch))

#|| = | = OR

print()
print(2%2==0|5%5==0)
print()
print(2%2==0 or 5%5==0)