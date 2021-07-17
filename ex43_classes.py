from sys import exit 
from random import randint

class scene(object):
	def enter(self):
        print("This scene is not yet cinfigured. Subclass it and implement enter()")
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
        
        
class lasor_weapon_armour(scene):
    def enter(self):
        pass
        
class central_corridore(scene):
    def enter(self):
        pass
        
        
class thebridge(scene):
    def enter(self):
        pass
        
        
class escap_pod(scene):
    def enter(self):
        pass
        
        
class map(object):
    def __init__(self, start_scene):
        pass
        
    def next_scene(self,scene_name):
        pass
        
    def opening_scene(self):
        pass
        
        
a_map = map('CENTRAL_CORRIDORE')

a_game = engine(a_map)
a_game.play()


    
   