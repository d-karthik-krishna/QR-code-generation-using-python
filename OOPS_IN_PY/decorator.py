#decorator is a fucntion that extends the behavior of another function 
#   q/o modifying the base func
#   Pass the bas func as an arg to the decorator

#   @add_sprinkles 
#   get_ice_cream{"vanilla"}

#declration of a decorator
def add_sprinkles(func):
    def wrapper(*args,**kwargs):
        print("You add sprinkles")
        func(*args,**kwargs)
    return wrapper

#a wrapper function must be returned because without it the whole code will be execued, that is base function will be executed regardless of calling it 

def add_fudge(func):
    def wrapper(*args,**kwargs):
        print("YOu add FUDGE")
        func(*args,**kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavour):# if we give args to the base function, then we need to declare args and kwargs in wrapper function to accept any num of args and kwargs, without this, the code wont run, it will show an error
    print(f"Here is your {flavour} ice cream")


get_ice_cream("Chocolate")

