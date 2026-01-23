'''
Class Methods :
It is a type of method that is bound to the class and not the instance of class.
They are defined using @classmethod decorator, followed by function defination.
The first argument of function is always (cls) which represents the class itself.
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

print("-----------------------------------------------------------------------------")

''' 
Class Methods as Alternative Constructors :
Methods that create and return instances of a class using different formats or logic than default __init__ constructor.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2025 - birth_year
        return cls(name, age)
    

p1 = Person("Alice", 25)
p2 = Person.from_birth_year("bob", 2000)
print(p2.name, p2.age)
