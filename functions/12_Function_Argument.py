'''
There are 4 types of arguments that we can provide in a function.
1. Default Argument.
2. Keyword Argument.
3. Variable length Argument.
4. Required Argument.
'''

"-----------------------------------------------------------------------------"

# Default Argument.
def Average(a=9, b=18):
    print("The Average is: ", (a+b)/2)
Average()

name = str(input("Enter First Name: "))
def Name(first_name, last_name="Jagtap"):
    print("Hello,", first_name, last_name)
Name(name)

print("-----------------------------------------------------------------------------")

# Required Argument.
def Average(c, d):
    print("The Average is: ", (c+d)/2)
Average(25, 18)

print("-----------------------------------------------------------------------------")

# Keyword Argument. order does not matter
def Average(c, d):
    print("The Average is: ", (c+d/2))
Average(d=20, c=10)

print("-----------------------------------------------------------------------------")

# Variable length Argument
def Average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("The Average is: ", sum/len(numbers))
Average(2, 6, 8, 4, 5, 5)
