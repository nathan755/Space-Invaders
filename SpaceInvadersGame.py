import pygame
from images import ship, enemys, bonus, laser, small_ship
pygame.init()
WINDOW = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
BLACK = 0, 0, 0
GREEN = 78, 255, 87
WHITE = 255, 255, 255 

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
        self.h = 50
        self.enemy_type = enemy_type
        self.img = enemys[self.enemy_type][0] # ----> lol
        self.velocity = 15
        
    def draw(self):
        game.win.blit(self.img,(self.x, self.y))


class Block:
    def __init__(self, x, y, w, h):
        self.rect = x, y, w, h
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        pygame.draw.rect(game.win, GREEN, (self.rect))


class Projectile:
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.w = 1
        self.h = 1
        self.img = laser
        self.velocity = 10

    def draw(self):
        game.win.blit(self.img,(self.x, self.y))


class SpaceInvaders:
    def __init__(self):
        self.win = WINDOW
        self.ship = Ship(300,530)
        self.block1 = 100,410
        self.block2 = 275,410
        self.block3 = 425,410
        self.block4 = 600,410
        self.blocks = []
        self.enemys = []
        self.move_event = pygame.USEREVENT + 1
        self.velocity = 10
        self.lasers = []
        self.shootloop = 0
        self.lives = 3
        self.score = 0
        self.small_font = pygame.font.SysFont("Karmatic Arcade", 24)
        self.medium_font = pygame.font.SysFont("Karmatic Arcade", 24)
        self.large_font = pygame.font.SysFont("Karmatic Arcade", 48)

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

    def create_blocks(self, x, y, num, block):
        count = 0
        for i in range(num):
            self.blocks.append(Block(x, y, 10, 10))
            x += 10 
            count += 1
            if count == 10:
                y += 10
                x = block[0]
                count = 0
    
    def redraw(self):
        pygame.Surface.fill(self.win,(BLACK))
        self.ship.draw()
        for block in self.blocks:
            block.draw()
        for enemy in self.enemys:
            enemy.draw()
        for laser in self.lasers:
            laser.draw()
        self.display_lives()
        self.score_handler()

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

    def collision_check(self):
    
        for laser in self.lasers:
            for block in self.blocks:
                if laser.x > block.x and laser.x < block.x + block.w and laser.y == block.y:
                    self.blocks.pop(self.blocks.index(block))
                    self.lasers.pop(self.lasers.index(laser))

            for enemy in self.enemys:
                if laser.x > enemy.x and laser.x < enemy.x + enemy.w and laser.y > enemy.y and laser.y < enemy.y + enemy.h:
                    if enemy.enemy_type == "enemy1":
                        self.score += 30
                    elif enemy.enemy_type == "enemy2":
                        self.score += 20
                    elif enemy.enemy_type == "enemy3":
                        self.score += 10
                    elif enemy.enemy_type == "mystry":
                        self.score += 100 
                    self.lasers.pop(self.lasers.index(laser))
                    self.enemys.pop(self.enemys.index(enemy))
    
    def score_handler(self):
        score_text = self.small_font.render("Score: " + str(self.score), True, WHITE)
        self.win.blit(score_text,(10,10))

    def display_lives(self):
        if self.lives == 3:
            self.win.blit(small_ship,(700,10))
            self.win.blit(small_ship,(730,10))
            self.win.blit(small_ship,(760,10))
        elif self.lives == 2:
            self.win.blit(small_ship,(700,10))
            self.win.blit(small_ship,(730,10))
        elif self.lives == 1:
            self.win.blit(small_ship,(700,10))

    def main_loop(self):
        self.create_enemys()
        self.create_blocks(100,410,50,self.block1)
        self.create_blocks(275,410,50,self.block2)
        self.create_blocks(425,410,50,self.block3)
        self.create_blocks(600,410,50,self.block4)
        pygame.time.set_timer(self.move_event, 1000)

        while True:
            clock.tick(60)
            self.ship.move()
            self.collision_check()
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


#####todo######

# draw lives = done
# draw score = done
# create collison detection if enenmies hit blocks 
# create game over screen 
# create pause screen 
# create controls screen 
# make enemies shoot
# add mystery enemy 
# create main menu
# add sounds
# sort out animation.. help! (ie when they are shot)
# make exc file 