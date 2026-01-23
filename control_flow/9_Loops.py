# for loop for String.
name = "Ajju"
for i in name:
    print(i)

print("-----------------------------------------------------------------------------")

# for loop for List.
Brothers = ["Rushi", "Aniket", "Ajju", "Avi", "Apurv", "Shubham"]
for x in Brothers:
    print(x)
    for y in x:
        print(y)

print("-----------------------------------------------------------------------------")

# range() Method.
for a in range(50):
    print(a + 1)

for b in range(1, 10):  # 1 is "start" argument and 10 is "stop" argument.
    print(b)

for c in range(1, 10, 4): # 1 is "start" argument, 10 is "stop" argument and 4 is "step" argument.
    print(c)

print("-----------------------------------------------------------------------------")

# WHILE LOOP
q = 0
while(q <= 50):
    print(q)
    q = q + 1

print("-----------------------------------------------------------------------------")

# DO WHILE LOOP
i = 0
while True:
    print(i)
    i = (i + 1)
    if(i % 100 == 0):
        break



d = int(input("Enter number: "))
print(d)
while(d <= 10):
    d = int(input("Enter number: "))
    print(d)

