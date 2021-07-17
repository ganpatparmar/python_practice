#more printings more learning]
name = 'Ganpat'
age = 19 #not a lie
height = 163 #in inches
weight = 50# in kg
eyes = 'Brown'
teeth = 'White'
hair = 'Black'
my_list = [1,2,'Ganpat','!@#$%^']
print("let's talk about %s."% name)
print("He's  %d inches tall." % height)
print("He's is %d kg heavy." % weight)
print("that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes,hair))
print("if i add %d, %d, %d i get %d" %(age, height, weight,age + height + weight))
print("my list is %s" %my_list)
for i in my_list:
    if i == 'Ganpat':
        print(i)
data = ("John", "Doe", 53.44)
formate_string = "hello %s %s you current balance is $%d"


print(formate_string % data)
