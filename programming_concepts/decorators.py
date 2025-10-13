# decorator = a function that extends the behavior of another function 
# without modifying the base function 
# pass the base function as an argument to the decorator 

# @add_sprinkles 
# get_ice_cream("vanilla") 

def add_sprinkles(func):            # make decorator 
    def wrapper(*args, **kwargs):
        print("* You add sprinkles🎊 *")
        func(*args, **kwargs) 
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("* You add fudge 🍫*")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor): 
    print(f"Here is your {flavor} ice cream🍧")

get_ice_cream("vanilla")


# @add_sprinkles and @add_fudge is decorators 
# each decorator must include a wrapper function, 
# else the function will run without being called. 


