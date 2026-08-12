import random
low = 1
high = 10

guess = 0

num = random.randint(low,high)
while True:
    g = int(input(f"Guess a random number between {low} to {high}: "))
    guess+=1
    if g > num:
        print("A little lower")
    elif g<num:
        print("A little higher")
    else:
        print("You have found the number !")
        break;
print(f"Number of guesses taken to guess {num} is {guess} ")