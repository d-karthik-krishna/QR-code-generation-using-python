Foods = []
Prices = []
total = 0

while True :
    food = input("What do you want to buy? Enter Q to quit : ")
    if food == 'q' or food == 'Q': #food.lower() == 'q'
        break
    else :
        price = float(input(f'Enter the  price of {food}: $'))
        Foods.append(food)
        Prices.append(price)

print("=====Your Items=====\n")

for Food in Foods :
    print(Food, end= " ")
print("\n")

#for p,f in Prices and Foods :    # zip() concepts should be learnt to execute these type of statement # for food, price in zip(foods, prices):
    #print(f"For {food} Price is {p}")

for Price in Prices:
    total += Price
    
print(f"Your total is {total:.2f}$")