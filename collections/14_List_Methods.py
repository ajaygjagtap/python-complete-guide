'''
List : 
A list is an ordered collection of data with elements seperated by a comma(,) and enclosed within square [] brackets.
List are "Mutable" and can be modified after creation (List is Changable).
'''

list1 = [1, 3, 2, 5, 7, 25, 8, 4, 6, 11, 25 ]
print(list1)


# len() method is used to calculate the length of the list.
print("The length of the list is:", len(list1))

print("-----------------------------------------------------------------------------")

# extend() method is just extends the list which we wants to extend.
list3 = [98, 76, 54, 32, 10]
list1.extend(list3)
print(list1)

print("-----------------------------------------------------------------------------")

# copy() method is used to copy a list in another list.
list2 = list1.copy()
list2[1] = 9
print(list2)

print("-----------------------------------------------------------------------------")

# append() method append the element at the end of the list.
list1.append(9)
print(list1)

print("-----------------------------------------------------------------------------")

# insert() method is used to insert an element in a list at particular index without replacing with number present at that index.
list1.insert(6, 18)
print(list1)

print("-----------------------------------------------------------------------------")

# index() method returns the index of the first occurence of the list.
print("The element at index 7 is:",list1.index(7))

print("-----------------------------------------------------------------------------")

# reverse() method just reverse the list and print it.
list1.reverse()
print(list1)

print("-----------------------------------------------------------------------------")

# sort() method sort the element in the list and prints in ascending order.
list1.sort()
print(list1)

print("-----------------------------------------------------------------------------")

list1.sort(reverse = True)  #The elements in the list prints in descending order.
print(list1)

print("-----------------------------------------------------------------------------")

# count() method returns the count of the number (how many times it comes in the list).
print("The count is:",list1.count(25))