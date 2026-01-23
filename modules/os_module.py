'''
The os module in Python is a built-in module that 
allows you to interact with the operating system 
like handling files, folders, environment variables, paths, and more. 
It's very powerful when working with system-level tasks.
'''

# File and folder opertions
import os

print("Current Directory:", os.getcwd())
os.mkdir("TestFolder")          # Create folder
print("Folders:", os.listdir())  # List folders and files
os.rmdir("TestFolder")          # Remove folder

"-----------------------------------------------------------------------------"

# Working with paths
path = "/home/user"
print(os.path.exists(path))     # Check path
print(os.path.join(path, "file.txt"))  # Join path

"-----------------------------------------------------------------------------"

# Environment variables
print(os.environ.get('PATH'))   # Get system PATH
