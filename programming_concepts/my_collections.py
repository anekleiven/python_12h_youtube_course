# collection = single "variable" used to store multiple variables 
# list = [] ordered, changeable, allows duplicate members 
# tuple = () ordered, unchangeable, allows duplicate members
# set = {} unordered, unindexed, no duplicate members


# lists 

"""
fruits = ["apple", "banana", "cherry", "kiwi"] 
print(fruits[::-1]) # reverse 

for fruit in fruits: # iterate through list
    print(fruit)  

print(len(fruits)) # length of list

print("apple" in fruits) # check if item exists in list
fruits.append("orange") # add item to end of list 
print(fruits)

fruits[0] = "pear" # change item value 

for fruit in fruits: 
    print(fruit) 
 

fruits.remove("banana") # remove item from list
print(fruits)

fruits.insert(0, "pineapple")  # insert item at index
fruits.sort() # sort list
print(fruits)

print(fruits.count("kiwi")) # count occurences of item in list 

""" 

# sets 

"""

fruits = {"apple", "banana", "cherry", "kiwi"} 
print(fruits)
# print(type(fruits))  # Viser typen av objektet
# print(dir(fruits))   # Viser tilgjengelige metoder

# print(fruits[0]) # Dette vil gi en feil fordi sett er uordnet og ikke indeksert

fruits.add("orange")  # Legger til et element i settet
print(fruits)

fruits.remove("banana") # Fjerner et element fra settet
print(fruits)

"""

# tuples 
# faster than lists 

fruits = ("apple", "banana", "cherry", "kiwi") 
print(fruits)

print(len(fruits)) # length of tuple

fruits.count("kiwi") # count occurences of item in tuple
print(fruits.count("kiwi"))

print(fruits.index("cherry")) # get index of item in tuples