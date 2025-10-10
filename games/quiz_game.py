# Python quiz game 
# Questions and options are store in tuples = fixed, unchangeable collections 
# Guesses are stored in a list = changeable collection 

# Questions 

questions = ("How many elements are in the periodic table?", 
            "What is the capital of Norway?",
            "What is the largest planet in our solar system?",
            "Who wrote 'Romeo and Juliet'?", 
            "What is the smallest prime number?", 
            "What is the capital of France?"
            )
# Options

options = (("A. 116", "B. 118", "C. 120", "D. 122"), 
           ("A. Oslo", "B. Stockholm", "C. Copenhagen", "D. Helsinki"), 
           ("A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"), 
           ("A. Shakespeare", "B. Dickens", "C. Austen", "D. Hemingway"),
           ("A. 0", "B. 1", "C. 2", "D. 3"), 
           ("A. Nice", "B. Madrid", "C. Paris", "D. Rome")
           )


answers = ("B", "A", "C", "A", "C", "C") 
guesses = []
score = 0 
question_num = 0 

# Iterate through questions and options

for question in questions: 
    print("-------------------------") 
    print(question)
    for option in options[question_num]: 
        print(option)

    guess = input("Enter (A, B, C, or D): ").upper() 
    guesses.append(guess) 
    if guess == answers[question_num]: 
        score += 1 
        print("CORRECT!")
    else: 
        print("WRONG!")
        print(f"The correct answer was: {answers[question_num]}")
    question_num += 1

# Display results depending on score 

print("-------------------------")
print("RESULTS")
print("-------------------------")
print("Answers: ", end = "")
for answer in answers:
    print(answer, end = " ")
print() 

print("Guesses: ", end = "")
for guess in guesses: 
    print(guess, end = " ")
print()

score_percent = int(score / len(questions) * 100)
print(f"Your score is: {score_percent}%")
if score_percent >= 80: 
    print("You passed!")
elif score_percent == 100: 
    print("Congratulations, you got a perfect score!")
else: 
    print("You failed. Better luck next time!")

