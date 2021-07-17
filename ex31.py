print("You enter a dark room with two doors. Do you go through #1 door to #10 door ")
for x in range(1,10):
    print(x)
print("Any of the door you want")

door = input('> ')

if door == "1":
    print(" There's giant bear here eating a chees cack. What do you do?")
    print("1. Take the cack.")
    print("2. Screme at the bear.")
    
    
    bear = input('> ')
    
    if bear == "1":
        print("The bear eats you face off. Good job!")
        
    elif bear == "2":
        print("The bear eats you legs off. Good job!")
        
    else:
        print("Well, douing %s is probably better. Bears runs away."%bear)
        

elif door == "2":
    print("You stare into the endless abyss at cthulu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jackets clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    
    insanity = input('> ')
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. Good job!")
    
    else:
        print("The insanity rots your eyes into a pool of muck. Good job!")
        
else:
    print("You stumble around and fall on kinfe and die. Good ob!")

    
    