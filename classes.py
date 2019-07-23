import pygame
from images import ship
from game import *



class Ship:
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.rect = (x, y, 50, 50)
        self.velocity = 5
        self.image = ship

    def draw(self):
        game.SpaceInvaders.window(blit,self.image((self.x, self.y))



