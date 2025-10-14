# property = decorator used to define a method as a property 
# it can be accessed like an attribute 
# benefit: add additional logic when read, write or delete attributes 
# gives you getter (read), setter (write) and deleter method 

class Rectangle: 
    def __init__(self, width, height): 
        self._width = width
        self._height = height 

    @property
    def width(self): 
        return f"{self._width:.2f} cm" 
    
    @property
    def height(self):
        return f"{self._height:.2f} cm" 

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else: 
            print("Width must be greater than zero")
    
    @height.setter 
    def height(self, new_height):
        if new_height > 0: 
            self._height = new_height 
        else: 
            print("Height must be greater than zero") 

    @width.deleter 
    def width(self): 
        del self._width
        print("Width has been deleted") 

    @height.deleter
    def height(self): 
        del self._height 
        print("Height has been deleted") 
        

rectangle = Rectangle(3,4) 

rectangle.width = 5
rectangle.height = 6

del rectangle.width               # calls the width deleter 
del rectangle.height              # calls the height deleter

# print(rectangle.width)          # calls the width setter
# print(rectangle.height)         # calls the height setter 


