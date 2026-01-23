''' 
CLASS :
It is a blueprint or template for crreating objects.

Object :
It is an instance of class.
Used to access the properties of the class.
'''

class Details:      # Creating Class
    name = "Ajay"
    age = 22

obj1 = Details()    # Creating Object

print(obj1.name)    # Printing Values
print(obj1.age)

print("-----------------------------------------------------------------------------")

'''
self Parameter :
It is a reference to the current instance of class.
Used to access variables that belongs to the class.
'''

class Details:      
    name = "Ajay"
    age = 22

    def describe(self):
        print(f"My name is {self.name}, and I'm {self.age} years old.")

obj1 = Details()    
obj1.describe()

print("-----------------------------------------------------------------------------")

'''
Inheritance :
One class acquires properties of another class.

Types : 1. Single
        2. Multiple
        3. Multilevel
        4. Hierarchical
'''

# 1. Single Inheritance : One child class inherits from one parent class.
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show_Details(self):
        print(f"The name of Employee {self.id} is {self.name}")


class Programmer(Employee):
    def show_Language(self):
        print(f"{self.name} is good in python")


e1 = Employee("Alice", 1)
e1.show_Details()

e2 = Programmer("Bob", 2)
e2.show_Details()
e2.show_Language()

print("-----------------------------------------------------------------------------")

# 2. Multiple Inheritance : One child class inherits from multiple parent class.
class Employee1:
    def __init__(self, name):
        self.name = name 

    def show(self):
        print(f"The name is {self.name}")


class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The name is {self.dance}")


class Employee1Dancer(Employee1, Dancer):
    def __init__(self, name, dance):
        self.name = name
        self.dance = dance 

e3 = Employee1Dancer("Emma", "Kathak")
print(e3.name)
print(e3.dance)
e3.show()
print(Employee1Dancer.mro()) # Method Resolution Order

print("-----------------------------------------------------------------------------")

# 3. Multilevel Inheritance : A class is derived from another derived class.
class Animal:
    def eat(self):
        print("Animal eats food")

class Dog(Animal):
    def bark (self):
        print("Dog barks")

class Puppy(Dog):
    def weep(self):
        print("Puppy weeps") # weep means to cry softly

p = Puppy()
p.eat()
p.bark()
p.weep()

print("-----------------------------------------------------------------------------")

# 4. Hierarchical Inheritance : Multiple child classes inherit from one parent class.
class Employee2:
    def work(self):
        print("Employee works")

class Mangaer(Employee2):
    def manage(self):
        print("Manager manages the team")

class Developer(Employee2):
    def code(self):
        print("Developer writes code")

m = Mangaer()
d = Developer()

m.work()
m.manage() 

d.work()
d.code()