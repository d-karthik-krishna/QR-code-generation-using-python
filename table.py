print("====Multiplication Table====\n")
a = int(input("Enter the number you want to find the table for : "))

print("how many tables do you want? (Enter possible from >=10 to <=50), enter in multiples of 10 only")
num = int(input())

if num==10:
    for prod in range(1,11):
        print(f"{a}x{prod}={a*prod}")
elif num==20:
    for prod in range(1,21):
        print(f"{a}x{prod}={a*prod}")
elif num==30:
    for prod in range(1,31):
        print(f"{a}x{prod}={a*prod}")
elif num==40:
    for prod in range(1,41):
        print(f"{a}x{prod}={a*prod}")
elif num==50:
    for prod in range(1,51):
        print(f"{a}x{prod}={a*prod}")
