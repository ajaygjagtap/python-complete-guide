'''
Constructors :
Special method in a class used to create and initialize an object of class.
A constructor is a unique function that gets called automatically when an object of class is created.
'''

class Details:      

    def __init__(self, n, a):   # Parameterized Constructor
        self.name = n
        self.age = a

    def info(self):
        print(f"My name is {self.name} and I'm {self.age} years old.")  

obj1 = Details("Ajay", 22)    
obj2 = Details("Sushant", 23)   
obj1.info()
obj2.info()

print("-----------------------------------------------------------------------------")

class Student:      

    def __init__(self, id = 0, name = "Unknown"):   
        self.id = id
        self.name = name

    def display(self):
        print(self.id, self.name)  

obj1 = Student()            # Default Behavior
obj2 = Student(53, "Ajay")  # Parameterized Behavior
obj1.display()
obj2.display()