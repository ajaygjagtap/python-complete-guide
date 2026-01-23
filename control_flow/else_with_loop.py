for i in range(5):
    print("iteration no. {} in for loop".format(i+1))
else:
    print("else block in loop")
print("out of loop")

print("-----------------------------------------------------------------------------")

for x in range(6):
    print(x)
    if x == 4:
        break
else:
    print("Sorry there is no x")

print("-----------------------------------------------------------------------------")

a = 0
while a < 8:
    print(a)
    a = a + 1
    if a == 7:
        break
else:
    print("Sorry there is no a")
    
