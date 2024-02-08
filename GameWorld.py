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
        self._screen = pygame.display.set_mode((1920,1080), pygame.NOFRAME)
        self._res_multiplier = self._screen.get_height() / 5
        self._res_scaler = self._screen.get_width() / 1920
        
        self._one = False
        self._two = False
        self._three = False
        self._four = False

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
        background_b.build("Power Pong Background.png", pygame.math.Vector2(4.444,2.5))
        self._game_objects.append(background_b.get_gameObject())
        if self._load_scene > 1:
            if not self._playing:
                pygame.mixer.music.load("assets//In Game.wav")
                pygame.mixer.music.play(-1)
            self._playing = True
            ball_b = BallBuilder()
            ball_b.build(self.Lose)
            self._ball = ball_b.get_gameObject()
            self._game_objects.append(self._ball) 

            player_b = PlayerBuilder()
            player_b.build(0)
            self._game_objects.append(player_b.get_gameObject())
            player_b.build(1)
            self._game_objects.append(player_b.get_gameObject())
        else:
            self._playing = False
        match scene_index:
            case 0:
                pygame.mixer.music.load("assets//Menu.wav")
                pygame.mixer.music.play(-1)

                button_b = ButtonBuilder()
                button_b.build("Level.png", pygame.math.Vector2(2.944,2.5), self.LevelOne, True)
                self._game_objects.append(button_b.get_gameObject())

                if self._one:
                    button_b = ButtonBuilder()
                    button_b.build("Level.png", pygame.math.Vector2(3.944,2.5), self.LevelTwo, True)
                    self._game_objects.append(button_b.get_gameObject())
                else:
                    button_b = ButtonBuilder()
                    button_b.build("Level Locked.png", pygame.math.Vector2(3.944,2.5), self.NotUnlocked, False)
                    self._game_objects.append(button_b.get_gameObject())

                if self._two:
                    button_b = ButtonBuilder()
                    button_b.build("Level.png", pygame.math.Vector2(4.944,2.5), self.LevelThree, True)
                    self._game_objects.append(button_b.get_gameObject())
                else:
                    button_b = ButtonBuilder()
                    button_b.build("Level Locked.png", pygame.math.Vector2(4.944,2.5), self.NotUnlocked, False)
                    self._game_objects.append(button_b.get_gameObject())

                if self._three:
                    button_b = ButtonBuilder()
                    button_b.build("Level.png", pygame.math.Vector2(5.944,2.5), self.LevelFour, True)
                    self._game_objects.append(button_b.get_gameObject())
                else:
                    button_b = ButtonBuilder()
                    button_b.build("Level Locked.png", pygame.math.Vector2(5.944,2.5), self.NotUnlocked, False)
                    self._game_objects.append(button_b.get_gameObject())

                button_b = ButtonBuilder()
                button_b.build("Options Knap.png", pygame.math.Vector2(0.4,0.6), self.Options, True)
                self._game_objects.append(button_b.get_gameObject())

                button_b = ButtonBuilder()
                button_b.build("Exit Knap2.png", pygame.math.Vector2(4.444,3.5), self.QuitGame, True)
                self._game_objects.append(button_b.get_gameObject())

                p_in = ImageBuilder()
                p_in.build("P1 instruct.png",pygame.math.Vector2(0.5,2.5))
                self._game_objects.append(p_in.get_gameObject())
                p_in.build("P2 instruct.png",pygame.math.Vector2(8.444,2.5))
                self._game_objects.append(p_in.get_gameObject())

                tittle = ImageBuilder()
                tittle.build("Power Pong.png",pygame.math.Vector2(4.444,1))
                self._game_objects.append(tittle.get_gameObject())

                player_b = PlayerBuilder()
                player_b.build(0)
                self._game_objects.append(player_b.get_gameObject())
                player_b.build(1)
                self._game_objects.append(player_b.get_gameObject())
            case 1:
                panel = ImageBuilder()
                panel.build("Panel.png", pygame.math.Vector2(4.444,2.5))
                self._game_objects.append(panel.get_gameObject())

                menu_btn = ButtonBuilder()
                menu_btn.build("Exit Knap.png", pygame.math.Vector2(4.444,3.5), self.Menu, True)
                self._game_objects.append(menu_btn.get_gameObject())
            case 2:
                enemy_b = EnemyBuilder()
                enemy_b.build(pygame.math.Vector2(4.444,2.5), "basic")
                self._game_objects.append(enemy_b.get_gameObject())
                self._enemies.append(enemy_b.get_gameObject())
                enemy_b.build(pygame.math.Vector2(4.444,1), "basic")
                self._game_objects.append(enemy_b.get_gameObject())
                self._enemies.append(enemy_b.get_gameObject())
                enemy_b.build(pygame.math.Vector2(4.444,4), "basic")
                self._game_objects.append(enemy_b.get_gameObject())
                self._enemies.append(enemy_b.get_gameObject())
            case 3:
                enemy_b = EnemyBuilder()
                enemy_b.build(pygame.math.Vector2(3.444,2.5), "shield")
                self._game_objects.append(enemy_b.get_gameObject())
                self._enemies.append(enemy_b.get_gameObject())
                enemy_b.build(pygame.math.Vector2(4.444,1), "basic")
                self._game_objects.append(enemy_b.get_gameObject())
                self._enemies.append(enemy_b.get_gameObject())
                enemy_b.build(pygame.math.Vector2(5.444,4), "shield")
                self._game_objects.append(enemy_b.get_gameObject())
                self._enemies.append(enemy_b.get_gameObject())
            case 4:
                enemy_b = EnemyBuilder()
                enemy_b.build(pygame.math.Vector2(4.444,2.5), "basic")
                self._game_objects.append(enemy_b.get_gameObject())
                self._enemies.append(enemy_b.get_gameObject())
                enemy_b.build(pygame.math.Vector2(4.444,1), "basic")
                self._game_objects.append(enemy_b.get_gameObject())
                self._enemies.append(enemy_b.get_gameObject())
                enemy_b.build(pygame.math.Vector2(5.444,1), "basic")
                self._game_objects.append(enemy_b.get_gameObject())
                self._enemies.append(enemy_b.get_gameObject())
                enemy_b.build(pygame.math.Vector2(3.444,1), "basic")
                self._game_objects.append(enemy_b.get_gameObject())
                self._enemies.append(enemy_b.get_gameObject())
                enemy_b.build(pygame.math.Vector2(4.444,4), "basic")
                self._game_objects.append(enemy_b.get_gameObject())
                self._enemies.append(enemy_b.get_gameObject())
            case 5:
                enemy_b = EnemyBuilder()
                enemy_b.build(pygame.math.Vector2(4.444,2.5), "basic")
                self._game_objects.append(enemy_b.get_gameObject())
                self._enemies.append(enemy_b.get_gameObject())
                enemy_b.build(pygame.math.Vector2(4.444,1), "basic")
                self._game_objects.append(enemy_b.get_gameObject())
                self._enemies.append(enemy_b.get_gameObject())
                enemy_b.build(pygame.math.Vector2(4.444,4), "basic")
                self._game_objects.append(enemy_b.get_gameObject())
                self._enemies.append(enemy_b.get_gameObject())
                
                enemy_b.build(pygame.math.Vector2(3.444,2.5), "basic")
                self._game_objects.append(enemy_b.get_gameObject())
                self._enemies.append(enemy_b.get_gameObject())
                enemy_b.build(pygame.math.Vector2(3.444,1), "basic")
                self._game_objects.append(enemy_b.get_gameObject())
                self._enemies.append(enemy_b.get_gameObject())
                enemy_b.build(pygame.math.Vector2(3.444,4), "basic")
                self._game_objects.append(enemy_b.get_gameObject())
                self._enemies.append(enemy_b.get_gameObject())
                
                enemy_b.build(pygame.math.Vector2(5.444,2.5), "basic")
                self._game_objects.append(enemy_b.get_gameObject())
                self._enemies.append(enemy_b.get_gameObject())
                enemy_b.build(pygame.math.Vector2(5.444,1), "basic")
                self._game_objects.append(enemy_b.get_gameObject())
                self._enemies.append(enemy_b.get_gameObject())
                enemy_b.build(pygame.math.Vector2(5.444,4), "basic")
                self._game_objects.append(enemy_b.get_gameObject())
                self._enemies.append(enemy_b.get_gameObject())
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

            delta_time = self._clock.tick(120) / 1000

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

    def Menu(self):
        self._should_load_scene = True
        self._load_scene = 0

    def LevelOne(self):
        self._should_load_scene = True
        self._load_scene = 2
    
    def LevelTwo(self):
        self._should_load_scene = True
        self._load_scene = 3
    
    def LevelThree(self):
        self._should_load_scene = True
        self._load_scene = 4
    
    def LevelFour(self):
        self._should_load_scene = True
        self._load_scene = 5

    def NotUnlocked(self):
        pass

    def Lose(self):
        self._ball.destroy()

        panel = ImageBuilder()
        panel.build("Panel.png", pygame.math.Vector2(4.444,2.5))
        self._game_objects.append(panel.get_gameObject())

        win_text = ImageBuilder()
        win_text.build("YOU LOST.png", pygame.math.Vector2(4.444,2.25))
        self._game_objects.append(win_text.get_gameObject())

        menu_btn = ButtonBuilder()
        menu_btn.build("Exit Knap.png", pygame.math.Vector2(4.444,3.5), self.Menu, True)
        self._game_objects.append(menu_btn.get_gameObject())
    
    def Win(self):
        match self._load_scene:
            case 2:
                self._one = True
            case 3:
                self._two = True
            case 4:
                self._three = True
            case 5:
                self._four = True
        
        self._ball.destroy()

        panel = ImageBuilder()
        panel.build("Panel.png", pygame.math.Vector2(4.444,2.5))
        self._game_objects.append(panel.get_gameObject())

        win_text = ImageBuilder()
        win_text.build("YOU WIN.png", pygame.math.Vector2(4.444,2.25))
        self._game_objects.append(win_text.get_gameObject())

        menu_btn = ButtonBuilder()
        menu_btn.build("Exit Knap.png", pygame.math.Vector2(4.444,3.5), self.Menu, True)
        self._game_objects.append(menu_btn.get_gameObject())

    def Options(self):
        self._should_load_scene = True
        self._load_scene = 1
    
    def QuitGame(self):
        self._running = False
    
gw = GameWorld()

gw.awake()
gw.start()
gw.update()