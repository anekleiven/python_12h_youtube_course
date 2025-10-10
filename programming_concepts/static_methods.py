# static methods = a method that belong to a class rather than any object for that class (instance) 
# usually used for generally utility functions 

# instance methods = best for operations on instances of the class (objects) 
# static methods = best for utility functions that do not need access to class data 


class Employee: 
    def __init__(self, name, position):
        self.name = name
        self.position = position 
    
    # instance method
    def get_info(self):                  
        return f"{self.name} = {self.position}" 
    
    @staticmethod 
    def is_valid_position(position): 
        valid_positions = ["Manager", "Cashier", "Cook", "Receptionist"] 
        return position in valid_positions 
    
employee1 = Employee("Eugene", "Manager") 
employee2 = Employee("Finn", "Cook") 
employee3 = Employee("Lars", "Receptionist") 

print(Employee.is_valid_position("Manager")) 
print(employee2.get_info()) 


# instance method = call objects within the class - the method belongs to a object
# static methods = only call the class - the method belongs to the class 



