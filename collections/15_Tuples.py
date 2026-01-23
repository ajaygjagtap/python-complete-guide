'''
Tuple : 
A Tuple is an ordered collection of data with elements seperated by a comma(,) and enclosed within round() brackets.
Tuple are "Immutable" and cannot be modified after creation (Tuple is Unchangable).
'''

tuple1 = (("Eagle","Parrot"), "Apple", "Banana", 18, -3, False)
print(tuple1)

if 18 in tuple1:
    print("Yes, it present in the tuple.")
else:
    print("No, it not present in the tuple.")

if "App" in "Apple":
    print("Yes, it present in the word Apple.")
else:
    print("No, it not present in the word Apple.")

print(tuple1[0:6:2]) #(tuple_name[ start : end : jump index]) jump index - same as step Argument in range() function.
