# format specifiers = {value:flags} format a value based on what flags are inserted 

price1 = 3.14
price2 = -49.99
price3 = 12.34

print(f"Price1: ${price1:.3f}") # f = floating point number 
print(f"Price2: ${price2:10}") # each number takes up 10 spaces 
print(f"Price3: ${price3:010}") # each number takes up 10 spaces, 0 = fill in with zeros
print(f"Price1: ${price1:<10}") # < = left align
print(f"Price2: ${price2:>10}") # > = right align
print(f"Price3: ${price3:^10}") # ^ = center align
print(f"Price1: ${price1:+}") # displays a plus sign in front of the value 
print(f"Price2: ${price2:-}") # displays a minus sign in front of the value
