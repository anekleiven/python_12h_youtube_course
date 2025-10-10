# validate user input exercise 
# 1- username is no more than 12 characters 
# 2- username must not contain spaces 
# 3- username must not contain digits 

username = input("Enter your username: ") 

username.find(" ")
username.isalpha() 


if len(username) > 12:
    print("Username can't be more than 12 characters.")
elif not username.find(" ") == -1 or username.isalpha() == False:
    print("Username can't contain any spaces or digits. Try again.") 
else: 
    print(f"Welcome, {username}") 
