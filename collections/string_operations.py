# Calculating length of string using len() function.
Names = "Ajju, Rushi"
print(len(Names))

print("-----------------------------------------------------------------------------")

fruit = "Banana"
print("The length of word Banana is", len(fruit))
for character in fruit:
    print(character)

print("-----------------------------------------------------------------------------")

name = "!!!!!Ajju!!!!!"
# For Uppercase upper() method used.
print(name.upper())

print("-----------------------------------------------------------------------------")

# For Lowercase lower() method used.
print(name.lower())

print("-----------------------------------------------------------------------------")

# Removing trailing character in right side of the string is done by rstrip() method.
print(name.rstrip("!"))

print("-----------------------------------------------------------------------------")

# Removing trailing character in left side of the string is done by lstrip() method.
print(name.lstrip("!"))

print("-----------------------------------------------------------------------------")

# Removing trailing character from bothe side of the string is done by strip() method.
print(name.strip("!"))

print("-----------------------------------------------------------------------------")

# Replace a string with another we can use replace() method.
print(name.replace("Ajju", "Rushi"))

print("-----------------------------------------------------------------------------")

# split() method is used to convert a string into a list.
print(name.split()) 

print("-----------------------------------------------------------------------------")

# capitalize() method only turns the first character of the string to uppercase and rest other turns into lowercase.
blog_heading = "introduction tO PythoN"
print(blog_heading.capitalize())

print("-----------------------------------------------------------------------------")

# center() method aligns the string to the center as per parameter given by user.
print(name.center(50))

print("-----------------------------------------------------------------------------")

# count() method returns the number of times the given value has occured within a string
c = "Rushi, Aniket, Ajju, Avi, Apurv, Shubham"
print(c.count("A"))

print("-----------------------------------------------------------------------------")

# endswith() method checks if the string ends with given value. If yes then returns True else returns False.
stmt = "Welcome to the Console."
print(stmt.endswith("."))

print("-----------------------------------------------------------------------------")

# find() method search for the first occurence of given value and return the index of it. If given value is absent thrn it returns -1.
print(stmt.find("t"))
print(stmt.find("a"))

print("-----------------------------------------------------------------------------")

# isalnum() method returns the True only if entire string only consist of A-Z, a-z, 0-9. If any other presents there then it returns False.
stmt = "WelcometotheConsole1"
print(stmt.isalnum())

print("-----------------------------------------------------------------------------")

# isalpha() method returns the True only if entire string only consist of A-Z, a-z. If any other presents there then it returns False.
stmt = "WelcometotheConsole"
print(stmt.isalpha())

print("-----------------------------------------------------------------------------")

# islower() method returns the True only if characters of the entire string is in lowercase otherwise it returns False.
stmt = "welcome to the console."
print(stmt.islower())

print("-----------------------------------------------------------------------------")

# isupper() method returns the True only if characters of the entire string is in uppercase otherwise it returns False.
stmt = "WELCOME TO THE CONSOLE."
print(stmt.isupper())

print("-----------------------------------------------------------------------------")

# swapcase() method used to convert uppercase to lowercase and lowercase to uppercase.
a = "ajju"
r = "RUSHI"
print(a.swapcase(), r.swapcase())
