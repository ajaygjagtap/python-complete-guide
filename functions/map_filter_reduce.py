'''
map() :   TRANSFORM ELEMENTS
Applies a function to each element of an iterable.
'''

# SQUARE_NUMBERS :
nums = [4, 2, 7, 3, 9, 5]
square_nums = list(map(lambda x : x * x, nums))
print(f"squares of given {nums} are {square_nums}")


# CONVERTING STRING LIST INTO INT :
n = ["1", "2", "3"]
result = list(map(int, n))
print(result)

print("-----------------------------------------------------------------------------")

'''
filter() :   SELECT ELEMENTS
Filters elements based on a condition (True/False).
'''

# EVEN NUMBERS :
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_nums = list(filter(lambda x : x % 2 == 0, num_list))
print(f"Even numbers from given {num_list} are {even_nums}")


# STRINGS WITH LENGTH > 3 :
words = ["Hi", "Python", "API", "Hello"]
output = list(filter(lambda x : len(x) > 3, words))
print(f"Words with length > 3 from {words} are {output}")

print("-----------------------------------------------------------------------------")

'''
reduce() :   COMBINE ELEMENTS
Reduces iterable to a single value by repeatedly applying a function.
'''

# SUM OF NUMBERS :
from functools import reduce

numbers = [1, 18, 2, 3, 4, 12, 25, 5, 6, 7, 8, 9, 10]
summation = reduce(lambda a, b : a + b, numbers)
print(f"Total Sum of given {numbers} is {summation}")


# MAXIMUM VALUE :
max_value = reduce(lambda a, b : a if a > b else b, numbers)
print(f"Max value from {numbers} is {max_value}")
