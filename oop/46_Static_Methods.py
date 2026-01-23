'''
Static Methods :
Methods that belongs to a class but do not depend on instance (self) or class (cls) data.
They are defined using @staticmethod decorator.
They are called on the class itself.
'''

class Math:
    @staticmethod
    def add(a, b):
        return a + b
    
result = Math.add(1, 8)
print(result)