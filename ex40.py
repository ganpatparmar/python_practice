class computer(object):
    
    
    def __init__(self,ram,pc):
        self.ram = ram
        self.pc = pc
        
    def config(self):
        print("This computer is ",self.ram,self.pc)
        
        
temp = computer(8,'i3')
temp.config()
print(id(temp.config()))
temp1 = computer(16,'i7')
temp1.config()


