#program to use fution return values
def add(a,b):
    print("ADDITION OF %d and %d"%(a,b))
    return a+b
    
def sub(a,b):
    print("SUBSTRACTION OF %d and %d"%(a,b))
    return a-b
    
    
def mul(a,b):
    print("MULTIPLICATION OF %d and %d" %(a,b))
    return a*b
    
def div(a,b):
    print("DIVSON OF %d and %d "%(a,b))
    return a/b 
age = add(23,12)
height = sub(198,45)
weight = mul(12,6)
iq = div(100/3,4)

print("So your age is %d \n your height is %d \n your weight is %d \n your IQ is %d you look much inteligent then me \n so nice of you"%(age,height,weight,iq))

print("Here is a puzzle")
what = sub(age,(add(height,div(weight,mul(iq,7)))))
print("That becomes ", what,"Can you do it by yourself?") 

we = 1+(2+(7/8-(6*102)))
print(we)