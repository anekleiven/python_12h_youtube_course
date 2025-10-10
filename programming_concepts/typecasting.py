# typecasting 
# the process of converting a variable from one type to another 

name = "John" 
age = 25
gpa = 3.5
is_student = True 

print(type(name))       # str
print(type(age))        # int
print(type(gpa))        # float
print(type(is_student)) # bool

pga = int(gpa)          # float to int
print(type(pga))        # int
print(pga)              # 3

age = float(age) 
print(age)

age = str(age) 
print(type(age))        # str
print(age)              # "25.0"

name = bool(name) 
print(name)              # True
