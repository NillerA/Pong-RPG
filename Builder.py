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

class ButtonBuilder(Builder):

    def build(self, image_name, position, callback, good):
        self._gameObject = GameObject(position)
        self._gameObject.add_component(SpriteRenderer(image_name))
        self._gameObject.add_component(Button(callback, good))

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
        self._gameObject = GameObject(pygame.math.Vector2(6.88,2.5))
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
    
    def build(self, startpos):
        self._gameObject = GameObject(startpos)
        self._gameObject.add_component(SpriteRenderer("Guy.png"))
        self._gameObject.add_component(BasicEnemy(0))
        self._gameObject.add_component(Collider())

    def get_gameObject(self) -> GameObject:
        return self._gameObject