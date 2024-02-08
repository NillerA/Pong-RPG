import pygame
from Components import Component
import random

class BasicEnemy(Component):
    def __init__(self, type) -> None:
        super().__init__()
        self._cooldown = 8
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
                self._speed *= random.choice([-1, 1])
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
        self._cooldown = 5
        self._speed = -2
        self._timer = 0
        self._type = type
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
            self._type = random.choice(["Left","Right"])
            self._speed *= random.choice([1,-1])
            self._timer -= self._cooldown
            self.ChangeType()
    
    def ChangeType(self):
        sprite_renderer = self.gameobject.get_component("SpriteRenderer")
        sprite_name = f"Guy Shield{self._type}.png"
        sprite_renderer.set_sprite(sprite_name)

    def draw(self, screen, res_multiplier, res_scaler):
        pass

    def on_pixel_collision_enter(self, other, collision_mask):
        if other.gameobject.get_component("SpriteRenderer")._sprite_name == "Ball.png":
            ball_position = other.gameobject.transform.position[0]

            print(f"enemy was{self._type}")

            if self._type == "Left" and self.gameobject.transform.position[0] < ball_position or self._type == "Right" and self.gameobject.transform.position[0] > ball_position:
                self._death_sound.play()
                self.gameobject.destroy()

class BossEnemy(Component):
    def __init__(self, type) -> None:
        super().__init__()
        self._cooldown = 3
        self._speed = 1
        self._timer = 0
        self._life = 4
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
                self._speed *= random.choice([-1, 1])
                self._timer -= self._cooldown

        if self._life <= 0:
            self.gameobject.destroy()
        

    def draw(self, screen, res_multiplier, res_scaler):
        pass

    def on_pixel_collision_enter(self, other, collision_mask):
       
        if(other.gameobject.get_component("SpriteRenderer")._sprite_name == "Ball.png"):
          self._death_sound.play()
          self._life -= 1
