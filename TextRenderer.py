import pygame
from Components import Component

class TextRenderer(Component):
    def __init__(self, font_size) -> None:
        super().__init__()
        self.font = pygame.font.SysFont(None, font_size)
        self.settext("text")
    
    def awake(self, game_world):
        pass

    def start(self):
        pass

    def update(self, delt_time, events):
        pass
    
    def settext(self, text):
        self._img = self.font.render(text, True, (255,255,255))
        self._sprite = pygame.sprite.Sprite()
        self._sprite.rect = self._img.get_rect()
        self._sprite_mask = pygame.mask.from_surface(self._img)
        
    def draw(self, screen, res_multiplier, res_scaler):
        self.scaled_image = pygame.transform.scale(self._img, (int(self._img.get_size()[0] * res_scaler), int(self._img.get_size()[1] * res_scaler)))
        self._sprite.rect = self.scaled_image.get_rect()
        self._sprite.rect.center = self.gameobject.transform.position * res_multiplier
        screen.blit(self.scaled_image, self._sprite.rect)