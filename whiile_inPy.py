age = 10
#Syntax 
# while condition :
    #statements 
while age != 15:
    print(age, end = '\t')
    age+=1


#for loop
#Syntax :
    #for x in range (begRange,EndRange) :
        #statements 
        
print("\n\nFor loop executes below ............")
for x in range(1,5):
    print(x, end = '\t')
print("\n\nFor loop using incrementation")   
for x in range(1,11,2):#increments the x value by 2
    print(x,  end ="\t")
    
#nested loops in Py
print("\n\nBelow demonstrates nested loops in Py")

for x in range(4):
    for y in range(1,5):
        print(y,end=" ")
    print()


print("\n") 
rows = int(input("Enter the number of rows : "))
cols = int(input("Enter the number of Cols : "))
Symb = input("Enter a symbol to use : ")

for x in range(rows):
    for y in range(cols):
        print(Symb,end=" ")
    print()