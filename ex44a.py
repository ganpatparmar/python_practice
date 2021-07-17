
# learning for a implicite inheritance

class Parent(object):
    def implicite(self):
        print("Parent Implicite()")
        
class Child(Parent):
    pass
    
    
dad = Parent()
son = Child()

dad.implicite()
son.implicite()
