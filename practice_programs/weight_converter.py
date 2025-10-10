# python weight converter 

weight = float(input("Enter your weight: ")) 
unit = input("Kilograms or pounds? (K/P): ")

if unit == "K": 
    weight = weight * 2.205 
    unit = "Lbs."
    print(f"Your weight is {round(weight, 2)} {unit}")
elif unit == "P": 
    weight = weight / 2.205
    unit = "Kg."
    print(f"Your weight is {round(weight, 2)} {unit}")
else: 
    print(f"{unit} was not valid") 
