try:
    num = int(input("Enter the index: "))
    a = [6, 3, 4, 8, 1, 7, 5, 2]
    print(a[num])


except IndexError:
    print("Index error occured")
