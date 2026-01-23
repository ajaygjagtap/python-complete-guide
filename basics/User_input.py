# Basic Input function
a = input()
print("My name is", a)

print("-----------------------------------------------------------------------------")

# Input function using string
b = input("Enter your name: ")
print("Your name is", b)

print("-----------------------------------------------------------------------------")

# Input function with typecasting
x = input("Enter first number: ") 
y = input("Enter second number: ")

print(x+y) #concatination

x1 = int(x) 
y1 = int(y)
print(x1+y1)
print(int(x)+int(y))

print("-----------------------------------------------------------------------------")

# Que - Make simple calculator by taking values from user.
# Solution -

a = input("Enter first number: ")
b = input("Enter second number: ")

#Addition
print("Addition of ", a, "+", b, "=", int(a) + int(b))

# Substracton
print("Substraction of ", a, "-", b, "=", int(a) - int(b))

# Multiplication
print("Multiplication of ", a, "*", b, "=", int(a) * int(b))

# Division
print("Division of ", a, "/", b, "=", int(a) / int(b))

#Modulus
print("Modulus of ", a, "%", b, "=", int(a) % int(b))

# Exponential
print("The value of", a, "^", 2, "=", int(a) **2)
print("The value of", b, "^", 3, "=", int(b) **3)
