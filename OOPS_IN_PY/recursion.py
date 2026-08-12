#recursion = a function that calls itself from within
#       helps to visualize a complex problem into basic steps
#       problems can be solved more easily iteratively or recursively
#       iterative = faster, complex
#       recursive = slower, simpler

#recursive apporach
def walk(steps):
    if steps == 0:
        return
    walk(steps-1)
    print(f"You took step #{steps}")

walk(100)#if we give 1000 there will be a recursion error saying that max cap for recursion has been reached

print()
print()

#iteratives should be used for  larger number becuse it doesnt have a max range to iterate the values

def wal(steps):
    for step in range(1, steps +1):
        print(f"{step} number ")
        
wal(1000)