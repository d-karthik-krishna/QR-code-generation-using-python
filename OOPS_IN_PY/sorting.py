# two types : .sort(), sorted() depends  on the DS we are using like lists[], typles(), Dictionary{"":""} and objects

#============================================================
#lists

fruits = ["banan","apple","orange"]
print(fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse = True)
print(fruits)
#============================================================
print("\n\n")
#============================================================
#tuples

vegetables = ("potato","beans","tomato")
#vegetables.sort() wont work here, as vegetables is a tuple
print(vegetables)
vegetables = sorted(vegetables)#converts the tuple into a list 
print(vegetables)
vegetables = tuple(sorted(vegetables))#keeps the tuple as a tuple only, it does not convert it into a list, we are type casting it
print(vegetables)
vegetables = tuple(sorted(vegetables, reverse=True))
print(vegetables)
#============================================================
print("\n\n")
#============================================================
#dictionary

sports = {1:"Football",
          2:"Cricket",
          3:"Hockey"}
print(sports)
print(sports.values())
for value in sports.values():
    print(value,end = " ")
print()  
sports = dict(sorted(sports.items()))
print(sports)
sports = dict(sorted(sports.items(),key=lambda item: item[0], reverse=True))
print(sports)
sports = dict(sorted(sports.items(), key = lambda item: item[1]))
print(sports)
sports = dict(sorted(sports.items(), key = lambda item: item[1], reverse= True))
print(sports)
#============================================================
print("\n\n")
#============================================================
#objects

class Fruit:
    def __init__(self,name, calories):
        self.name = name
        self.calories = calories
        
    def __repr__(self):
        return f"{self.name} : {self.calories}"
    
Fruits = [Fruit("Banana",105),Fruit("Apple",95),Fruit("Mango",150)]
print(Fruits)
Fruits = sorted(Fruits,key = lambda pandu: pandu.name)
print(Fruits)
Fruits = sorted(Fruits,key = lambda pandu: pandu.name, reverse=True)
print(Fruits)
#same goes for calories also
#==========================================================