'''
Getter :
Used to read (get) the value of a variable.

Setter :
Used to modify (set) the value of a variable.
'''

# THEY HELP IN DATA ENCAPSULATION. (DATA HIDING).

class Student:
    def __init__(self, name):
        self._name = name 

    #GETTER
    @property
    def name(self):
        return self._name 
    
    #SETTER
    @name.setter
    def name(self, value):
        self._name = value

s1 = Student("Ajay")
print(s1.name)

s1.name = "Sushant"
print(s1.name)
