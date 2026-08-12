#this program is for genetating random numbers
import random #use help(lib_nam/listetctec) to get its details

low = 1
high = 100

number = random.randint(low,high)
print(number)
print( random.random())#for generating a float num >0and <1

option = ("rock","Paper","Scissors")

print(random.choice(option))

card = ["2","3","4","5","6","7","8","9","10","j","Q","K","A"]
print((card))
random.shuffle(card)
print(card)