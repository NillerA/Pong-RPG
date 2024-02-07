from abc import ABC, abstractclassmethod
from GameObject import GameObject
from Components import SpriteRenderer
from Player import Player
from Enemys import BasicEnemy
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

class StartButtonBuilder(Builder):

    def build(self, callback):
        self._gameObject = GameObject(pygame.math.Vector2(4,2))
        self._gameObject.add_component(SpriteRenderer("Level.png"))
        self._gameObject.add_component(Button(callback))

    def get_gameObject(self) -> GameObject:
        return self._gameObject

class BackgroundBuilder(Builder):
    
    def build(self):
        self._gameObject = GameObject(pygame.math.Vector2(0,0))
        self._gameObject.add_component(SpriteRenderer("Power Pong Background.png"))

    def get_gameObject(self) -> GameObject:
        return self._gameObject

class BallBuilder(Builder):
    def build(self):
        self._gameObject = GameObject(pygame.math.Vector2(4.33,2.5))
        self._gameObject.add_component(Ball())
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
    
    def build(self):
        self._gameObject = GameObject(pygame.math.Vector2(4,2))
        self._gameObject.add_component(SpriteRenderer("Guy.png"))
        self._gameObject.add_component(BasicEnemy(0))
        self._gameObject.add_component(Collider())

    def get_gameObject(self) -> GameObject:
        return self._gameObject