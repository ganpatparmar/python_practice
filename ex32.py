number = [1,2,3,4,5,8,8,8,8,8,8]
fruits = ['apples','blueberries','jackfruit','mango','chicku']
changes = [1,'pennies',2,'dimes',3,'quarters']

for i in number:
    print("This is count %d"%i)
    
for i in fruits:
    print("A fruit of type: %s"%i)
    
for i in changes:
    print("I got for %r"%i)
    
element = []

for i in range(0,6):
    print("Adding %d to the list"%i)
    #this function append to the list
    element.append(i)
    
    
for i in element:
    print("Element was %d"%i)
    
    
number.extend([6,7,8,'hi how are you','whats upp'])
for i in number:
    print("\t",i)
    
    
    
number.insert(3,"ganpat")
number.insert(3,4)
num = [1,2,3,4,5,6,7,8,9]
for i in number:
    for x in num:
        print("\t"*x,i)
number.remove(2)

for i in number:
    print(i)
number.pop(10)
for i in number:
    for x in num:
        print("\n \t"*x,i)


print(number[:2])
print(number[4:])
print(number[5:9])
print(number[:])
print(number[::-1])
number.reverse()
print(len(number))
print(max(num))
print(min(num))
print(number.count(8))
new = number+num
#for i in range(1,6):
    #for x in range(1,6):
        #print("\t"*x,new*5)
        
print(number.index('ganpat'))
num2 = [4,34,54,3,245,6546,64536,344,543542245,4532235,42452354,352]
num2.sort()
print(num2)

