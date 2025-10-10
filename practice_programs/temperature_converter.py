# temperature converter 

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ") 
temp = float(input("Enter the temperature: ")) 

if unit == "C": 
    temp = temp * 9/5 + 32
    print(f"The temperature is {round(temp, 1)} F")
elif unit == "F": 
    temp = (temp - 32) * 5/9
    print(f"The temperature is {round(temp, 1)} C")
else: 
    print(f"{unit} is not a valid temperature unit")

