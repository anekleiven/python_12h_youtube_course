# membership operators = used to test whether a value of variable is found in a sequence
# string, list, tuple, set, dictionary 

word = "APPLE" 

letter = input("Guess a letter in the secret word: ").upper()

if letter in word: 
    print(f"There is a {letter} in the word!")
else: 
    print(f"Sorry, {letter} is not in the word.")
          

# set 

students = {"Jim", "Michael", "Pamela"}

student = input("Enter a student name: ") 

if student in students: 
    print(f"{student} is in the class.")
else: 
    print(f"{student} is not in the class.")


# dictionary 

grades = {"Jim": "A", 
         "Pamela": "B", 
         "Michael": "C"}

student = input("Enter a student name: ") 

if student in grades: 
    print(f"{student}'s grade is {grades[student]}.")  # access value in dictionary using key 
else: 
    print(f"{student} was not found.") 
    

# string 

email = "ane.kleiven@gmail.com"

if "@" and "." in email: 
    print("Valid email") 
else: 
    print("Invalid email") 

    