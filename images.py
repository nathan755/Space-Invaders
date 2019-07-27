import pygame

ship = pygame.image.load("ship.png")
enemys = {"enemy1":[pygame.transform.scale(pygame.image.load ("enemy1_1.png"),(30,30)),
                    pygame.image.load ("enemy1_2.png"),
                    pygame.image.load ("explosionpurple.png"),("hello")
                    ],
        
        "enemy2": [  pygame.transform.scale(pygame.image.load ("enemy2_1.png"),(40,40)),
                     pygame.image.load ("enemy2_2.png"),
                     pygame.image.load ("explosionblue.png")],

        "enemy3":    [pygame.transform.scale(pygame.image.load ("enemy3_1.png"),(44,44)),
                     pygame.image.load ("enemy3_2.png"),
                     pygame.image.load ("explosiongreen.png")]}

bonus = pygame.image.load("mystery.png")


print(enemys["enemy1"][0])