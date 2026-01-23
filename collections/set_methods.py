# union() method is used to make union of two sets.
set1 = {1, 2, 5, 6}
set2 = {3, 6, 7, 2, 5, 9}
print(set1.union(set2))

print("-----------------------------------------------------------------------------")

# update() method is used to update the set.
set3 = {1, 2, 5, 6}
set4 = {3, 6, 7, 2, 5, 9}
set3.update(set4)
print(set3, set4)

print("-----------------------------------------------------------------------------")

# intersection() method is used to print the same values in both set.
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7, 2, 5, 9}
s3 = s1.intersection(s2)
print(s3)

print("-----------------------------------------------------------------------------")

# intersection_update() method is used to print the same values in both set.
s4 = {1, 2, 5, 6}
s5 = {3, 6, 7, 2, 5, 9}
s4.intersection_update(s5)
print(s4, s5)

print("-----------------------------------------------------------------------------")

# difference() method is used to print values that are only presents in original set and not in both the sets.
st1 = {1, 2, 5, 6}
st2 = {3, 6, 7, 2, 5, 9}
st3 = st1.difference(st2)
print(st3)

print("-----------------------------------------------------------------------------")

# difference_update() method is used to print values that are only presents in original set and not in both the sets.
st4 = {1, 2, 5, 6}
st5 = {3, 6, 7, 2, 5, 9}
st4.difference_update(st5)
print(st4)

print("-----------------------------------------------------------------------------")

# add() method
cities = {"Sangola", "Pandharpur", "Mangalwedha", "Madha", "Karmala"}
cities.add("Malshiras")
print(cities)

print("-----------------------------------------------------------------------------")

# update() method
cities2 = {"Mohol", "South Solapur", "North Solapur", "Barshi", "Akkalkot"}
cities.update(cities2)
print(cities)

print("-----------------------------------------------------------------------------")

# remove() / discard() method
cities2.remove("South Solapur")
cities2.discard("North Solapur")
print(cities2)

print("-----------------------------------------------------------------------------")

# pop() method : 1 random value will be removed.
item = cities.pop()
print(cities)
print(item)

print("-----------------------------------------------------------------------------")

# del is not method , rather it is a keyword which delets the entire set. NameError: name 'cities' is not defined.
del cities
# print(cities)

print("-----------------------------------------------------------------------------")

# clear() method clears all the values in the set and prints an empty set.
cities2.clear()
print(cities2)
