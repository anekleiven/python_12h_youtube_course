# class variable = shared among all instances of class 
# defined outside the constructor 
# allow you to share data among all objects created from that class 

class Student: 

    class_year = 2024       # this is a class variable
    num_students = 0  


    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
        Student.num_students += 1 

student1 = Student("Amy", 19) 
student2 = Student("Lara", 18) 
student3 = Student("Kerry", 21) 
student4 = Student("Mikkel", 23) 

print(student1.name)         # access the name of student1 
print(student1.age)          # access the age of student 1 

print(student1.class_year)   # common for all students 
print(Student.class_year)    # good practice to access class variables by the class name (not class objects)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students:") 
print(student1.name) 
print(student2.name) 
print(student3.name) 
print(student4.name) 