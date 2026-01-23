'''
Conditional operators : 
    < --> is less than.
    > --> is greater than.
    <= --> is less than or equal to.
    >= --> is greater than or equal to.
    == --> is equal to. 
    != --> is not equal to.
'''

# if-else codition ("Simple")
Age = int(input("Enter your age: "))
print("Your age is ", Age)

if (Age>=18):
    print("You can drive")

else:
    print("you cannot drive")

print("-----------------------------------------------------------------------------")

# if-elif-else condition ("Ladder")
Number = int(input("Enter Number: "))
if (Number<0):
    print("The number is negative")

elif (Number==0):
    print("The number is zero")

elif (Number==999):
    print("The number is special")

else:
    print("The number is positive")

print("-----------------------------------------------------------------------------")

# if-elif-if-elif-else-else condition ("Nested")
Number = int(input("Enter Number: "))
if (Number < 0):
    print("The number is negative")

elif (Number > 0):

    if (Number <= 10):
        print("The number is between 1-10")

    elif (Number > 10 and Number <= 20):
        print("The number is between 11-20")

    else:
        print("The Number is greater than 20")
else:
    print("The number is Zero")
