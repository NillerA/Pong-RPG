import pygame
from Components import Component

class Ball(Component):
    def __init__(self) -> None:
        super().__init__()
        self._speed = pygame.math.Vector2(1,1)
        self._right = True
        self._up = True

        self.p1Owned = True

    def awake(self, game_world):
        collider = self.gameobject.get_component("Collider")
        collider.subscribe("collision_enter",self.on_collision_enter)
        collider.subscribe("collision_exit", self.on_collision_exit)
        collider.subscribe("pixel_collision_enter", self.on_pixel_collision_enter)
        collider.subscribe("pixel_collision_exit", self.on_pixel_collision_exit)

    def start(self):
        pass

    def update(self, delt_time):
        keys = pygame.key.get_pressed()
        movement = pygame.math.Vector2(0,0)
        
        if(self._right):
            self.gameobject.transform.translate(pygame.math.Vector2(self._speed.x * delt_time, 0))
        else:
            self.gameobject.transform.translate(pygame.math.Vector2(-self._speed.x * delt_time, 0))
        if(self._up):
            self.gameobject.transform.translate(pygame.math.Vector2(0, self._speed.y * delt_time))
        else:
            self.gameobject.transform.translate(pygame.math.Vector2(0, -self._speed.y * delt_time))

    def draw(self, screen, res_multiplier, res_scaler):
        pass

    def on_collision_enter(self, other):
        print("collision enter")

    def on_collision_exit(self, other):
        print("collision exit")

    def on_pixel_collision_enter(self, other, collision_mask):
        print("pixel collision enter")
        if(collision_mask[0] > collision_mask[1]):
            self._up = not self._up
        else:
            self._right = not self._right

        if(other.gameobject.get_component("SpriteRenderer")._sprite_name == "Bluebar"):
            self.p1Owned = True
        else:
            self.p1Owned = False

        

    def on_pixel_collision_exit(self, other):
        print("pixel collision exit")