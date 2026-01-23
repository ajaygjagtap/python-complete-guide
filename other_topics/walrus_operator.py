'''
Walrus Operator (:=) :
From Python 3.8 onwards.
Also known as Assignment expression.
Assigns Values to variables as part of larger expressions.
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while (num := len(numbers)) > 5:
    print(numbers.pop())

print(numbers)

print("-----------------------------------------------------------------------------")

foods = list()

print("If you wants to exit just enter quit.")
while(food := input("What food do you like? ").capitalize()) != "Quit":
    foods.append(food)

print(foods)
