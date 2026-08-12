#zip() = Combines multiple iterables (lists, tuples, sets, dict)
#       into a single iterator of tuples.
#       Makes managing multiple indices easier.

names = ["Spongebob", "Patrick", "Squidward"]
ages = [30, 35, 50]
jobs = ["Cook", "Unemployed", "Cashier"]


# for i in range(len(names)):
#    name = names[i]
#    age = ages[i]
#    print(f"{name } {age}")


data = zip(names, ages, jobs)
i =1
for name, age, job in data:
    print(f"{i}: {name} is a {age} year old {job}")
    i+=1