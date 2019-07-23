import pygame
import sys
from classes import Ship






class SpaceInvaders:

    def __init__(self):
        self.window = pygame.display.set_mode((500,500))
        self.ship = Ship(300,300)

    def main_loop(self):
        while True:
            #self.ship.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

play = SpaceInvaders()
game.window
game.main_loop()