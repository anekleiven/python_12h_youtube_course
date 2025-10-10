import random 

# print("\u25cf \u250c \u2500 \u2520 \u2502 \u2514 \u2518")

# ● ┌ ─ ┠ │ └ ┘

"┌─────────┐" 
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1:     ("┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"),
    2:     ("┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"),
    3:     ("┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘"),
    4:     ("┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"),
    5:     ("┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"),     
    6:     ("┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘")
}

dice = []
total = 0 
num_of_dice = int(input("How many dice would you like to roll? "))

for die in range(num_of_dice): 
    dice.append(random.randint(1,6))

#for die in range(num_of_dice):                 # prints each die vertically
#    for line in dice_art.get(dice[die]): 
#        print(line) 

for line in range(5):                           # prints each die horizontally      
    for die in dice:                            # line = 0,1,2,3,4 
        print(dice_art.get(die)[line], end="") 
    print()

for die in dice: 
    total += die 
print(f"Your total is {total} points.") 

if total >= num_of_dice * 5: 
    print("Wow! You rolled really high!")
elif total <= num_of_dice * 2: 
    print("Oof! You rolled really low!")
else: 
    print("Not too shabby!")

print("--------------------------------")
print("Thanks for playing!")
print("Goodbye!")
print("--------------------------------")


