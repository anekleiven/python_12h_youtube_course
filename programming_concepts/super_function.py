# super() = function used in a child class to call methods from a parent class (superclass) 
# allows you to extend the functionability of the inherited methods 

class Shape:                                                                # parent class      
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled 
    
    def describe(self): 
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}") 

class Circle(Shape):                                                        # child class 
    def __init__(self, color, is_filled, radius): 
        super().__init__(color, is_filled) 
        self.radius = radius

    def describe(self):                                                     
        print(f"It is a circle with an area of {3.14 * self.radius} cm^2")  # the child's describe() function will override the parent's

class Square(Shape):                                                        # child class 
    def __init__(self, color, is_filled, width): 
        super().__init__(color, is_filled) 
        self.width = width
    
    def describe(self):
        print(f"The square has a width of {self.width} cm")                 # in this case the parent's describe() function "wins"
        super().describe()                                                  #  over the square's describe() function because of super().describe() 

class Triangle(Shape):                                                      # child class 
    def __init__(self, color, is_filled, width, height):                    # has no describe() function. The parent's describe() is called. 
        super().__init__(color, is_filled) 
        self.width = width
        self.height = height 


circle = Circle(color = "Blue", is_filled = True, radius = 5) 
square = Square(color = "red", is_filled=False, width=6) 
triangle = Triangle(color = "Yellow", is_filled= False, width=8, height=7) 

print(circle.color) 
print(circle.is_filled) 
print(f"{circle.radius} cm") 
print(f"The height of the triangle is {triangle.height} cm. The width of the triangle is {triangle.width} cm.")

circle.describe() 
square.describe() 
triangle.describe()                                                        