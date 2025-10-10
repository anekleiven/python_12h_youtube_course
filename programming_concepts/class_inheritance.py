# inheritance = Allows a class to inherit attributes and methods from another class 
# helps with code reusability and extensibility 
# class Child(Parent) 

class Animal: 
    def __init__(self, name):
        self.name = name
        self.is_alive = True 

    def eat(self):
        print(f"{self.name} is eating") 

    def sleep(self): 
        print(f"{self.name} is sleeping") 

    
class Dog(Animal): 
    def speak(self):            # child classes can have their own functions, different from other children. 
        print("Woof") 

class Cat(Animal): 
    def speak(self): 
        print("Meow") 

class Mouse(Animal):
    def speak(self): 
        print("pip") 


dog = Dog("Marco") 
cat = Cat("Sir James") 
mouse = Mouse("Mickey") 

print(dog.name) 
print(dog.is_alive) 
dog.sleep() 
mouse.eat() 
mouse.speak()

# inheritance requires less code and better readability, since code can be reused in the child classes. 