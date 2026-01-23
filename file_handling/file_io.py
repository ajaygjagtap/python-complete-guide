'''
Opening a file :
Python provides the open() function to open a file.
It should take arguments, Name of file and Mode.
'''

f = open("Sample.txt", "r")
print(f)    # <_io.TextIOWrapper name='Sample.txt' mode='r' encoding='cp1252'>

print("-----------------------------------------------------------------------------")

'''
Modes in file :
"r" ---> This mode opens the file for reading only & gives an error if file does not exists. This is default mode.
"w" ---> This mode opens the file for writing only & creates a new file if file does not exists.
"a" ---> This mode opens the file for appending only & creates a new file if file does not exists.
"c" ---> This mode creates a file & gives an error if file already exists.
"t" ---> This mode used to handle text files. There is no difference between "r" & "rt" or "w" & "wt" since text mode is default.
         The default mode is "r" (open for reading text, synonym of "rt").
"b" ---> Used to handle binary files (images, pdfs, etc).
'''

"-----------------------------------------------------------------------------"

'''
Closing a file :
It is important to close a file after you done with it.
This releases the resources used by the file and allow other programs to access it.
'''
f = open("Sample.txt", "r")
# Do something with file.
f.close()

print("-----------------------------------------------------------------------------")

'''
Reading Files :- 
'''
# Read Entire File :-
file = open("Sample.txt", "r")
content = file.read()
print(content)
file.close()

# Read Line By Line :-
file = open("Sample.txt", "r")
for line in file:
    print(line)
file.close()

print("-----------------------------------------------------------------------------")

'''
Writing to Files :-
'''
# Write
file = open("Sample.txt", "w")
file.write("I'm learning about file handling.")
file.close()

# Append
file = open("Sample.txt", "a")
file.write("\nNew line added.")

print("-----------------------------------------------------------------------------")

'''
with Statement :-
Alternatively you can use the with statement to automatically close the file after you are done with it.
'''
with open("Sample.txt", "r") as file:
    content = file.read()
    print(content)    

'''
File Methods :
file.read()      -----> Reads the entire file.
file.readline()  -----> Reads one line at a time.
file.readlines() -----> Read all the lines and returns a list.
file.write()     -----> Writes a string to a file.
file.writelines() ----> Writes a list of strings to a file.
file.seek()      -----> Moves the file cursor to a specific position.
file.tell()      -----> Returns the current file position(cursor).
file.flush()     -----> Forces writing buffered data to a disk.
'''
