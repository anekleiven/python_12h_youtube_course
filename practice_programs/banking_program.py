# Python Banking Program 
# Program to show balance, deposit money and withdraw money. 

# Section 1: Show balance 

def show_balance(balance): 
    print("-" * 60) 
    print(f"Your balance is ${balance:.2f}") 
    print("-" * 60) 

# Section 2: Deposit money 

def deposit(): 
    print("-" * 60) 
    amount = float(input("Enter an amount to be deposited: ")) 
    print("-" * 60) 

    if amount < 0: 
        print("-" * 60) 
        print("That's not a valid amount")
        print("-" * 60) 
        return 0 
    else: 
        return amount 

# Section 3: Withdraw money 

def withdraw(balance): 
    print("-" * 60) 
    amount = float(input(f"Enter an amount to be withdrawn: "))
    print("-" * 60) 

    if amount > balance: 
        print("-" * 60) 
        print("Insufficient funds...") 
        print("-" * 60) 
        return 0 
    elif amount < 0:
        print("-" * 60) 
        print("Thats not a valid amount") 
        print("-" * 60) 
        return 0
    else:
        return amount 

# Section 4: Main function 

def main(): 
    balance = 0 
    is_running = True 

    while is_running: 
        print("-" * 60) 
        print("     Welcome to my banking Program   ") 
        print("-" * 60) 
        print("     1. Show Balance                 ") 
        print("     2. Deposit                      ") 
        print("     3. Withdraw money               ") 
        print("     4. Exit                         ") 
        print("-" * 60) 

        choice = input("Enter your choice (1-4): ") 

        if choice == '1': 
            show_balance(balance) 
        elif choice == '2': 
            balance += deposit() 
        elif choice == '3': 
            balance -= withdraw(balance)
        elif choice == '4': 
            is_running = False 
        else: 
            print("Invalid input. Please enter a number between 1 and 4") 

    print("-" * 60) 
    print("Thank you for using my banking program.") 
    print("Have a great day!") 
    print("-" * 60)


if __name__ == "__main__": 
    main() 


