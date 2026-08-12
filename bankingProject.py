

def show_balance(balance):
    print(f"Your balance is {balance:.2f}")

def deposit():
    dep = float(input("Enter the Deposit amount : "))
    if dep<0:
        print("Invalid entry")
    else :
        print(f"Amount of {dep:.2f} was deposited successfully ")
        return dep

def withdraw():
    wit  = float(input("Enter the amount to withdraw: "))
    return wit

def main():
    balance = 0
    running = True 

    while running:
        print("\n")
        print("---BANKING PROJECT---")
        print("enter 1 for viewing your balance\nEnter 2 for depositing\nEnter 3 for withdrawing\nEnter 4 to exit")
        choice = int(input("Enter your choice : "))
    
        match choice:
            case 1:
                show_balance(balance)
            case 2:
                balance+=deposit()
            case 3 :
                wit = withdraw()
                if wit<balance:
                    balance -= wit
                    print(f"Amount of {wit:.2f} was successfully withdrawn")
                    show_balance(balance)
                else:
                    print("Withdraw amount is more than your balance\nYour current balance is : ")
                    print(balance)
            
            case 4:
                running = False
            case _: 
                print("Invalid choice")
    
if __name__=='__main__':
    main()
