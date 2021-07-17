print("Let's practice all that we did in last 20 exercises")
print('you\'d know \'bout escapes\\ about \t tabes and last but not least i.e \n nextline')

poem = (""" 
\t The lovely world
with logic so irmly planted
canot discern \n the need of lovel
nor comprehand passion for intution
and requires an explantion 
\n\t\t where there is NONE""")

print('_'*10)
print(poem)
print('_'*10)

def secret_formula(started):
    jelly_beans = started*500
    jars = jelly_beans/1000
    crates = jars/100
    return jelly_beans,jars,crates
    
start_point = 10000
beans,jars,crates = secret_formula(start_point)
print("With starting point of %d:"%start_point)
print("We have %d number of beans \n %d numbers of jars \n and %d numbers of crates"%(beans,jars,crates))
start_point/=10
print("We \'d have %d number of beans \n %d number of jars and \n%d number of crates"%secret_formula(start_point))