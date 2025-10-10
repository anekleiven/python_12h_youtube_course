# list comprehensions = a way to create a new list with less syntax 
# compact and easier to read than traditional loops 
# [express for value in iterable if condition]

# regular way

doubles = []

for x in range(1,11): 
    doubles.append(x * 2) 

print(doubles) 


# list comprehension way 

doubles = [x * 2 for x in range(1,11)]    # for every value in the range, multiply it by 2 and add it to the list 
print(doubles)

triples = [y * 3 for y in range(1,11)]
print(triples) 

squares = [z * z for z in range(1,11)]
print(squares)

fruits = [fruit.upper() for fruit in ["apple", "banana", "cherry", "kiwi", "mango"]] 
print(fruits) 



# using conditions 

number = [1, -2, 3, -5, 6, -7] 
positive_nums = [num for num in number if num > 0] 
negative_nums = [num for num in number if num < 0]
even_nums = [num for num in number if num % 2 == 0]
odd_nums = [num for num in number if num % 2 == 1] 

print(odd_nums) 

grades = [85, 42, 79, 90, 56, 61, 30]

passing_grades = [grade for grade in grades if grade >=60]
failing_grades = [grade for grade in grades if grade < 60] 

print(passing_grades)
print(failing_grades)
