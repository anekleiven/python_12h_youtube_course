# exception = an event interrupts the flow of a program 
# ZeroDivisionError, TypeError, ValueError 
# 1. try, 2. except, 3. finally 

try: 
    number = int(input("Enter a number: "))
    print(f"{1/number:.3f}")  
except ZeroDivisionError: 
    print("You can't divide by zero!") 
except ValueError: 
    print("Enter only numbers, please.") 
except Exception: 
    print("Something went wrong :( ") 
finally: 
    print("Do some clean up here :) ")

