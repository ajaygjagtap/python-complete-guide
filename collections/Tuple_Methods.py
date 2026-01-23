'''
Tuple :
A Tuple is an ordered collection of data with elements seperated by a comma(,) and enclosed within round() brackets.
Tuple are "Immutable" and cannot be modified after creation (Tuple is Unchangable).
'''

tuple1 = (1, 9, -3, 5, 2, 7, "Orange", -6, -1)
print(tuple1)


# count() method returns the count of the number (how many times it comes in the tuple).
print("The count is:",tuple1.count(1))

print("-----------------------------------------------------------------------------")

# index() method returns the index of the first occurence of the tuple.
print("The first occurence of 7 ia at index:",tuple1.index(7))

print("-----------------------------------------------------------------------------")

# len() method is used to calculate the length of the tuple.
print("The length of the tuple is:", len(tuple1))
