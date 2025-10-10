import random 
# randint = random.randint(a, b) returns a random integer N such that a <= N <= b 
random.randint(1,100) 
print(random.randint(1,100)) # Prints a random integer between 1 and 100 

num = random.randint(1,6) # Prints a random integer between 1 and 6
print(num) 

low = 1 
high = 100 
options = ("rock", "paper", "scissors") 
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

num2 = random.randint(low,high) 
print(num2)

# random = random.random() returns a random float in the range [0.0, 1.0)
num3 = random.random() # Prints a random float between 0.0 and 1.0 
print(num3)

# choice = random.choice(seq) returns a random element from the non-empty sequence seq 
option = random.choice(options) 
print(option) # Prints a random choice from the options tuple

# shuffle = random.shuffle(x) shuffles the sequence x in place 
random.shuffle(cards) 
print(cards) 

