"""

# input() = a function that lets user input data 

name = input("What is your name?") # the string inside the parentheses is called a prompt
age = int(input("How old are you?")) 

age = age + 1 

print(f"Hello, {name}!") 
print("HAPPY BIRTHDAY")
print(f"You are {age} years old")


# Exercise 1 rectangle area calculator

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width 

print(f"The area of the rectangle is {area}cm²")

""" 

# Exercise 2 Shopping cart program 

item = input("Enter the item you want to buy: ")
price = float(input("What is the price of the item? ")) 
quantity = int(input("How many do you want to buy? "))
total = price * quantity 

print(f"You have bought {quantity} {item}(s)") 
print(f"Your total is: ${total}") 
print("Thank you for shopping with us!")
print("Welcome back!")


