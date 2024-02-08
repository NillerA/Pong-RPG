import pygame
from Components import Component
import random

class BasicEnemy(Component):
    def __init__(self, type) -> None:
        super().__init__()
        self._cooldown = 300
        self._speed = -2
        self._timer = 0
        self._death_sound = pygame.mixer.Sound("Assets//Enemy Death.mp3")
    
    def awake(self, game_world):
        collider = self.gameobject.get_component("Collider")
        collider.subscribe("pixel_collision_enter", self.on_pixel_collision_enter)

    def start(self):
        pass

    def update(self, delt_time, events):
        self.gameobject.transform.position[1] += self._speed * delt_time
        self._timer += delt_time

        if self.gameobject.transform.position[1] <= 0.55 and self._speed < 0:
            self._speed *= -1
        elif self.gameobject.transform.position[1] >= 4.45 and self._speed > 0:
            self._speed *= -1
        
        if(self._timer >= self._cooldown):
            if random.getrandbits(1) == 0:
                self._speed *= -1
                self._timer -= self._cooldown
        

    def draw(self, screen, res_multiplier, res_scaler):
        pass

    def on_pixel_collision_enter(self, other, collision_mask):
        if(other.gameobject.get_component("SpriteRenderer")._sprite_name == "Ball.png"):
          self._death_sound.play()
          self.gameobject.destroy()

class ShieldEnemy(Component):
    def __init__(self, type) -> None:
        super().__init__()
        self._cooldown = 300
        self._speed = -2
        self._timer = 0
    
    def awake(self, game_world):
        collider = self.gameobject.get_component("Collider")
        collider.subscribe("pixel_collision_enter", self.on_pixel_collision_enter)

    def start(self):
        pass

    def update(self, delt_time, events):
        self.gameobject.transform.position[1] += self._speed * delt_time
        self._timer += delt_time

        if self.gameobject.transform.position[1] <= 0.55 and self._speed < 0:
            self._speed *= -1
        elif self.gameobject.transform.position[1] >= 4.45 and self._speed > 0:
            self._speed *= -1
        
        if(self._timer >= self._cooldown):
            if random.getrandbits(1) == 0:
                self._speed *= -1
                self._timer -= self._cooldown
        
        #turn shield to other side randomly 
        

    def draw(self, screen, res_multiplier, res_scaler):
        pass

    def on_pixel_collision_enter(self, other, collision_mask):
        print(other.gameobject.get_component("SpriteRenderer")._sprite_name)
        #dont die if hit on shield
        if(other.gameobject.get_component("SpriteRenderer")._sprite_name == "Ball.png"):
          self.gameobject.destroy()

class BossEnemy(Component):
    def __init__(self, type) -> None:
        super().__init__()
        self._cooldown = 300
        self._speed = -2
        self._timer = 0
    
    def awake(self, game_world):
        collider = self.gameobject.get_component("Collider")
        collider.subscribe("pixel_collision_enter", self.on_pixel_collision_enter)

    def start(self):
        pass

    def update(self, delt_time, events):
        self.gameobject.transform.position[1] += self._speed * delt_time
        self._timer += delt_time

        if self.gameobject.transform.position[1] <= 0.55 and self._speed < 0:
            self._speed *= -1
        elif self.gameobject.transform.position[1] >= 4.45 and self._speed > 0:
            self._speed *= -1
        
        if(self._timer >= self._cooldown):
            if random.getrandbits(1) == 0:
                self._speed *= -1
                self._timer -= self._cooldown
        

    def draw(self, screen, res_multiplier, res_scaler):
        pass

    def on_pixel_collision_enter(self, other, collision_mask):
        if(other.gameobject.get_component("SpriteRenderer")._sprite_name == "Ball.png"):
            self.gameobject.destroy()