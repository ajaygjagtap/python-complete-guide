list1 = [1, 2.3, [-4, 5], ["Apple", "Banana"], True, "Red", -2, 0, 3.6]

for index, item in enumerate(list1):
    print(index,":", item)

print("------------------------------------------------------------")

# Changing start index (by passing it an argument).
list_1 = [1, 2.3, [-4, 5], ["Apple", "Banana"], True, "Red", -2, 0, 3.6]

for index, item in enumerate(list_1, start = 1):
    print(index,":", item)
