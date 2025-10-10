# while loop = execute some code while some condition remains true 
# remember exit strategy 

name = input("Enter your name: ")

while name == "": 
    print("You did not enter your name") 
    name = input("Enter your name: ")
print(f"Hello, {name}")


age = int(input("Enter your age: "))

while age < 0: 
    print("Age can't be negative.") 
    age = int(input("Enter your age: ")) 
print(f"You are {age} years old.")


food = input("Enter a food you liker (q to quit): ") 

while not food == "q": 
    print(f"{food} is a great food!") 
    food = input("Enter a food you like (q to quit): ")

print("Program ended.")


num = int(input("Enter a number between 1 and 10: ")) 

while num < 1 or num > 10: 
    print(f"{num} is not valid.")
    num = int(input("Enter a number between 1 and 10: ")) 
print(f"You entered {num}.")
    
