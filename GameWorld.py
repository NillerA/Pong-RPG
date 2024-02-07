import pygame
from GameObject import GameObject
from Components import SpriteRenderer
from Components import Collider
from Player import Player
from Ball import Ball

class GameWorld:

    def __init__(self) -> None:
        pygame.init()
        self._game_objects = []
        self._colliders = []
        self._screen = pygame.display.set_mode((1280,720))
        self._res_multiplier = self._screen.get_height() / 5
        self._res_scaler = self._screen.get_width() / 1920

        go = GameObject(pygame.math.Vector2(0,0))
        go.add_component(SpriteRenderer("Power Pong Background.png"))
        self._game_objects.append(go)

        go = GameObject(pygame.math.Vector2(0,0))
        go.add_component(Player(0))
        go.add_component(SpriteRenderer("Blue bar.png"))
        go.add_component(Collider())
        self._game_objects.append(go)

        go = GameObject(pygame.math.Vector2(0,0))
        go.add_component(Player(1))
        go.add_component(SpriteRenderer("Red bar.png"))
        go.add_component(Collider())
        self._game_objects.append(go)

        go = GameObject(pygame.math.Vector2(2,3))
        go.add_component(Ball())
        go.add_component(SpriteRenderer("Ball.png"))
        go.add_component(Collider())
        self._game_objects.append(go)
        self._running = True
        self._clock = pygame.time.Clock()

    def awake(self):
        for game_object in self._game_objects[:]:
            game_object.awake(self)

    @property
    def colliders(self):
        return self._colliders
    
    def start(self):
        for game_object in self._game_objects[:]:
            game_object.start()

    def update(self):
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
            self._screen.fill("cornflowerblue")

            delta_time = self._clock.tick(60) / 1000

            for game_object in self._game_objects[:]:
                game_object.update(delta_time)

            for i, collider1 in enumerate(self._colliders):
                for j in range(i + 1, len(self._colliders)):
                    collider2 = self._colliders[j]
                    collider1.collision_check(collider2)

            for game_object in self._game_objects[:]:
                game_object.draw(self._screen, self._res_multiplier, self._res_scaler)
            
            pygame.display.flip()
            self._clock.tick(60)
        pygame.quit()

gw = GameWorld()

gw.awake()
gw.start()
gw.update()