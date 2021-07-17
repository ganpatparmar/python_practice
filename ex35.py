from sys import exit


def gold_room():
    print("This room is full of GOLD. How much would you take?")
    
    next = input('> ')
    if "0" in next or "1" in next:
        how_much = int(next)
    
    else:
        dead("Man learn to type a number.")
    
    if how_much < 50:
        print("Nice, you are not a greedy, you win!")
    
    else:
        dead("You greedy bastard!")
        
        
def bear_room():
    print("There is a bear here.")
    print("The bear has bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    
    while True:
        next = input('> ')
        if next == "take honey":
            dead("The bear looks at you and then slap your face off")
            
        elif next == "taunt bear" and not bear_moved:
            print("Bear has moved from the door. You can go through it now.")
            bear_moved = True
            
        elif next == "Open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")
            
def cthulhu_room():
    print("Here you see great evil Chulthu")
    print("He eat whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    
    next = input('> ')
    
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tastey.")
    else:
        cthulhu_room()
        
def dead(why):
    print(why,"Good job.")
    exit(0)
    
def start():
    print("You are in a dark room.")
    print("There is door to your right and left.")
    print("Which one do you take?")
    
    next = input('> ')
    if next == "left":
        bear_room()
        
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stamble around the room untill you starve.")

print("there is intresting game for you would you like to play")
new = input('> ')
if new == "yes":
    start()
    
else:
    exit(0)