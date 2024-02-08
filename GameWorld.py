import pygame
from GameObject import GameObject
from Builder import ButtonBuilder
from Builder import ImageBuilder
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

        self._load_scene = 0
        self._should_load_scene = False
        self.LoadScene(0)

        self._running = True
        self._playing = False
        self._clock = pygame.time.Clock()
        

    def LoadScene(self, scene_index):
        self._game_objects = []
        self._colliders = []
        self._enemies = []
        self._should_load_scene = False

        background_b = ImageBuilder()
        background_b.build("Power Pong Background.png", pygame.math.Vector2(4.3333,2.5))
        self._game_objects.append(background_b.get_gameObject())
        if self._load_scene > 0:
            self._playing = True
        else:
            self._playing = False
        match scene_index:
            case 0:
                button_b = ButtonBuilder()
                button_b.build("Level.png", pygame.math.Vector2(4.3333,2.5), self.LevelOne)
                self._game_objects.append(button_b.get_gameObject())

                player_b = PlayerBuilder()
                player_b.build(0)
                self._game_objects.append(player_b.get_gameObject())
                player_b.build(1)
                self._game_objects.append(player_b.get_gameObject())
            case 1:
                ball_b = BallBuilder()
                ball_b.build(self.Lose)
                self._game_objects.append(ball_b.get_gameObject()) 

                player_b = PlayerBuilder()
                player_b.build(0)
                self._game_objects.append(player_b.get_gameObject())
                player_b.build(1)
                self._game_objects.append(player_b.get_gameObject())

                enemy_b = EnemyBuilder()
                enemy_b.build(pygame.math.Vector2(4.333,2.5))
                self._game_objects.append(enemy_b.get_gameObject())
                self._enemies.append(enemy_b.get_gameObject())
                enemy_b.build(pygame.math.Vector2(4.333,1))
                self._game_objects.append(enemy_b.get_gameObject())
                self._enemies.append(enemy_b.get_gameObject())
                enemy_b.build(pygame.math.Vector2(4.333,4))
                self._game_objects.append(enemy_b.get_gameObject())
                self._enemies.append(enemy_b.get_gameObject())
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
        self.awake()
        self.start()

    def awake(self):
        for game_object in self._game_objects[:]:
            game_object.awake(self)

    @property
    def colliders(self):
        return self._colliders
    
    def start(self):
        for game_object in self._game_objects[:]:
            game_object.start()
            game_object.draw(self._screen, self._res_multiplier, self._res_scaler)
        pygame.display.flip()

    def update(self):
        while self._running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self._running = False

            delta_time = self._clock.tick() / 1000

            for game_object in self._game_objects[:]:
                game_object.update(delta_time, events)

            for i, collider1 in enumerate(self._colliders):
                for j in range(i + 1, len(self._colliders)):
                    collider2 = self._colliders[j]
                    collider1.collision_check(collider2)
            
            if self._playing:
                if self._enemies.__len__() is 0:
                    self.Win()

            for game_object in self._game_objects[:]:
                game_object.draw(self._screen, self._res_multiplier, self._res_scaler)
            
            self._colliders = [obj for obj in self._colliders if not obj.gameobject.is_destroyed]
            self._game_objects = [obj for obj in self._game_objects if not obj.is_destroyed]
            self._enemies = [obj for obj in self._enemies if not obj.is_destroyed]
            
            pygame.display.flip()
            if self._should_load_scene:
                self.LoadScene(self._load_scene)
        pygame.quit()

    
    def LevelOne(self):
        self._should_load_scene = True
        self._load_scene = 1
    
    def Lose(self):
        self._should_load_scene = True
        self._load_scene = 1
    
    def Win(self):
        self._should_load_scene = True
        self._load_scene = 0

    def Options(self):
        print("implement")
    
gw = GameWorld()

gw.awake()
gw.start()
gw.update()