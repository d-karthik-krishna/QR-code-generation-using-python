#Keyword args = an arg preceded by an identifier
#   helps with readability, order of arg doesnt matter, (types )positional, default, KEYWORD, arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")
    
hello("Hello","Mr","loa","da")
#same code for invokiung the function but with keywords :
hello("hello",first = "lou",title = "mr",last ="da")

print("1","2","3","5",sep="_")

print("Phone number genrator:\n ")
def getPhone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"
print(getPhone(91,123,456,7894))

#Args 
#kwars

def add(a,b):
    return a+b
print(add(5,6))

#for sending many number of args in to the the same fuinction name we use *args 

def addtion(*args): #you can give any names, not just args, this returns the data in tuple
    total = 0
    for arg in args:
        total += arg
    return total

print(addtion(1))
print(addtion(1,2))
print(addtion(1,2,3,6))

#kwargs = keyword args

def print_add(**kwargs):#stores in a dictionary
    for val in kwargs.values():#prints values, if you select keys, it will print keys in the dictionary 
        #if you give items, you should declare it as like keyvalue pairs
        print(val,end=" ")#get method will give you the value of the key you want to get

print_add(street="4th cross",city = "KGF", state = "KA", pin = 563115)