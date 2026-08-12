fruits = ["a","M","O"]
Vegetables = ["C","P","O"]
Meats = ["Ch","Mu","Fish"]
# same for sets and tuples 
Groceries = [fruits,Vegetables,Meats] #Can be declared like [] = [[],[],[]]

print(Groceries)

Meats[0]="Chicken"

print(Groceries[2][0])
print(" ")

#Accessing 2dL

for Groecery in Groceries:
    print(Groecery,end = ", ")
print(" ")

print(" ")
for Grocery in Groceries:
    for food in Grocery: 
        print(food,end = " ")
    print()

