from sys import argv
script,U_name = argv
 #= "ganpat"
prompt = '>'
print(" Hello %s I am %s"%(U_name,script))
print("I would like to ask you some questions")
print("Do you like me? ")
like = input(prompt)


print("where do you live?")
place = input(prompt)

print("what kind of computer yo have?")
c_type = input(prompt)

print("""
So you are %s
%s you said about liking me
you live at %s not sure where it is
and you have a %s computer. Nice.
"""%(U_name,like,place,c_type))
