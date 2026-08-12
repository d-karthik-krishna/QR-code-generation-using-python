import time

Time = int(input("Enter the time in seconds : "))

for x in range(Time,0,-1): # or for x in reversed(range(0.TIme))
    print(x)
    time.sleep(1)
print("Time is UP!")
