import pygame
from images import ship



class Ship:
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.rect = (x, y, 50, 50)
        self.velocity = 5
        self.image = ship

    def draw(self):
        SpaceInvaders.window(blit,self.image((self.x, self.y)))



class SpaceInvaders:

    def __init__(self):
        self.window = pygame.display.set_mode((500,500))
        self.ship = Ship(300,300)

    def main_loop(self):
        while True:
            self.ship.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

play = SpaceInvaders()

play.main_loop()