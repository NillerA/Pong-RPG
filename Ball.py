import pygame
from Components import Component

class Ball(Component):
    def __init__(self) -> None:
        super().__init__()
        self._speed = pygame.math.Vector2(10,5)
        self._right = False
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
        if self.gameobject.transform.position[1] <= 0.2:
            self._up = True
        elif self.gameobject.transform.position[1] >= 4.5:
            self._up = False

    def draw(self, screen, res_multiplier, res_scaler):
        pass

    def on_collision_enter(self, other):
        pass

    def on_collision_exit(self, other):
        pass

    def on_pixel_collision_enter(self, other, collision_mask):
        print(f"pixel collision enter with {other.gameobject.get_component("SpriteRenderer")._sprite_name}")
        

        if other.gameobject.get_component("SpriteRenderer")._sprite_name == "Blue bar.png":
            self._right = True
            self.p1Owned = True
        elif other.gameobject.get_component("SpriteRenderer")._sprite_name == "Red bar.png":
            self._right = False
            self.p1Owned = False
        else:
            if(collision_mask[0] > collision_mask[1]):
                self._up = not self._up
            else:
                self._right = not self._right

        

    def on_pixel_collision_exit(self, other):
        print(f"pixel collision exit with {other.gameobject.get_component("SpriteRenderer")._sprite_name}")