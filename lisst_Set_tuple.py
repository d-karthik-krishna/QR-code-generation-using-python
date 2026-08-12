# List = [] ordered and changeable, Dups OK
# set = {} unordered and immuatable, but add \ remove OK, Dups NO
# Tuple = () ordered and unchangeable, Dups OK, Faster

Fruits = ["a","c","b","b","igfsg"]
print(Fruits[2])

for fruit in Fruits:
    print(fruit)
print("\n")
Fruits.sort() #listName.Func()
print(Fruits)
for fruit in Fruits:
    print(fruit)

Fruits.append("Mango") # . remove, .insert(0,"pinesjdfh")
print(f"\n{Fruits}")

Name = [ "v","x","a","fff","mm","z"]
Name.sort()
Name.reverse()
print(Name)
Fruits.reverse()
print(Fruits)
print(Name.count("z"))
