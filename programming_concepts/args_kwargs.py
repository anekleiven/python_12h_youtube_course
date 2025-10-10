# *args = allows you to pass multiple non-keyword arguments to a function = tuple 
# **kwargs = allows you to pass multiple keyword arguments to a function = dictionary 
# * unpacks a list or tuple into positional arguments


def add(a,b):  # can only take 2 arguments 
    return a + b 

print(add(2,3))


def add(*args): # can take any number of arguments 
    total = 0 
    for arg in args: 
        total += arg 
    return total 

print(add(2,3,4,5,6,7,8,9,10)) 


def display_name(*args): 
    for arg in args: 
        print(arg, end = " ") 

display_name("John", "Doe") 


# kwargs 

def print_address(**kwargs): 
    for key, value in kwargs.items(): 
        print(f"{key}: {value}")

print_address(street = "123 Main St", 
              city = "New York", 
              state = "NY", 
              zip = "10001")


def shipping_label(*args, **kwargs): 
    for arg in args: 
        print(arg, end = " ")
    print() 

    if "apt" in kwargs: 
        print(f"{kwargs.get('street')}, {kwargs.get('apt')}")  # use single quotes to avoid conflict with double quotes in f-string 
    elif "pobox" in kwargs: 
        print(f"{kwargs.get('pobox')}, {kwargs.get('street')}")
    else: 
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('state')}, {kwargs.get('zip')}")


shipping_label("Dr.", "Johhny", "Linkoln", "III",
               street = "123 Main St",
               pobox = "456",
               city = "New York", 
               state = "NY", 
               zip = "10001")


