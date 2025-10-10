# iterables = an object/collection than can return its elements one at a time, 
# allowing it to be iterated over in a loop. Examples: lists, tuples, dictionaries, sets, string

# iterate over a list 

numbers = [1,2,3,4,5]

for item in numbers: 
    print(item)

for item in reversed(numbers): # reverses the order of the list
    print(item, end = ' ') # end = ' ' keeps everything on the same line with a space in between


# iterate over a tuple 

integers = (2,3,4,5) 

for item in integers: 
    print(item)

# iterate over a string 

fruits = {'apple', 'banana', 'cherry'}

for fruit in fruits: 
    print(fruit)

# strings 

name = "Ane Kleiven" 

for character in name: 
    print(character, end = " ")

# dictionaries 

my_dictionary = {"A": 1, "B": 2, "C": 3} 

for key in my_dictionary: 
    print(key)  

for value in my_dictionary.values(): 
    print(value) 

for key, value in my_dictionary.items(): 
    print(f"{key} = {value}")




