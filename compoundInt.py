principle = 0
rate =0
time = 0
while principle <=0 : 
    principle = float(input("Enter the principle amount : " ))
    if principle <= 0 :
        print("Principle cant be 0 or less than 0")

while rate <= 0 : 
    rate = float(input("Enter the rate : " ))
    if rate <= 0 :
        print("rate cant be 0 or less than 0")
        
while time <= 0 : 
    time = float(input("Enter the time : " ))
    if time <= 0 :
        print("time cant be 0 or less than 0")
        
print(f"Principle : {principle} | Time : {time} | Rate : {rate}")

total = principle * pow((1+rate/100),time)
print(f"Balance after {time} years : {total:.2f}")