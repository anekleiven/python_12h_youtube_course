# shopping cart program 
# practise lists, sets and tuples 

foods = []
prices = []
total = 0 

while True: 
    food = input("Enter a food item to buy (q to quit): ") 
    if food.lower() == "q":
        break
    else: 
        price = float(input(f"Enter the price of a {food}: $")) 
        foods.append(food) 
        prices.append(price) 


print("----- YOUR SHOPPING CART -----") 

for food in foods: 
    print(food, end =" ") 

for price in prices: 
    total += price 

print() 
print(f"Your total is: ${total:.2f}")
