ten_stuff = "Apple Oranges Cross Telephones Light Sugar"

print("Well there is not ten things to that list. let's fix them")
stuff = ten_stuff.split(" ")
more_stuff = ['Day','Night','Song','Firsbee','Corn','Banana','Girl','Boy']

while len(stuff) != 10:
    next_stuff = more_stuff.pop()
    print("Adding %s to list"%next_stuff)
    stuff.append(next_stuff)
    print("Now size of list is %d"%len(stuff))


print("THere we Go",stuff)
print("Let's play with this list." )
print(stuff[4])
print(stuff[-1]) # printing last item of this array
print(stuff.pop())
print('\n'.join(stuff))
print('#'.join(stuff[5:8]))
