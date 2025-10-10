# dictionary = key-value pairs 
# ordered, changeable, no duplicate keys 
# {key:value} 

# make a dictionary 
capitals = {"USA": "Washington DC",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"
            }

# look at a dictionaries methods 
print(dir(capitals))

# access values 
print(capitals.get("USA")) # returns value for key
print(capitals["India"]) # returns value for key

# check if key exists 
if capitals.get("Japan"): 
    print("Japan is in the dictionary") 
else: 
    print("Japan is not in the dictionary")

# add items
capitals.update({"Germany": "Berlin"})

print(capitals)

# remove items
capitals.pop("China") # removes item with specified key 

print(capitals)

# keys 
keys = capitals.keys() 
print(keys) 

for key in capitals.keys(): 
    print(key)

# values 
values = capitals.values() 
print(values)

for value in capitals.values(): 
    print(value)


# items 
items = capitals.items()
print(items)

for key, value in capitals.items(): 
    print(f"The capital of {key} is {value}")