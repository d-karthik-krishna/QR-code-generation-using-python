## variable scope where a variable is visible and accessible
# scope res = (LEGB) : local->Enclosed->Global->Built in 

from math import e#built in 

c = 3 #global scope
def fuc():
    a = 1#local scope
    print(a)
    print()
    def func2():
        a = 2#enclosed 
        print(a)
        print()
        print(e)#built in 
    func2()

def func():
    b = 2
    print()
    print(c)#global 
    print()
    print(b)#local scope
    
fuc()
func()