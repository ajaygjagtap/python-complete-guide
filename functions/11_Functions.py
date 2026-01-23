'''
# A function is a block of code that performs a specific task whwnever it is called.
Types - 1. Built-in function
        2. User-defined function

1. Built-in function
    The functions already defined in python is known as built-in function.
    Like min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

 2. User-defined function
    The functions created or defined by user to do specific task as per our need is known as user-defined function.
'''

# Printing Greater number.
def is_Greater(a, b):
    if (a>b):
        print("First Number is greater\n")
    elif(a==b):
        print("Number is Same")
    else:
        print("Second Number is greater\n")

def is_Lesser(a,b):
    pass

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
is_Greater(a, b)

c = int(input("Enter First Number: "))
d = int(input("Enter Second Number: "))
is_Greater(c, d)