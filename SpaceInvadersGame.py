import pygame
from images import ship, enemys, bonus, laser

WINDOW = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
BLACK = 0, 0, 0
GREEN = 78, 255, 87
left = False
right = True

class Ship:
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.rect = (x, y, 50, 50)
        self.velocity = 7
        self.image = ship 

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.x + 55 < 790:
            self.x += self.velocity
        if keys[pygame.K_LEFT] and self.x - 10 > 0:
            self.x -= self.velocity
    
    def draw(self):
        game.win.blit(self.image,(self.x, self.y))


class Enemy:
    def __init__(self, x, y, enemy_type):
        self.x = x
        self.y = y
        self.w = 50
        self.h =50
        self.enemy_type = enemy_type
        self.img = enemys[self.enemy_type][0] # ----> lol
        self.velocity = 15
        
    def draw(self):
        game.win.blit(self.img,(self.x, self.y))


class Block:
    def __init__(self, x, y, w, h):
        self.rect = x, y, w, h

    def draw(self):
        pygame.draw.rect(game.win, GREEN, (self.rect))


class Projectile:
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.w = 5
        self.h = 5
        self.img = laser
        self.velocity = 10

    def draw(self):
        game.win.blit(self.img,(self.x, self.y))


class SpaceInvaders:
    def __init__(self):
        self.win = WINDOW
        self.ship = Ship(300,530)
        self.block1 = Block(100,410,100,50)
        self.block2 = Block(275,410,100,50)
        self.block3 = Block(425,410,100,50)
        self.block4 = Block(600,410,100,50)
        self.enemys =[]
        self.move_event = pygame.USEREVENT + 1
        self.velocity = 10
        self.lasers = []
        self.shootloop = 0 

    def create_enemys(self):
        x = 153
        for _ in range(11):
            self.enemys.append(Enemy(x, 100, "enemy1"))
            x += 45
        x = 153
        for enemy in range(11):
            self.enemys.append(Enemy(x, 135, "enemy2"))
            x += 45
        x = 153 
        for enemy in range(11):
            self.enemys.append(Enemy(x, 175, "enemy2"))
            x+=45
        x = 153
        for enemy in range(11):
            self.enemys.append(Enemy(x, 220, "enemy3"))
            x += 45
        x = 153
        for enemy in range(11):
            self.enemys.append(Enemy(x, 265, "enemy3"))
            x += 45

    def redraw(self):
        pygame.Surface.fill(self.win,(BLACK))
        self.ship.draw()
        self.block1.draw()
        self.block2.draw()
        self.block3.draw()
        self.block4.draw()
        for enemy in self.enemys:
            enemy.draw()
        for laser in self.lasers:
            laser.draw()

    def move_enemys(self):
        for enemy in self.enemys:
            if enemy.x > 700:
                self.velocity = -15
                for enemy in self.enemys:
                    enemy.y += 3
            elif enemy.x < 100:
                self.velocity = 15
                for enemy in self.enemys:
                    enemy.y += 3
        for enemy in self.enemys:
            enemy.x += self.velocity

    def main_loop(self):
        self.create_enemys()
        pygame.time.set_timer(self.move_event, 1000)

        while True:
            clock.tick(60)
            self.ship.move()
            self.redraw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == self.move_event:
                    self.move_enemys()
                    

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                if len(self.lasers) < 5 and self.shootloop == 0:
                    self.lasers.append(Projectile(self.ship.x + 23, self.ship.y))


            self.shootloop += 1
            if self.shootloop > 3:
                self.shootloop = 0
            for laser in self.lasers:

                if laser.y > 0:
                    laser.y -= laser.velocity
                else:
                    self.lasers.pop(self.lasers.index(laser))
               
            pygame.display.update()

game = SpaceInvaders()
game.main_loop()


