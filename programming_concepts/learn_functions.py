# functions = a block of reuable code 
#             place () after the function name to call it 

# defining a function
def happy_birthday(name, age):
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} years old!")
    print(f"Happy Birthday to you!")
    print() 

happy_birthday("Alice", 30)    # call the function
happy_birthday("Bob", 25)      
happy_birthday("Charlie", 22)


def display_invoice(username, amount, due_date): 
    print(f"Hello, {username}.")
    print(f"Your bill of ${amount} is due: {due_date}")


display_invoice("Alice", 250.75, "07/31/2024")

# return = statement used to exit a function 
# send result back to caller 

def add(x,y):
    z = x + y 
    return z 

def subtract(x,y): 
    z = x-y 
    return z

def multiply(x,y): 
    z = x*y
    return y 

def divide(x,y): 
    z = x/y 
    return     

print(add(5,3))
print(subtract(5,3))
print(multiply(5,3))
print(divide(5,3))

# full name function 

def create_name(first, last): 
    first = first.capitalize()
    last = last.capitalize() 
    return first + " " + last 

full_name = create_name("spongebob", "squarepants")

print(full_name)


