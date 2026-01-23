'''
== (Equality Operator) :
Checks value equality.
Compares contents/data.

is (Identity Operator) :
Checks object identity.
Compares memory location.
'''
a = 10
b = 10
print(a == b)
print(a is b)

print("-----------------------------------------------------------------------------")

c = [1, 3, 5]
d = [1, 3, 5]
print(c == d)
print(c is d)


# Differnce :
# '==' checks value equality, while 'is' checks whether both variables point to the same object in memory.