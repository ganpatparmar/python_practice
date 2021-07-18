#Learning Composition

class Other(object):
    def implicit(self):
        print("OTHER implicit()")
        
    def override(self):
        print("OTHER override()")
        
    def alter(self):
        print("OTHER alter()")
        
        
class Child(object):
    def __init__(self):
        self.other = Other()
        
    def implicit(self):
        self.other.implicit()
        
    def override(self):
        print("CHILD override()")
        
    def alter(self):
        print("CHILD alter() Before OTHER alter()")
        self.other.alter()
        print("CHILD alter() After OTHER alter()")
        
        
        
        
        
son = Child()

son.implicit()
son.override()
son.alter()


        
   
        