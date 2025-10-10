# 2D lists = list of lists 

fruits = ["apple", "banana", "cherry", "kiwi"] 
vegetables = ["carrot", "potato", "cucumber"]
dairy = ["milk", "cheese", "yogurt"] 

# indexing and slicing works the same way as for 1D lists
groceries = [fruits, vegetables, dairy] 
print(fruits)
print(groceries[0]) # returns first list (first row)
print(groceries[0][1]) # returns second item in first list (second item in first row)

# iterate through 2D list
for collection in groceries: 
    print(collection)

# use nested loops to iterate through 2D list
for collection in groceries: 
    for food in collection: 
        print(food, end = " ") 
    print() 

# 2D tuple 

num_pad = ((1,2,3),
           (4,5,6), 
           (7,8,9,), 
           ("*",0,"#")) 

for row in num_pad: 
    for num in row: 
        print(num, end = " ") 
    print()


