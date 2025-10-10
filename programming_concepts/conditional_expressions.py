# conditional expression = a one line shortcut for if-else statement 
# print or assign one or two values based on a condition 
# X if condition else Y 


a = 6 
b = 7 
age = 16 
temperature = 25  
user_role = "guest"

max_num = a if a > b else b 
min_num = a if a < b else b 

print(max_num)
print(min_num)

status = "Adult" if age >= 18 else "Child" 
weather = "Hot" if temperature >= 30 else "Warm" if temperature < 30 and temperature >= 20 else "Cold"
access_level = "Full access" if user_role == "admin" else "Limited access" 



print(status)
print(weather)
print(access_level)