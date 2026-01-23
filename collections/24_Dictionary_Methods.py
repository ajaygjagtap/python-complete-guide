dict1 = {"name":"Ajay", "age":20, "canVote":True}

dict2 = {"villege":"Manjari", "constituency":"Sangola"}


# update() method used to update the dictionary.
dict1.update(dict2)
print(dict1)

print("-----------------------------------------------------------------------------")

# clear() method clears all the values in the dictionary and prints an empty dictionary.
dict2.clear()
print(dict2)

print("-----------------------------------------------------------------------------")

# pop() method - selected key value will be removed.
item = dict1.pop("villege")
print(dict1)
print(item)

print("-----------------------------------------------------------------------------")

# popitem() method - last key value in the dictionary will be removed.
dict1.popitem()
print(dict1)

print("-----------------------------------------------------------------------------")

# del is not method , rather it is a keyword which delets the entire dictionary. NameError: name 'dict1' is not defined.
del dict1
# print(dict1)