import pygame
from Components import Component

class Player(Component):
    def __init__(self, playerNumber) -> None:
        super().__init__()
        self._speed = 5
        self._player_number = playerNumber

    def awake(self, game_world):
        if(self._player_number == 0):
            self.gameobject.transform.position = pygame.math.Vector2(1,2)
        elif(self._player_number == 1):
            self.gameobject.transform.position = pygame.math.Vector2(8,2)

    def start(self):
        pass

    def update(self, delt_time):
        keys = pygame.key.get_pressed()
        movement = pygame.math.Vector2(0,0)
        
        if(self._player_number == 0):
            if(keys[pygame.K_w] and self.gameobject.transform.position.Y <= 1):
                movement.y -= self._speed * delt_time
            if(keys[pygame.K_s] and self.gameobject.transform.position.Y >= 7):
                movement.y += self._speed * delt_time

        elif(self._player_number == 1):
            if(keys[pygame.K_UP] and self.gameobject.transform.position.Y <= 1):
                movement.y -= self._speed * delt_time
            if(keys[pygame.K_DOWN] and self.gameobject.transform.position.Y >= 7):
                movement.y += self._speed * delt_time
        self.gameobject.transform.translate(movement)

    def draw(self, screen, res_multiplier, res_scaler):
        pass