item = input("what item would you like to buy? ")
price = int(input("What is the price of the item ? "))
qty = int(input("Enter the quantity of the item "))

total = price * qty

print(f"\nyou have bought {item} of quantity {qty} the total bill amount was {total}")