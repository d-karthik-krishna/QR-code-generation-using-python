#if__name__==__'__man__': ( this script can be imprted or run standalone)
    # functions and classes in this module can be reused
    # withoit the main block of the code executing
    #can be used like a python library, like importing muiltiple scripts 
    
#   
def square(a):
    return a*a

print(dir())
def main():
    a = 10
    print(a)
    print(dir())
    
if __name__== '__main__':
    main()
    print(__name__)
    print(f"square of 100 is {square(100)}")