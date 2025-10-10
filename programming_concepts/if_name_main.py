# This code demonstrates the use of the if __name__ == "__main__": construct 
# if __name__ == "__main__": this script can be imported OR run standalone 
# Functions and classes in this module can be reused without the main block of code executing 

# Good practice to put main code inside a function called main() 
#   Code is modular 
#   Helps readability 
#   Leaves no gloabal variables 
#   Avoids unintentional execution when imported

def favorite_food(food): 
    print(f"My favorite food is {food}")

def main (): 
    # anything thats not a function or class definition goes here 
    favorite_food("Pizza")
    print("This script is being run directly")


if __name__ == "__main__": 
    main()

# The function main() will only be called if this script is run directly 
# The main function is called since the script is being run directly 
# When importing a module containing main(), the code inside main() will not execute automatically  
# You wanna borrow the favorite_food function in another script without running the main() function 


