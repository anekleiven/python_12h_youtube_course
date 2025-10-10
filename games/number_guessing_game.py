# number guessing game 

import random 

lowest_num = 1
highest_num = 100 
answer = random.randint(lowest_num, highest_num)
guesses = 0 
is_running = True 

print("===================================")    
print("Welcome to my number guessing game!")
print("Are you ready to play?")
print(f"Select a number between {lowest_num} and {highest_num}.") 

while is_running: 
    guess = input("Enter your guess: ") 

    if guess.isdigit(): 
        guess = int(guess) 
        guesses += 1 

        if guess < lowest_num or guess > highest_num: 
            print("That number is out of range.") 
            print(f"Please select a number between {lowest_num} and {highest_num}.")
        elif guess < answer: 
            print("Too low. Tru a higher number.") 
        elif guess > answer: 
            print("Too high. Try a lower number.") 
        else: 
            print(f"Congratulations! The answer was {answer}.") 
            print(f"You guessed the number in {guesses} tries.") 

    else: 
        print("Invalid guess.") 
        print(f"Please select a number between {lowest_num} and {highest_num}.")
