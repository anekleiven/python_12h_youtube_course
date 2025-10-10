# keyword arguments = arguments that are passed to a function by explicitly naming each parameter and specifying its value 
# help with readability and allows for out of order arguments 

def hello(greeting, title, first, last): 
    print(f"{greeting} {title} {first} {last}") 

hello(greeting = "Hello", title="Mr.", first = "John", last = "Smith") 

hello(last="Larsen", first="Kim", title="Dr.", greeting="Hey") 


for x in range(1,11): 
    print(x, end =" ") 

print("1", "2", "3", sep="-")


# the print function has 3 keyword arguments 
# sep = string inserted between values, default is a space
# end = string appended after the last value, default is a newline
# file = a file-like object (stream); defaults to the current sys.stdout


def get_phone(country, area, first, last): 
    return f"{country}-{area}-{first}-{last}" 

phone_num =get_phone(area="123", country="+45", first="456", last="7890") 
print(phone_num)