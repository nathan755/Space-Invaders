import pygame
from images import ship, enemys, bonus, laser, small_ship, small_enemies
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



class Button:
    def __init__(self, x, y, w, h, text, active_text, colour, type_):
        self.x = x
        self.y = y
        self.w = w 
        self.h = h
        self.text = text
        self.active_text = active_text
        self.colour = colour
        self.active = False
        self.clicked = False
        self.type_ = type_

    def button_function(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if mouse[0] > self.x and mouse[0] < self.x + self.w and mouse[1] > self.y and mouse[1] < self.y + self.h:
            self.active = True

            if click[0] == 1:
                self.clicked = True
                self.active = False
            else:
                self.clicked = False
        else:
            self.active = False

    def draw(self):
        if self.active:
            game.win.blit(self.text,(self.x,self.y))
        else:
            game.win.blit(self.active_text,(self.x,self.y))


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
        self.move_event2 = pygame.USEREVENT + 2
        self.velocity = 10
        self.hi_score = 00
        self.lasers = []
        self.shootloop = 0
        self.lives = 3
        self.score = 0
        self.small_font = pygame.font.SysFont("Karmatic Arcade", 24)
        self.medium_font = pygame.font.SysFont("Karmatic Arcade", 32)
        self.large_font = pygame.font.SysFont("Karmatic Arcade", 48)
        self.main_menu = True
        self.game_on = False
        self.controls_on = False
        self.play_text = self.small_font.render("PLAY",True, WHITE)
        self.quit_text = self.small_font.render("QUIT", True, WHITE)
        self.controls_text = self.small_font.render("CONTROLS", True, WHITE)
        self.active_play_text = self.medium_font.render("PLAY",True,WHITE)
        self.active_quit_text = self.medium_font.render("QUIT", True, WHITE)
        self.active_controls_text = self.medium_font.render("CONTROLS", True, WHITE)
        self.play_button = Button(50,250,80,40,self.active_play_text,self.play_text,WHITE,"PLAY")
        self.quit_button = Button(50,285,80,40,self.active_quit_text,self.quit_text,WHITE,"QUIT")
        self.controls_button = Button(50,320,200,40,self.active_controls_text,self.controls_text,WHITE,"CONTROLS")
        self.title = self.large_font.render("SPACE", True, WHITE)
        self.title2 = self.large_font.render("INVADERS", True, GREEN)
        self.buttons = [self.play_button, self.quit_button, self.controls_button]
        self.credits_text = self.small_font.render("CREDITS   00", True, WHITE)
        self.hiscore_text = self.small_font.render("HI-SCORE - " + str(self.hi_score) ,True, WHITE)
        self.score_table_text = self.medium_font.render("SCORE", True, WHITE)
        self.score_table_text_2 = self.medium_font.render("TABLE", True, GREEN)
        self.mystry_text = self.small_font.render("?? MYSTRY ??", True, WHITE)
        self.thirty_text = self.small_font.render("30 POINTS", True, WHITE)
        self.twenty_text = self.small_font.render("20 POINTS", True, WHITE)
        self.ten_text = self.small_font.render("10 POINTS", True, WHITE)
        self.shoot_text = self.medium_font.render("SHOOT -- SPACEBAR", True, WHITE)
        self.left_text = self.medium_font.render("MOVE LEFT -- LEFT ARROW ", True, WHITE)
        self.right_text = self.medium_font.render("MOVE RIGHT -- RIGHT ARROW ", True, WHITE)
        self.back_text = self.small_font.render("BACK", True, GREEN)
        self.back_active_text = self.medium_font.render("BACK", True, GREEN)
        self.back =  Button(25,25,100,50, self.back_active_text, self.back_text, GREEN, "BACK")
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
        score_text = self.small_font.render("Score: " + str(self.score) , True, WHITE)
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

    def menu(self):
        pygame.time.set_timer(self.move_event, 500)
        count = 0
        x = 0

        while self.main_menu:
            pygame.Surface.fill(self.win,(BLACK))
            clock.tick(5)
            count += 1
             
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.win.blit(self.title,(300,50))
            self.win.blit(self.title2,(260,105))
            self.win.blit(self.hiscore_text,(100, 550))
            self.win.blit(self.score_table_text,(400,200))
            self.win.blit(self.score_table_text_2,(550,200))
            self.win.blit(small_enemies[0],(420,250))
            self.win.blit(small_enemies[1],(420,300))
            self.win.blit(small_enemies[2],(420,350))
            self.win.blit(small_enemies[3],(420,400))
            self.win.blit(self.thirty_text,(470,250))
            self.win.blit(self.twenty_text,(470,300))
            self.win.blit(self.ten_text,(470,350))
            self.win.blit(self.mystry_text,(470,400))

            for btn in self.buttons:
                btn.button_function()
                btn.draw()
                if btn.clicked:
                    if btn.type_ == "PLAY":
                        self.game_on = True
                        self.main_menu = False
                    elif btn.type_ == "CONTROLS":
                        self.main_menu = False
                        self.controls_on = True

                         
                    elif btn.type_ == "QUIT":
                        pygame.quit()
                        quit()
                
            if count % 2 == 0:
                self.win.blit(self.credits_text,(500, 550))
            if count == 100:
                    count = 0
            pygame.display.update()
    
    def controls(self):
        #back = Button(25,25,100,50, self.back_active_text, self.back_text, GREEN, "BACK")
        while self.controls_on:
            pygame.Surface.fill(self.win,(BLACK))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.win.blit(self.shoot_text,(150,200))
            self.win.blit(self.left_text,(150,250))
            self.win.blit(self.right_text,(150,300))
            self.back.draw()
            self.back.button_function()
            if self.back.clicked:
                self.main_menu = True

                self.controls_on = False

                print("foobar")
              

                        
                        
                    
            pygame.display.update()

    def main_loop(self):
        self.create_enemys()
        self.create_blocks(100,410,50,self.block1)
        self.create_blocks(275,410,50,self.block2)
        self.create_blocks(425,410,50,self.block3)
        self.create_blocks(600,410,50,self.block4)
        pygame.time.set_timer(self.move_event, 1000)
        while True:
            self.controls()
            self.menu()
                



        
           
            while self.game_on:
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
# create controls screen = done
# make enemies shoot
# add mystery enemy 
# create main menu = done
# fix while loops that control the buttons , dunno wjat the fuck is going on... 
# add sounds
# sort out animation.. help! (ie when they are shot)
# make exc file 