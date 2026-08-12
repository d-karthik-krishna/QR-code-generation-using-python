#functions in python 

#syntax for defining a function in python :
    #def fun_name():
        # function body
        
# to call a function just call it

def birthday():
    print("Happy birthday!!")

for x in range(3):
    print(f"{x+1}",end=" ")
    birthday()
    
def birthday(name):
    print("Itterashai "+name)
    
birthday("Eren")

#you can send different number of arguements, youcan you function overloading, same as in c++, java 

def add(a,b):
    return a+b
z = add(1,2)
print(f"Your sum is {z}")

def sub(a,b):
    z = a-b
    return z
print("Sub is ",(sub(1,2))) # + is used fr strings and , is used for calling functions inside a print statement 

#default arguments in python 
print()
def net_price(list_price,discount=0,tax=0.05): #we need to set the default values in the function definition itself, and while calling it, it depends on us if we want to use those parameters also 
    return list_price * (1-discount)*(1+tax)

print(f"Your net price amount is {net_price(500)} ")
print(f"Your net price amount is {net_price(500,0.1)} with an discount of 5% ")
print(f"Your net price amount is {net_price(500,0.1,0.02)} with an discount of 5% and a tax of 0.02% ")