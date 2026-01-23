''' 
Dictionary : 
A dictionary is an unordered collection of data containing a key:value pair.
The key:value pair enclosed with curly{} brackets.
'''

dict1 = {"name":"Ajay", "age":20, "canVote":True}
print(dict1)

print(dict1.keys())

print(dict1.values())

for key in dict1.keys():
    print(dict1[key])

    print("The value of corresponding to the key", key, "is", dict1[key])

