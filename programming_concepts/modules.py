# module = a file containing code you want to include in your program 
# use 'import' to include a module (built-in or your own) 
# useful to break up a large program reusable separate files 

# built in modules 

import math # built-in module
import pandas as pd # external module (need to install first)
from math import pi, sqrt # import specific parts of a module


print(math.pi) 
print(math.sqrt(16))

print(pi) # possible because of 'from math import pi' 


print(math.pi) # better to use 'math.pi' to avoid confusion 


# create your own module 
# module saved in 'example_modules.py'

import example_modules as em 

print(em.pi) 
print(em.square(4))
print(em.cube(3))
print(em.average(10, 20))

