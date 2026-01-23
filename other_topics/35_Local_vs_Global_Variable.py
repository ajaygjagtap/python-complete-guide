'''
Local Variables :
A local varibale is created inside a function and
can be used only within that function.
'''

def my_function():
    x = 10 #local variable
    print(f"{x} is a local variable")
    

my_function()

# print(x)    Error: x is not defined outside the function 

print("-----------------------------------------------------------------------------")

'''
Global variable:
A global variable is created outside all functions and
be accessed anywhere in program. 
'''
y = 20

def my_function():
    print(y)

my_function()
print(y)  # y is accessible both inside and outside the function.

print("-----------------------------------------------------------------------------")

'''
global Keyword :
To change a local variable inside a function 
you must use the global keyword 
Otherwise python treats it as a local variable 
'''

count = 0

def increase():
    global count
    count += 1

increase()
print(count)

print("-----------------------------------------------------------------------------")

'''
Local vs Global Variable with Same Name :
Python treats a variable LOCAL when it inside a function.
Python treats a variable GLOBAL when it outside a function.
'''

x = 5   # Global

def test():
    x = 10  # Local
    print(x)

test()
print(x)
