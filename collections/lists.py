'''
List : 
A list is an ordered collection of data with elements seperated by a comma(,) and enclosed within square [] brackets.
List are "Mutable" and can be modified after creation (List is Changable).
'''

list1 = [1, 2.3, [-4, 5], ["Apple", "Banana"], True, "Red", -2, 0, 3.6]
print(list1)

if 1 in list1:
    print("Yes, it present in the list.")
else:
    print("No, it not present in the list.")

if "App" in "Apple":
    print("Yes, it present in the word Apple.")
else:
    print("No, it not present in the word Apple.")

print(list1[0:6:2]) #(list_name[ start : end : jump index]) jump index - same as step Argument in range() function.
