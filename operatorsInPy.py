#and 
#or
#not

#eg :
age = int(input("Age "))

if age >=18 and age <=80 :
    print("OLD NIGGA")
elif age >=18 or age <=100:
    print("naww")
else :
    print ("nigga")
    
hot = True 
if not hot :
    print("Rain")
else :
    print("hot ")

print("==============================\nCondOp")
# conditonal op in py
# syntax : if cond else cond
num = 6
result = "Even " if num%2==0 else "ODD"
print(f"{num} is {result}")