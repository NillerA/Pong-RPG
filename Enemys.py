import pygame
from Components import Component
import random

class BasicEnemy(Component):

    

    def __init__(self, type) -> None:
        super().__init__()
        self.Dir = False
        self._curDir = "" 
        self._cooldown = 300
        self._speed = 2
        self._timer = 0
    
    def awake(self, game_world):
        self.Dir = bool(random.getrandbits(1))

    def start(self):
        pass

    def update(self, delt_time):

        if(dir):
            self._curDir = "-"
        else:
           self._curDir = "+"

        self.gameobject.transform.position[1] += self._speed * delt_time

        self._timer += delt_time
        if(self._timer >= self._cooldown):
            if random.getrandbits(1) == 0:
                self._speed * -1
                self._timer -= self._cooldown
        

    def draw(self, screen, res_multiplier, res_scaler):
        pass

    def on_pixel_collision_enter(self, other, collision_mask):
        if(other.gameobject.get_component("SpriteRenderer")._sprite_name == "Ball"):
          self.kill()

        if(collision_mask[0] > collision_mask[1]):
            self.Dir = not self.Dir


