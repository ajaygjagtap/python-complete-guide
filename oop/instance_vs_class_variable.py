'''
Instance Variable :
Belongs to an object.
Each object has its own copy.
Defined inside __init__() using self.

Class Variable :
Belongs to the class.
Shared among all objects.
Defined inside class but outside methods.
'''

class Employee:
    company = "TCS"     # Class Variable

    def __init__(self, name):
        self.name = name    # Instance Variable

e1 = Employee("Rushi")

Employee.company = "Capgemini"

print(f"{e1.name} works in {e1.company}")
