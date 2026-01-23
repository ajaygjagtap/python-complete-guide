'''
A module is simply a Python file (.py) containing functions, classes, or variables.
When you use import, you load that module into your program.
'''

# Basic import
import math
print(math.sqrt(16))

print("-----------------------------------------------------------------------------")

# Import specific function
from math import sqrt
print(sqrt(25))

print("-----------------------------------------------------------------------------")

# Import with alias
import numpy as np 
print(np.array([1, 2, 3]))

print("-----------------------------------------------------------------------------")

# Installing External Module
''' pip install numpy '''