#This program demonstrates a credit card's validation

sum_odd_digits = 0
sum_even_digits = 0
total = 0

card_number = input("Enter a credit card number: ")
card_number = card_number.replace("-","")
card_number = card_number.replace(" ","")
card_number = card_number[::-1]#reversing the credit number to add the odd and double the digits from right to left 

for c in card_number[::2]:
    sum_odd_digits+= int(c)
    
for c in card_number[1::2]:
    c = int(c)*2
    if c>=10 :
        sum_even_digits += (1+(c%10))
    else :
        sum_even_digits += c
        
total = sum_even_digits+sum_odd_digits

card_number = card_number[::-1]
if total%10==0 :
    print(f"Your credit card number : {card_number} is valid")
else :
    print("INVALID")