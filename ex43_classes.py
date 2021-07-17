from sys import exit 
from random import randint

class scene(object):
    def enter(self):
        print("fefre")
        exit(1)
	
    
class engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map
        
    def play(self):
        current_scene = self.scene_map.opening_scene()
        
        while True:
             print("\n",'*' * 10)
             next_scene_name=current_scene.enter()
             current_scene = self.scene_map.next_scene(next_scene_name)
            
        
        
        
class death(scene):
    quips = [
                "You died. You kinda suck at this.",
                "Your mom would be proud.... if were a smater.",
                "Such a looser.",
                "I have a small puppy that's better at this."
            ]
            
            
    def enter(self):
        print(death.quips[randint(0,len(self.quips)-1)])
        exit(1)
        
        
class lasor_weapon_armour(scene):
    def enter(self):
        print("You do a dive roll into the weapon armory, crouch and scan the room")
        print("for more Gothons that might be hiding. It's deadquite, tooquite.")
        print("You stand up and run to the far side of the room and find the")
        print("neautron bomb in its cointainer. There's keypad lock on the box")
        print("and you need to code to get the bomb out. If you get the code")
        print("wrong 10 times and lock closes forever and you can't get the bomb out")
        print("The code is three digit.")
        
        code = "%d%d%d"%(randint(1,9),randint(1,9),randint(1,9))
        guesses = 0
        guess = input("[keypad]> ")
        
        while code != guess and guesses <10:
            print("BZZZEDDD!")
            guesses +=1
            guess = input("[keypad]> ")
            
        if guess == code:
            print("The container clicks open and the seal breaks,letting gas out.")
            print("You grab the neautron bomb and run as fast as you can to the bridge")
            print("where you must place it in the right spot.")
            return 'thebridge'
        else:
            print("The lock buzzes the last time and then you hear a sickening")
            print("melting sound as the mechanism is fused together.")
            print("You decide to sit there, and finally the Gothons blow up the")
            print("ship from there ship and you die")
            return 'death'
        
        
        
        
        
        
        
        
class central_corridore(scene):
    def enter(self):
        print("The Gothons of the Planet Paracal #25 have invaded your ship and destroyed")
        print("Your entire crwe died. You are the last surving member and your last")
        print("mission is to get the Neutron destruction bomb from the laser armory,")
        print("put it int bridge, and blow up the ship after fetting into an ")
        print("escap pod")
        print("\n")
        
        print("You are rnning down a the central corridore to the weapon armory when ")
        print("a Gothons jumps out, red scaly skin, dark grimy teeth, and evil clown costume")
        print("flowing around this hate filled body. He is blockoing the door to the ")
        print("Armory about to pull a weapon to blast you.")
        
        action = input(">>")
        
        if action == "shoot!":
            print("Quick on the draw you yank out your blaster and fire it at the Gothon.")
            print("His clown costume is flowing and moving around his body, which throws")
            print("off your aim. Your blaster hit his costume but misses him entirely. This")
            print("makes him fly into rage and blst you repeatedly in the face untill")
            print("you are dead. Then he eats you")
            return 'death'
        
        elif action == "dodge!":
            print("Like a world class boxer you dodge, weavee, slips, nad slide right")
            print("as the Gothons blaster cranks a laser past your head.")
            print("In the middle of your artful dodge your foot slips and you")
            print("band your head on the metal wall and pass out.")
            print("You wake up shortly after only to die as the Gothons stomps on")
            print("your head and eats you")
            return 'death'
            
        elif action == "tell a joke":
            print("Lucky for you they made you learn Gothons insults in the academy.")
            print("You tell one Gothon joke you know:")
            print("LLgkrek0w Jgieoj Bufiw Bfhewiw Rjioot Wjewio.")
            print("The Gothon stops and, try not to laugh, then bust out laughing and can't move.")
            print("While he is laughing you run up and shoot him square in the head")
            print("putting him down, then jump through the Weapon Armory door.")
            return 'lasor_weapon_armour'
            
            
        else:
            print("DO NOT COMPUTE!")
            return 'central_corridore'
            
            
        
      
        
class thebridge(scene):
    def enter(self):
        print("You burst onto the bridge with the neautron destruction bomb")
        print("under your arm and surpise 5 Gothons who are trying to")
        print("take control of the ship, Each of them has even uglier")
        print("clown costume then the last. They havent pulled their")
        print("weapons out yet, as they see the active bomb under your")
        print("arm and don't want to set it off.")
        
        action = input(">> ")
        
        if action == "throw the bomb":
            print("In a panic you throw the bomb at the group of the Gothons")
            print("and make a leap for the door. Right as you drop it a")
            print("Gothons shoots you right in the back killing you.")
            print("As you die you see another Gothon frantically ry to disarm")
            print("the bomb. You die knowing they will probably nlow up when")
            print("it goes off")
            return 'death'
            
            
        elif action == "slowly place the bomb":
            print("You point your blaster at the bomb under your arm")
            print("and Gothons put their hands up and start to sweat.")
            print("You inch backward to the door, open it, and then carefully")
            print("place bomb on the floor, pointing your blaster at it.")
            print("You then jump back throuh the door, punch the close button")
            print("and blast the lock so Gothons can't get out.")
            print("NOW THE BOMB IS PLACED YOU RUN TO THE ESCAPE POD TO")
            print("get off this tin can.")
            return 'escap_pod'
            
        else:
            print("DOES NOT COMPUTE")
            return 'thebridge'
      
        
        
        
        
        
    
class escap_pod(scene):
    def enter(self):
        print("You rush through the ship desperately trying to make it to")
        print("the escap pod before the whole ship explodes. It seems like")
        print("hardely any Gothons are on the ship, so your run is clear of")
        print("interference. You get to the chamber with the escape pods, and")
        print("now need to pick one to take.Some of them colud be damaged")
        print("but you don't have time to look. There's 5 pod, which one")
        print("wolud you take?")
        
        good_pod = randint(1,5)
        pod = input("[pod #]> ")
        
        if int(pod) != good_pod:
            print("You jump into pod %s and hit the eject button."%pod)
            print("The pod escape out into the void of space, then")
            print("impoads as the hull ruptures, crusing your body")
            print("into jam jelly.")
            return 'death'
            
        else:
            print("You jump into pod %s and hit the eject button."%pod)
            print("The pod easily slides out into space heading to")
            print("the planet below. As it flies to the planet, you look")
            print("back and see your ship impoade the expode like a")
            print("bright star, taking out Gothon ship at he same")
            print("time. You won!")
            
            return 'finished'
            
            
            
        
        
        
class Map(object):
    scene = {
                'central_corridore' : central_corridore(),
                'lasor_weapon_armour' : lasor_weapon_armour(),
                'thebridge': thebridge(),
                'escap_pod': escap_pod(),
                'death': death()
                }
                
    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def next_scene(self,scene_name):
        return Map.scene.get(scene_name)
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
        
        
a_map = Map('central_corridore')

a_game = engine(a_map)
a_game.play()


    
   
