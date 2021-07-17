# using Alter before or after
import random

class Parent(object):
    
    def __init__(self):
        self.list1 = list1 = ['King of Kurkunda','Divine soul','Ask your friend for a suggestion']
        
    
    def alter(self):
        print("PARENT Alter()")
        
    def funny(self,name,surname):
        
        self.name = name
        self.surname = surname
        
        print("First your name was %s and surname was %s"%(self.name,self.surname))
        print("After you met us it changed to %s"%random.choice(self.list1))
        
        
class Child(Parent):
    def alter(self):
        print("CHILD Alter()")
        super(Child,self).alter()
        super(Child,self).funny('Ganpat','PArmar')
        print("CHILD after parent alter()")
        
        
        
        
dad = Parent()
son = Child()

dad.alter()
dad.funny('Meet','Mori')
print('*'*20)
print('*'*20)
print('*'*20)
son.alter()

        