import pygame as pg
import random

from pygame import Surface

pg.init()

# reduced W an H to use less  memory
W = 15000  # size of space used for game world background
H = 15000  # 2nd surface over screen
HW = W / 2  # Finding center of game world
HH = H / 2
SCR_WIDTH = 1300  # view screen settings
SCR_HEIGHT = 800
sizex = int(W)
sizey = int(H)
exsize = (W, H)


class Background():
    def __init__(self):

        self.sizex = int(W)
        self.sizey = int(H)
        self.exsize = (W, H)
        self.bg2size = (W / 10, H / 10)
        self.center_pos = (HW, HH)
        self.bg = pg.Surface(exsize)
        self.bg_rect = self.bg.get_rect()
        self.bg.set_colorkey((0, 0, 0))
        self.bg.fill((0, 0, 0))
        self.bg2 = pg.image.load("gx/bg.png").convert_alpha()

        self.bg.blit(self.bg2, self.bg_rect)
        self.starmap()
        
    def starmap(self):

 

        # Drawing a grid map.
        for x in range(self.sizex):
            pg.draw.line(self.bg, (15, 20, 30), (x * 20, 0), (x * 20, self.sizey), 1)

        for y in range(self.sizey):
            pg.draw.line(self.bg, (15, 20, 30), (0, y * 20), (self.sizex, y * 20), 1)

        # Drawing Stars
        for self.stars in range(200000):
            self.starx = random.randint(10, self.sizex)
            self.stary = random.randint(10, self.sizey)
            self.star = self.starx, self.stary
            self.radius = random.randint(1, 2)
            pg.draw.circle(self.bg, pg.Color("white"), self.star, self.radius)
            pg.draw.circle(self.bg2, pg.Color("white"), self.star, self.radius)
            
        self.planets()
        
    def planets(self):
            
        p1 = pg.image.load("gx/P1.png").convert_alpha()
        p1_rect = p1.get_rect(center=(100, 6600))

        p2 = pg.image.load("gx/P2.png").convert_alpha()

        p3 = pg.image.load("gx/P3.png").convert_alpha()

        p4 = pg.image.load("gx/P4.png").convert_alpha()
        p5 = pg.image.load("gx/P5.png").convert_alpha()
        p6 = pg.image.load("gx/P6.png").convert_alpha()

        p7 = pg.image.load("gx/P7.png").convert_alpha()

        p8 = pg.image.load("gx/P8.png").convert_alpha()
        p9 = pg.image.load("gx/P9.png").convert_alpha()

        p10 = pg.image.load("gx/P10.png").convert_alpha()
        p11 = pg.image.load("gx/P11.png").convert_alpha()

        p12 = pg.image.load("gx/P12.png").convert_alpha()

        

        p2_rect = p2.get_rect(center=(1200, 10000))

        p3_rect = p3.get_rect(center=(1500, 4600))

        p4_rect = p4.get_rect(center=(2000, 13000))

        p5_rect = p5.get_rect(center=(3300, 10000))
        p6_rect = p6.get_rect(center=(4700, 8800))
        p7_rect = p7.get_rect(center=(3600, 300))

        p8_rect = p8.get_rect(center=(4200, 1800))

        p9_rect = p9.get_rect(center=(5000, 14000))

        p10_rect = p10.get_rect(center=(5200, 7100))

        p11_rect = p11.get_rect(center=(5600, 12000))

        p12_rect = p12.get_rect(center=(5800, 14400))

      

        self.bg.blit(p1, p1_rect)
        self.bg.blit(p2, p2_rect)
        self.bg.blit(p3, p3_rect)
        self.bg.blit(p4, p4_rect)

        self.bg.blit(p5, p5_rect)
        self.bg.blit(p6, p6_rect)
        self.bg.blit(p7, p7_rect)

        self.bg.blit(p8, p8_rect)
        self.bg.blit(p9, p9_rect)
        self.bg.blit(p10, p10_rect)
        self.bg.blit(p11, p11_rect)
        self.bg.blit(p12, p12_rect)
        pg.display.flip()

        return self.bg, self.bg_rect, self.bg2

    
    

