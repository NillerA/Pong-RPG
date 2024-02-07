import pygame
from Components import Component
import random

class BasicEnemy(Component):

    

    def __init__(self) -> None:
        super().__init__()
        self.Dir = False
        self._curDir = "" 
        self._cooldown = 300
        self.selfspeed = 1
    
    def awake(self, game_world, pos, type):

        self.Dir = bool(random.getrandbits(1))

        self.gameobject.transform.position = pos

    def start(self):
        pass

    def update(self, delt_time):

        if(dir):
            self._curDir = "-"
        else:
           self._curDir = "+"

        self.transform.position.Y += int(self._curDir) + self.speed


        if(delt_time.tick >= self._cooldown):
          self.Dir = bool(random.getrandbits(1))
        

    def draw(self, screen, res_multiplier, res_scaler):
        pass

    def on_pixel_collision_enter(self, other, collision_mask):
        if(other.sprite_name == "Ball"):
          self.kill()

        if(collision_mask[0] > collision_mask[1]):
            self.Dir = not self.Dir


