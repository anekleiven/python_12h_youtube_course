# multiple inheritance = inherit from more than one parent class 
# C(A,B) 

# multilevel inheritance = inherit from a parent which inherits from another parent 
# C(B) <- B(A) <- A 

class Animal:                               # grand parent class

    def __init__(self, name): 
        self.name = name 

    def eat(self): 
        print(f"{self.name} is eating")  
    
    def sleep(self):
        print(f"{self.name} is sleeping") 



class Prey(Animal):                         # parent class 
    def flee(self): 
        print(f"{self.name} is fleeing") 
    


class Preditor(Animal):                     # parent class 
    def hunt(self): 
        print(f"{self.name} is hunting") 
    


class Rabbit(Prey):                         # child class 
    pass


class Hawk(Preditor):                       # child class 
    pass 


class Fish(Prey, Preditor):                 # child class 
    pass 


rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo") 

rabbit.flee()                               # Rabbit inherits from Prey
hawk.hunt()                                 # Hawk inherits from Preditor 
fish.hunt()                                 # Fish can inherit from both parent classes 
fish.flee() 

fish.eat()              

# all the child classes can use the name attribute from the grandparents, since the parents are linked to the animal class 
# this is called multi level inheritance 


