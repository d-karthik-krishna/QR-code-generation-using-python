#list comprehension = a concise way to create lists 
#   compact ad easier to read than traditional loops
#    [expression for value in iterable if condtion]

doubles = [x*2 for x in range(1,11)] #list comprehension
print(doubles)

triples = [y*y for y in range(1,11)]
print(triples)

fruits = ["apples","orange","banana"]
print("before using the upper using the list comprehension")
print(fruits)
print("After using upper()")
fruits = [fruit.upper() for fruit in fruits]
print(fruits)
print()
numbers = [1,-2,4,5,7,99,108,6,-8]
postiveNumer = [num for num in numbers if num >=0]
print(postiveNumer)
print()
negativeNumbers =[num for num in numbers if num<0]
print(negativeNumbers)
EvenNumber = [num for num in numbers if num%2==0]
print()
print(EvenNumber)

grades =[85,42,66,78,90,35]
print()
PassingGrades = [grade for grade in grades if grade>=35]
print(PassingGrades)