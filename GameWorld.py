import pygame
from GameObject import GameObject
from Builder import StartButtonBuilder
from Builder import BackgroundBuilder
from Builder import PlayerBuilder
from Builder import BallBuilder
from Builder import EnemyBuilder

class GameWorld:

    def __init__(self) -> None:
        pygame.init()
        self._game_objects = []
        self._colliders = []
        self._screen = pygame.display.set_mode((1280,720))
        self._res_multiplier = self._screen.get_height() / 5
        self._res_scaler = self._screen.get_width() / 1920

        self.LoadScene(0)

        self._running = True
        self._clock = pygame.time.Clock()

    def LoadScene(self, scene_index):
        self._game_objects = []
        self._colliders = []

        match scene_index:
            case 0:
                background_b = BackgroundBuilder()
                background_b.build()
                self._game_objects.append(background_b.get_gameObject())

                button_b = StartButtonBuilder()
                button_b.build(self.LevelOne)
                self._game_objects.append(button_b.get_gameObject())
            case 1:
                background_b = BackgroundBuilder()
                background_b.build()
                self._game_objects.append(background_b.get_gameObject())

                player_b = PlayerBuilder()
                player_b.build(0)
                self._game_objects.append(player_b.get_gameObject())
                player_b.build(1)
                self._game_objects.append(player_b.get_gameObject())

                ball_b = BallBuilder()
                ball_b.build()
                self._game_objects.append(ball_b.get_gameObject()) 

                enemy_b = EnemyBuilder()
                enemy_b.build()
                self._game_objects.append(enemy_b.get_gameObject())
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
        self.awake()
        self.start()

    def LevelOne(self):
        self.LoadScene(1)

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