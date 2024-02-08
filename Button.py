import pygame
from Components import Component

class Button(Component):

    def __init__(self, callback, good) -> None:
        super().__init__()
        self.callback = callback
        if good:
            self._click_sound = pygame.mixer.Sound("Assets//Button Click.mp3")
        else:
            self._click_sound = pygame.mixer.Sound("Assets//Button Unclickable.mp3")

    def awake(self, game_world):
        pass

    def start(self):
        pass

    def update(self, delt_time, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.gameobject.get_component("SpriteRenderer")._sprite.rect.collidepoint(event.pos):
                    self._click_sound.play()
                    self.callback()

    def draw(self, screen, res_multiplier, res_scaler):
        pass