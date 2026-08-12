import  random

options = ("rock","paper","scissors")
running = True

print("Your Choices are : ")

for op in options :
    print(op,end=" ")
    
while running:
    player = None
    computer = random.choice(options)
    
    while player not in options: 
        player = input("\nEnter a choice : ")

    print(f"Player : {player}\nComputer : {computer}")

    if player == computer:
        print("TIE!!!")

    elif player == "rock" and computer == "scissors":
        print("You win!")

    elif player == "paper" and computer == "rock":
        print("You win!")

    elif player == "scissors" and computer == "paper":
        print("You win!") 
    else :
        print("YOU LOSE!!")
    
    play_again = input("You want yo try the game agian? (y/n)").lower()
    
    #if not input("Play again(y/n)").lower == "y":
    if play_again == "n":
        running = False