# object = a "bundle" of related attributes (variables) and methods (functions) 
# ex. phone, cup, book 
# you need a class to create many objects 

# class = blueprint used to design the structure and layour of an object 

from car import Car

car1 = Car("BMW XC90", "1997", "red", False)
car2 = Car("Audi e-tron", "2024", "silver", True) 
car3 = Car("Mercedes Benz", "2003", "blue", True)
car4 = Car("Hyundai", "2011", "blue", False)

car3.drive() 
car1.stop()
car2.describe()
car4.describe() 









