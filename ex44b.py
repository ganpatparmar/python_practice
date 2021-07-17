#learning for overriding explicitely

class parent(object):
    def override(self):
        print("PARENT override()")
        
        
class child(parent):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def override(self):
        print("CHILD override()")
        
    def fun(self,mem):
        self.mem = mem
        bob = self.mem+self.a+self.b
        print(bob)
        
        
dad = parent()

son = child(2,3)

dad.override()
son.override()
son.fun(23)
