# break satement exits the loop.
Number = int(input("Enter the Number: "))
for i in range(1, 15):
    print(Number, "x" , i, "=", Number * i)
    if(i == 10):
        break

print("-----------------------------------------------------------------------------")

# continue statement skips the iteration.
Number = int(input("Enter Number" ))
for i in range(1, 15):
    if(i == 11):
        continue
    print(Number, "x" , i, "=", Number * i)
