import pygame
from Components import Component
import random

class BasicEnemy(Component):

    Dir = False
    _curDir = "" 
    _cooldown = 300
    speed = 1
    

    def __init__(self) -> None:
        super().__init__()
    
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
        if(collision_mask[0] > collision_mask[1]):
            self.Dir = not self.Dir


