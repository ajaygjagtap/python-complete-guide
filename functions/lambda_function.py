'''
Lambda Function :
It is a anonymous function with a single expression,
commonly used for short operations.
'''

square = lambda num : num * num
n = 5
result = square(n)
print(f"Square of {n} is {result}")

print("-----------------------------------------------------------------------------")

cube = lambda num1 : num1 * num1 * num1
d = 3
result1 = cube(d)
print(f"cube of {d} is {result1}")

print("-----------------------------------------------------------------------------")

max_num = lambda a, b : a if a > b else b
q = 7
w = 9
result2 = max_num(q,w)
print(f"{result2} is greater")
