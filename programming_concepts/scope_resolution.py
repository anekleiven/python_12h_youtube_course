# variable scope = where a variable is accessible and visible 
# scope resolution = the order in which Python looks for a variable (LEGB rule) -> Local, Encloded, Global, Built-in 

def func1(): 
    a = 1           # a is local to func1, and cannot be accessed outside of func1 
    print(a) 

def func2(): 
    b = 2           # b is local to func2, and cannot be accessed outside of func2
    print(b)

func1()
func2()

# Encloded scope = function inside a function 

def outer_func():
    x = "local"     # x is local to outer_func 

    def inner_func(): 
        y = "enclosed"   # y is local to inner_func 
        print(x)        # x can be accessed inside inner_func because of encloded scope 
        print(y) 

    inner_func() 
    print(x) 
    # print(y)       # y cannot be accessed here because it is local to inner_func

outer_func() 

# Global scope = variable created outside of a function, and can be accessed anywhere in the file 

c = "global"        # c is global and can be accessed anywhere in the file 

print(c) 

# Built-in scope = names that are pre-defined in Python 

from math import e 

def func3():
    print(e) 

e = 3 

print(e)   # prints 3, because local scope has the highest priority 

