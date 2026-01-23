'''
Decorators :
It is a function that takes another function as an argument and
returns a new function that modifies the behavior of the original function.
'''

def msg(fx):
    def wrapper():
        print("Start")
        print("------------------------------------")
        fx()
        print("------------------------------------")
        print("End")
    return wrapper
    
@msg
def display():
    print("Hello")

display()
