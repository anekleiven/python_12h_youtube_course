# polymorphism = greek word that means "to have many forms"
# TWO WAYS:
#   1. Inheritance 
#   2. Duck typing = object must have necessary attributes/methods 

from abc import ABC, abstractmethod


class Shape(ABC): 

    @abstractmethod
    def area(self):
        pass
        

class Circle(Shape): 
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2 
     

class Square(Shape):
    def __init__(self, side):
        self.side = side 
    
    def area(self):
        return self.side ** 2 
     

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base 
        self.height = height 

    def area(self):
        return self.base * self.height * 0.5 
 

circle = Circle(4)           # circle is both a circle and a shape 

class Pizza(Circle): 
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping 
        

shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("Pepperoni", 15)] 

for shape in shapes:
    print(f"{shape.area()}cm^2") 

# all shapes have their own area method 
# pizza is also a shape (Circle), and therefore inherits the circles area method 
# this inheritance is polymorphism. 
# Pizza is a pizza, a circle and a shape = many forms
