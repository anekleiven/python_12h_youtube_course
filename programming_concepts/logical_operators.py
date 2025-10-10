# logical operators = evaluate multiple conditions (or, and, not) 
# or = at least one condition is true 
# and = all conditions must be true
# not = reverses the result, returns false if the result is true

temp = 0
is_sunny = False

if temp >= 28 and is_sunny:
    print("--------------------------------")
    print("It is HOT outside") 
    print("It is sunny") 
    print("--------------------------------")
elif temp <= 20 and is_sunny: 
    print("--------------------------------")
    print("It is cold outside") 
    print("It is sunny")
    print("--------------------------------")
elif temp < 28 and temp > 20 and is_sunny: 
    print("--------------------------------")
    print("It is warm outside") 
    print("It is sunny")
    print("--------------------------------")
elif temp >= 20 and not is_sunny: 
    print("--------------------------------")
    print("It is warm outside") 
    print("It is not sunny")
    print("--------------------------------")
elif temp <= 0 and not is_sunny: 
    print("--------------------------------")
    print("It is cold outside") 
    print("It is not sunny")
    print("--------------------------------")
