#dictionary = a collection of {key:value} pairs
#              ordered and changeable, No duplicates

capitals = {"India": "New Delhi", 
            "USA": "Washington DC",
            "Russia": "Moscow",
            "Japan": "Tokyo"}

#print(dir(capitals))
#print(help(capitals))

#methods of a dictionary

Cap = capitals.get("USA")
print(Cap)
print(capitals.get("India"))
print(capitals.get("China"))# prints none as there is no china in out dictionary

if(capitals.get("Japan")):
    print("Cap of japan is there in the dictionary")
else:
    print("Not there")
    
capitals.update({"China": "Beijing"})
print(capitals.get("China"))
print()
print(capitals)
print()
print("Capitals of these countires are present")
for cap in capitals:
    print(cap,end=", ")
    
#capitals.pop("China")
#capitals.popitem() clears the last recently added key
#capitals.clear() clears the dictionary
print("\n")
keys = capitals.keys()
print(keys)
print()
print(capitals.values())
print("\n")
for value in capitals.values():
    print(value)
print("\n") 
#capiitals.items() prints a tuple of key and values 

for key,value in capitals.items():
    print(f"{key:10}: {value}")
