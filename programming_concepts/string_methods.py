#name = input("Enter your full name: ")
phone_number = input("Enter your phone number: ")

# result = len(name) 
# result = name.find(" ")           # Find first occurrence of " "
# result = name.rfind("E")          # Find last occurrence of "E"
# name = name.capitalize()          # Capitalize first letter
# name = name.upper()               # Convert to uppercase
# name = name.lower()               # Convert to lowercase
# result = name.isdigit()           # Check if all characters are digits, boolean (T/F)
# result = name.isalpha()           # Check if all characters are alphabetic, boolean (T/F)
# result += phone_number.count(" ") # Count occurrences of " " in phone number
result = phone_number.replace(" ", "") 

print(result)


print(help(str))
