import pygame

ship = pygame.image.load("ship.png")
small_ship = pygame.transform.scale(ship,(25, 30))
enemys = {"enemy1":[pygame.transform.scale(pygame.image.load ("enemy1_1.png"),(30,30)),
                    pygame.transform.scale(pygame.image.load ("enemy1_2.png"),(30,30)),
            ],
        
        "enemy2": [  pygame.transform.scale(pygame.image.load ("enemy2_1.png"),(40,40)),
                      pygame.transform.scale(pygame.image.load ("enemy2_2.png"),(40,40)),
                     ],

        "enemy3":    [pygame.transform.scale(pygame.image.load ("enemy3_1.png"),(44,44)),
                      pygame.transform.scale(pygame.image.load ("enemy3_2.png"),(44,44)),]
                     }

bonus = pygame.image.load("mystery.png")

laser = pygame.image.load("laser.png")


