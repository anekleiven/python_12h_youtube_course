# hangman in python 

import random 
from hangman_words import words

# dictionary of key:() 
hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")} 


def display_man(wrong_guesses):
    print("-" * 40)
    for line in hangman_art[wrong_guesses]: 
        print(line) 
    print("-" * 40) 

def display_hint(hint): 
    print(" ".join(hint))

def display_answer(answer): 
    pass 

def main(): 
    answer = random.choice(words)  
    hint = ["_"] * len(answer)  
    print(hint)
    wrong_guesses = 0
    guessed_letters = set() 
    is_running = True 

    while is_running: 
        display_man(wrong_guesses) 
        display_hint(hint) 
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha(): 
            print("Invalid input. Enter a letter.")
            continue
            
        if guess in guessed_letters: 
            print(f"You have already guessed {guess}")
            continue

        guessed_letters.add(guess) 

    
        if guess in answer: 
            for index in range(len(answer)): 
                if answer[index] == guess: 
                    hint[index] = guess 
        else: 
            wrong_guesses += 1 

        if "_" not in hint: 
            display_man(wrong_guesses) 
            display_answer(answer) 
            print("YOU WIN!!!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1: 
            display_man(wrong_guesses)
            display_answer(answer) 
            print("YOU LOSE....")
            is_running = False

if __name__ == "__main__":
    main()



