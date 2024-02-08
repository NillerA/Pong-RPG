import pygame
from Components import Component

class Ball(Component):
    def __init__(self) -> None:
        super().__init__()
        self._speed = pygame.math.Vector2(0,0)
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

    def update(self, delt_time, events):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self._speed = pygame.math.Vector2(2,0)
        
        if(self._right):
            self.gameobject.transform.translate(pygame.math.Vector2(self._speed.x * delt_time, 0))
        else:
            self.gameobject.transform.translate(pygame.math.Vector2(-self._speed.x * delt_time, 0))
        if(self._up):
            self.gameobject.transform.translate(pygame.math.Vector2(0, self._speed.y * delt_time))
        else:
            self.gameobject.transform.translate(pygame.math.Vector2(0, -self._speed.y * delt_time))
        if self.gameobject.transform.position[1] <= 0.375:
            self._up = True
        elif self.gameobject.transform.position[1] >= 4.625:
            self._up = False

    def draw(self, screen, res_multiplier, res_scaler):
        pass

    def on_collision_enter(self, other):
        pass

    def on_collision_exit(self, other):
        pass

    def on_pixel_collision_enter(self, other, collision_mask):
        if other.gameobject.get_component("SpriteRenderer")._sprite_name == "Blue bar.png":
            self._right = True
            self._speed[1] = other.gameobject.transform.position.distance_to(self.gameobject.transform.position) * 10
            self.p1Owned = True
            self._up = other.gameobject.transform.position[1] - self.gameobject.transform.position[1] < 0
        elif other.gameobject.get_component("SpriteRenderer")._sprite_name == "Red bar.png":
            self._right = False
            self._speed[1] = other.gameobject.transform.position.distance_to(self.gameobject.transform.position) * 10
            self.p1Owned = False
            self._up = other.gameobject.transform.position[1] - self.gameobject.transform.position[1] < 0
        else:
            if(collision_mask[0] > collision_mask[1]):
                self._right = not self._right
            else:
                self._up = not self._up

        

    def on_pixel_collision_exit(self, other):
        pass