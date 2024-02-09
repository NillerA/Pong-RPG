import pygame
from Components import Component

class Spacebar(Component):
    def __init__(self):
        super().__init__()
        self._speed = pygame.math.Vector2(0,0)

    def awake(self, game_world):
        pass

    def start(self):
        pass

    def update(self, delt_time, events):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.gameobject.destroy()
        
    def draw(self, screen, res_multiplier, res_scaler):
        pass

    