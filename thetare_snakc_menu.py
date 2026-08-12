Menu = {"Popcorn": 50.00,
        "Coke": 45.00,
        "Potato Chips": 35.00,
        "Onion Chips": 35.00,
        "Thumbs up": 40.00,
        "Pastries": 45.00}

total = 0
Cart = []

print(f"=====Menu=====")
for snack,price in Menu.items():
    print(f"{snack:15}: ${price:.2f}")

while True:
    snack = input("Enter the food item you want to buy, Enter Q to exit : ")
    if snack == 'q'.lower():
        break
    elif Menu.get(snack) is not None:
        Cart.append(snack)
    else:
        print(f"No {snack} in the Menu, Try again!")

for price in Cart:
    total += Menu.get(price);

print("=====Your Cart=====")
for food in Cart:
    print(food,end=" ")
print()
print(f"Your total bill is ${total:.2f}")

