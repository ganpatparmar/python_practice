#everthing combined
# 1. Implicite
# 2. Override
# 3. Alter 


class Parent(object):
    def implicite(self):
        print("PARENT implicite()")
        
    def override(self):
        print("PARENT override()")
        
    def alter(self):
        print("PARENT alter()")
        
        
class Child(Parent):
    def override(self):
        print("CHILD override()")
        
    def alter(self):
        print("CHILD alter() before PARENT alter()")
        super(Child,self).alter()
        print("CHILD alter() after PARENT alter()")
        
        
        
        
dad = Parent()
son = Child()
print("***** Using implicite mathod *****")
dad.implicite()
son.implicite()
print("***** Using override mathod *****")
dad.override()
son.override()
print("***** Using alter  mathod *****")
dad.alter()
son.alter()

