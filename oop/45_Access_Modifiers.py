''' 
Public : 
Accessible everywhere.
No underscore (_) before variable.
'''

class Employee:
    def __init__(self, name):
        self.name = name

    def show_Details(self):
        print(f"The name of Employee is {self.name}")

obj1 = Employee("Alice")
obj1.show_Details()

print("-----------------------------------------------------------------------------")

''' 
Protected : 
Accessible inside class and child class.
Single underscore (_) before variable.
Should not be accessed outside (but still possible)
'''

class Student:
    def __init__(self):
        self._age = 22 

class Child(Student):
        def display(self):
             print(f"Age is {self._age}")

obj2 = Child()
obj2.display()

print("-----------------------------------------------------------------------------")

'''
Private : 
Cannot be accessed directly outside the class.
Double underscore (__) before variable.
Uses name mangling.
'''

class Student:
    def __init__(self):
        self.__marks = 85

    def show(self):
         print(f"Marks are {self.__marks}")

obj3 = Student()
obj3.show()