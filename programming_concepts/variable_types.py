# variables 

# strings
first_name = "Ane" 
food = "pizza"
email = "ane.kleiven@live.no" 

print(f"Hello, {first_name}!") 
print(f"You like {food}") 
print(f"Your email is {email}")

# integers 
age = 25 
height = 170  # in cm
weight = 65   # in kg
quantity = 3 

print(f"You are {age} years old")
print(f"Your height is {height} cm")
print(f"Your weight is {weight} kg")    
print(f"You want to order {quantity} {food}(s)")

# float 
price = 10.99 
distance = 5.5  # in km

print(f"The price is ${price}")
print(f"You ran {distance} km today") 

# boolean 
is_student = True 
is_employed = False
is_online = False 

print(f"Are you a student? {is_student}")
print(f"Are you employed?  {is_employed}")

if is_student: 
    print("You are a student.")
else:
    print("You are not a student.")

if is_employed:
    print("You are employed.")
else:
    print("You are not employed.")  

if is_online:
    print("You are online.")
else:
    print("You are offline.")