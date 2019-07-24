import pygame
from images import ship

WINDOW = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
BLACK = 0, 0, 0

class Ship:
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.rect = (x, y, 50, 50)
        self.velocity = 5
        self.image = ship

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.x + 50 < 500:
            self.x += self.velocity
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.velocity
         


    def draw(self):
        game.win.blit(self.image,(self.x, self.y))

class SpaceInvaders:

    def __init__(self):
        self.win = WINDOW
        self.ship = Ship(222.5,425)

    def redraw(self):
        pygame.Surface.fill(self.win,(BLACK))
        self.ship.draw()

    def main_loop(self):
        while True:
            clock.tick(60)
            self.ship.move()
            self.redraw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.update()

game = SpaceInvaders()
game.main_loop()