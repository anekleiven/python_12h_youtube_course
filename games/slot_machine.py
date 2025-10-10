# Python slot machine 

import random 

def spin_row(): 
    symbols = ["🍉","🍋","🍒","🔔","⭐"]

    return [random.choice(symbols) for symbol in range(3)]

def print_row(row): 
    print("-" * 40)
    print(" | ".join(row)) 
    print("-" * 40) 

def get_payout(row, bet): 
    if row[0] == row[1] == row[2]: 
        if row[0] == "🍒": 
            return bet * 3 
        elif row[0] == "🍉": 
            return bet * 4 
        elif row[0] == "🍋": 
            return bet * 5 
        elif row[0] == "🔔": 
            return bet * 10 
        elif row[0] == "⭐": 
            return bet * 50 
    return 0 

def main(): 
    balance = 100 

    print("-" * 40) 
    print("Welcome to my slot machine") 
    print("Symbols:🍉 🍋 🍒 🔔 ⭐")
    print("-" * 40) 

    while balance > 0: 
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount: ") 

        if not bet.isdigit():
            print("Invalid input. Please input a valid number") 
            continue
        
        bet = int(bet) 

        if bet > balance: 
            print("Insufficient funds") 
            continue 

        if bet <= 0: 
            print("Bet must be greater than 0") 
            continue 

        balance -= bet 

        row = spin_row()
        print("Spinning...\n")
        print_row(row) 
        
        payout = get_payout(row,bet) 

        if payout > 0: 
            print(f"You won ${payout}") 
        else: 
            print("Sorry, you lost....")
        
        balance += payout

        play_again = input("Do you want to take another spin? (y/n): ").upper() 

        if play_again != "Y": 
            break 
    
    print("-" * 40) 
    print(f"Game over! Your final balance is ${balance}") 
    print("-" * 40) 

if __name__ == "__main__": 
    main() 

