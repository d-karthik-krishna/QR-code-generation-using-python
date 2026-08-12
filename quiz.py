questions = ("Who is the biggest nigga of this colleger?",
             "who is the biggest dumbass of this college?",
             "who is the biggest indian superstar?",
             "babu lakey babu ?",
             "RTC cross roads records?")
options = (("you","me","all","NONE")
           ,("you","me","all","NONE")
           ,("Prabhas","Allu BHAAI","Ram Charan","Jr NTR"),
           ("kalyan babu","Mahesh babu","Ballayya babu","Sampoornesh babu"),
           ("1","2","3","4"))

guesses = []
answers =("B","B","A","B","D")

score = 0
Qn_no=0

for Question in questions:
    print("\n----------------------\n")
    print(Question)
    
    for option in options[Qn_no] :
        print(option,end=" ")
        
    guess = input("\nEnter A,B,C,D :").upper()
    guesses.append(guess)
    
    if guess == answers[Qn_no]:
        print("\nCorrect answer")
        score+=1;
    else :
        print("Incorrect \n"+answers[Qn_no]+" Is the correct answer")
    Qn_no+=1

print("\n====aNSWERS====")
for ans in answers :
    print(ans,end = " ")
print("\n====Guesses====")
for guess in guesses : 
    print(guess,end = " ")
print(f"\nTotal score is {score}/5")