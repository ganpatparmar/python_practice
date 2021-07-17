i = 6
number = []

while( i >= 0 ):
    print("At the top i is %d"%i)
    number.append(i)
    i-=1
    
    print("Number's now:- ",number)
    
    print("At the bottom i is %d"%i)
    
    
print("The numbers: ")

for i in number:
    print(i)
    