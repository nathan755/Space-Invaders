import pygame
import sys 






class SpaceInvaders:
    def __init__(self):
        self.window = pygame.display.set_mode((500,500))

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

game = SpaceInvaders()
game.window
game.main_loop()