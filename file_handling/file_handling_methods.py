'''
read() Method :-
Read the entire file (or specified number of characters).
'''

with open("data.txt", "r") as file:
    content = file.read(10)     # Read first 10 characters.
    content = file.read()       # Read entire file.
    print(content)

print("-----------------------------------------------------------------------------")

'''
readline() Method :-
Reads one line at a time.
'''

with open("data.txt", "r") as file:
    content = file.readline()
    print(content)

print("-----------------------------------------------------------------------------")

'''
readlines() Method :-
Reads all lines and returns a list.
'''

with open("data.txt", "r") as file:
    content = file.readlines()
    print(content)

print("-----------------------------------------------------------------------------")

'''
write() Method :-
Writes a single string to file.
'''

with open("data.txt", "w") as file:
    content = file.write("I wants to write something.")
    print(content)

print("-----------------------------------------------------------------------------")

'''
writelines() :-
Writes a list of strings. (No newline added automatically)
'''

lines = ["Line_1\n", "Line_2\n", "Line_3"]
with open("data.txt", "w") as file:
    content = file.writelines(lines)
    print(content)

print("-----------------------------------------------------------------------------")

'''
tell() Method :-
Returns current cursor position.
'''

with open("data.txt", "r") as file:
    content = file.tell()
    print(content)

print("-----------------------------------------------------------------------------")

'''
seek() Method :-
Moves cursor to a specific position.
'''

with open("data.txt", "r") as file:
    content = file.seek(0)

"-----------------------------------------------------------------------------"

'''
flush() Method :-
Forces data to be written to disk.
'''

with open("data.txt", "w") as file:
    content = file.write("Thank You")
    content = file.flush()
    print(content)

print("-----------------------------------------------------------------------------")

'''
close() Method :-
Closes the file and free resources.
'''

file = open("data.txt", "r")
content = file.read()
print(content)
file.close()        # Avoid manual close, Use with Statement as used above
