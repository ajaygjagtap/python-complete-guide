#Printing Single Value.
print("Hello World")

print("-----------------------------------------------------------------------------")

#Printing Single Value. 
print(9)

print("-----------------------------------------------------------------------------")

#Printing Multiple Value is possible using comma.
print("Hello World", 9, 18, 27)

print("-----------------------------------------------------------------------------")

'''
(ctrl+/) used for multiple line comment
Hello this is day 1 of learning python.
we learn about print statement.
we learn about variables and data types too.
'''

#Printing with escape sequence.
# \n used for new line and \"something\" used for printing double quote into print statement.
print("Hello I'm Ajay Jagtap \nand I'm a \"good boy\".")

print("-----------------------------------------------------------------------------")


''' 
Variables :
Variable is like a container that holds the data.

Data Types :
Data types specifies the type of value a variable holds.

In pyhton we can print type of any operator using type function
'''

"-----------------------------------------------------------------------------"

# python Built in Data types 
'''
1. Numeric Data --> int, float, complex
'''
# int : 1, 0, -2
# float : 7.349, -3.479
# complex : 6+3i


# Integer
a = 1 
print("The type of a is ", type(a))

# Float
d = 9.9
print("The type of d is ", type(d))

# Complex
comp = complex(6, 3)
print(comp, "The type of comp is", type(comp))

print("-----------------------------------------------------------------------------")

'''
2. Text Data
'''
# str - "Hello World"

# String
c = "Hello World"
print("The type of c is ", type(c))

print("-----------------------------------------------------------------------------")

'''
3. Boolean Data :
Boolean data consist of values True or False
'''

# Boolean
b = True  
print("The type of b is ", type(b))

print("-----------------------------------------------------------------------------")

'''
4. Sequenced Data

List :  
A list is an ordered collection of data with elements seperated by a comma(,) and enclosed within square[] brackets.
List are "Mutable" and can be modified after creation (List is Changable).


Tuple : 
A Tuple is an ordered collection of data with elements seperated by a comma(,) and enclosed within round() brackets.
Tuple are "Immutable" and cannot be modified after creation (Tuple is Unchangable).
'''

list1 = [1, 2.3, [-4, 5], ["Apple", "Banana"]]
print(list1)


tuple1 = (("Eagle","Parrot"), ("Apple", "Banana"))
print(tuple1)

print("-----------------------------------------------------------------------------")

'''
5. Mapped Data

Dictionary : 
A dictionary is an unordered collection of data containing a key:value pair.
The key:value pair enclosed with curly{} brackets.
'''

dict1 = {"name":"Ajay", "age":20, "canVote":True}
print(dict1)
