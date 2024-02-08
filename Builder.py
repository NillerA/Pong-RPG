from abc import ABC, abstractclassmethod
from GameObject import GameObject
from Components import SpriteRenderer
from Player import Player
from Enemys import BasicEnemy
from Enemys import ShieldEnemy
from Enemys import BossEnemy
from Components import Collider
from Ball import Ball
from Button import Button
import pygame
import random

class Builder(ABC):

    @abstractclassmethod
    def build(self):
        pass

    def get_gameObject(self) -> GameObject:
        pass

class ButtonBuilder(Builder):

    def build(self, image_name, position, callback):
        self._gameObject = GameObject(position)
        self._gameObject.add_component(SpriteRenderer(image_name))
        self._gameObject.add_component(Button(callback))

    def get_gameObject(self) -> GameObject:
        return self._gameObject

class ImageBuilder(Builder):
    
    def build(self, image_name, position):
        self._gameObject = GameObject(position)
        self._gameObject.add_component(SpriteRenderer(image_name))

    def get_gameObject(self) -> GameObject:
        return self._gameObject

class BallBuilder(Builder):
    def build(self, lose_callback):
        self._gameObject = GameObject(pygame.math.Vector2(2,2.5))
        self._gameObject.add_component(Ball(lose_callback))
        self._gameObject.add_component(SpriteRenderer("Ball.png"))
        self._gameObject.add_component(Collider())

    def get_gameObject(self) -> GameObject:
        return self._gameObject

class PlayerBuilder(Builder):

    def build(self, playerNumber):
        self._gameObject = GameObject(pygame.math.Vector2(0,0))
        self._gameObject.add_component(Player(playerNumber))
        if(playerNumber == 0):
            self._gameObject.add_component(SpriteRenderer("Blue bar.png"))
        else:
            self._gameObject.add_component(SpriteRenderer("Red bar.png"))
        self._gameObject.add_component(Collider())
    
    def get_gameObject(self) -> GameObject:
        return self._gameObject
    
        
class EnemyBuilder(Builder):
    
    def build(self, startpos, type):
        self._gameObject = GameObject(startpos)

        component_mapping = {
           "basic": (SpriteRenderer("Guy.png"), BasicEnemy(0), Collider()),
           "Shield" : (SpriteRenderer("Guy ShieldLeft.png"), ShieldEnemy("Left" if random.getrandbits(1) == 0 else "Right"), Collider()),
           "Boss" : (SpriteRenderer("Boss.png"), BossEnemy(0), Collider())
        }
        
        _components = component_mapping.get(type,(None,None,None))

        for component in _components:
            if component is not None:
                self._gameObject.add_component(component)


    def get_gameObject(self) -> GameObject:
        return self._gameObject