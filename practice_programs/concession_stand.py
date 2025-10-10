# Concession stand program 

menu = {"pizza": 3.00,
        "hot dog": 2.50,
        "soda": 1.50,
        "popcorn": 2.00,
        "candy": 1.00,
        "water": 1.00,
        "nachos": 2.50
        }

cart = [] 
total = 0 
print("----- WELCOME TO THE CONCESSION STAND -----")
print("Here is the menu:")
for key, value in menu.items(): 
    print(f"{key}: ${value:.2f}") 
print("-------------------------------------------")


while True: 
    item = input("Enter an item to add to your cart (or 'q' to quit): ").lower() 
    if item == "q": 
        break 
    elif menu.get(item) is not None: 
        cart.append(item) 
        print(f"{item} has been added to your cart.")


print("----- YOUR CART -----")
for item in cart: 
    total += menu.get(item) 
    print(item, end = "\n") 


print("---------------------") 
print(f"Your total is: ${total:.2f}")
print("Thank you for shopping with us!")


