# format speifiers = {value:flags}

#.(number)f = round to that many decimal places (fixed point)
#:(number) = allocate that many places 
# :03 = allocate and zero pad that many places
# :< = left justify || :> = right justify
# :^ = center align 
# :+ = use a plus sign to indicate ppositve value
# := = place sign to leftmost position
# :  = insert a space before pos numbers 
# :, = comma seperators

price1 = 3.1444
price2 = -878878.55
price3 = 122.322
p4 = 90000000000

print(f"p1 is {price1:.2f} ")#decimal formatting (:.2f) 
print(f"p2 is {price2:.2f} ")
print(f"p2 is {price2:.2f} ")
print(f"\n\np1 is {price1:10} ")#space
print(f"\n\np1 is {price1:<10} ")#left justify space after left 
#same for other format specifies also
print(f"\n\np1 is {price1:+10} ")
print(f"\n\np1 is {p4:.3f} ")

print('Time')