'''
super() :
Used to call methods or access attributes of parent (super) class.
'''

class ParentClass:
    def parent_method(self):
        print("This is parent method.")

class ChildClass(ParentClass):
    def child_method(self):
        print("This is child method.")

        super().parent_method()

child_obj = ChildClass()
child_obj.child_method()