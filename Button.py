import pygame
from Components import Component

class Button(Component):

    def __init__(self, callback) -> None:
        super().__init__()
        self.callback = callback

    def awake(self, game_world):
        pass

    def start(self):
        pass

    def update(self, delt_time):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.gameobject.get_component("SpriteRenderer")._sprite.rect.collidepoint(event.pos):
                    self.callback()

    def draw(self, screen, res_multiplier, res_scaler):
        pass