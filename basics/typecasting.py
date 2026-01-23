'''
Typecasting :
The conversion of one data type to other data type is known as Typecasting or Typeconversion.
python supports variety of functions or methods like int(), float(), str(), ord(), hex(), oct(), tuple(), 
set(), list(), dict(), etc for type casting or type conversion in python.

Types of Typecasting - 

1. Implicit Typecasting
Ordering of data types is not same in python. Some of the data types have the higher-order and some 
have lower order. While performing any operation on variables with different data types one of the 
variable's data type will be changed to the higher data type. According to the level, one data type is 
converted into other by Python interpreter itself(automatically). This is known as Implicit Typecasting.

2. Explicit Typecasting
The conversion of one data type into another data type done by programmer or manually as per requirement 
is known as Explicit Typecasting.
'''

# Implicit typecasting
a = 7
b = 2.0
c = a + b
print(c)
print(type(a))
print(type(b))
print(type(c))

print("-----------------------------------------------------------------------------")

# Explicit Typecasting
string = "7"
number = 2
string_number = int(string)
sum = number + string_number
print("The Sum of both numbers is", sum)
