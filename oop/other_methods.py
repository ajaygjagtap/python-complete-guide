'''
dir() :
Return a list of attribute and method names available for an object.
'''
class Employee:
    company = "TCS"

    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


e1 = Employee()
e1.name = "Rushi"
e1.show()
e1.change_company("Infosys")
e1.show()
print(Employee.company)

print(dir(Employee))

print("-----------------------------------------------------------------------------")

'''
__dict__ :
Returns a dictionary containing an object's writable attributes.
'''

print(e1.__dict__)  # Instance

print(Employee.__dict__)  # Class

print("-----------------------------------------------------------------------------")

'''
help() :
Displays documentation including description, methods, parameters, docstring, inheritance hierarchy.
'''

print(help(Employee))

