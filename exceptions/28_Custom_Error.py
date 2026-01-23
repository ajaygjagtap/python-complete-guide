num = input("Enter the number between 5-9: ").capitalize()

if num == "Quit":
    print("Quit")


elif (int(num) < 5 or int(num) > 9):
    raise ValueError("Value should be between 5-9")
