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

        p13 = pg.image.load("gx/P13.png").convert_alpha()
        p14 = pg.image.load("gx/P14.png").convert_alpha()

        p15 = pg.image.load("gx/P15.png").convert_alpha()

        p16 = pg.image.load("gx/P16.png").convert_alpha()
        p17 = pg.image.load("gx/P17.png").convert_alpha()
        p18 = pg.image.load("gx/P18.png").convert_alpha()

        p19 = pg.image.load("gx/P19.png").convert_alpha()

        p20 = pg.image.load("gx/P20.png").convert_alpha()
        p21 = pg.image.load("gx/P21.png").convert_alpha()

        p22 = pg.image.load("gx/P22.png").convert_alpha()

        p23 = pg.image.load("gx/P23.png").convert_alpha()
        p24 = pg.image.load("gx/P24.png").convert_alpha()
        p25 = pg.image.load("gx/P25.png").convert_alpha()

        p26 = pg.image.load("gx/P26.png").convert_alpha()
        p27 = pg.image.load("gx/P27.png").convert_alpha()

        p28 = pg.image.load("gx/P28.png").convert_alpha()
        p29 = pg.image.load("gx/P29.png").convert_alpha()
        p30 = pg.image.load("gx/P30.png").convert_alpha()
        p31 = pg.image.load("gx/P31.png").convert_alpha()
        p32 = pg.image.load("gx/P32.png").convert_alpha()

        p33 = pg.image.load("gx/P33.png").convert_alpha()

        p34 = pg.image.load("gx/P34.png").convert_alpha()
        p35 = pg.image.load("gx/P35.png").convert_alpha()
        p36 = pg.image.load("gx/P36.png").convert_alpha()

        p37 = pg.image.load("gx/P37.png").convert_alpha()

        p38 = pg.image.load("gx/P38.png").convert_alpha()
        p39 = pg.image.load("gx/P39.png").convert_alpha()

        p40 = pg.image.load("gx/P40.png").convert_alpha()

        p41 = pg.image.load("gx/P41.png").convert_alpha()
        p42 = pg.image.load("gx/P42.png").convert_alpha()
        p43 = pg.image.load("gx/P43.png").convert_alpha()

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

        p13_rect = p13.get_rect(center=(6200, 6000))

        p14_rect = p14.get_rect(center=(6400, 9600))

        p15_rect = p15.get_rect(center=(6600, 11000))

        p16_rect = p16.get_rect(center=(6800, 3500))
        p17_rect = p17.get_rect(center=(7000, 13000))
        p18_rect = p18.get_rect(center=(7200, 8000))

        p19_rect = p19.get_rect(center=(7500, 9000))

        p20_rect = p20.get_rect(center=(7800, 800))

        p21_rect = p21.get_rect(center=(8200, 10000))

        p22_rect = p22.get_rect(center=(8400, 500))

        p23_rect = p23.get_rect(center=(8600, 9000))
        p24_rect = p24.get_rect(center=(8800, 12300))
        p25_rect = p25.get_rect(center=(9200, 13000))
        p26_rect = p26.get_rect(center=(9600, 1800))

        p27_rect = p27.get_rect(center=(10000, 10000))

        p28_rect = p28.get_rect(center=(10500, 800))

        p29_rect = p29.get_rect(center=(11000, 1200))

        p30_rect = p30.get_rect(center=(11200, 2000))

        p31_rect = p31.get_rect(center=(11400, 4000))

        p32_rect = p32.get_rect(center=(12000, 4500))

        p33_rect = p33.get_rect(center=(12500, 5600))

        p34_rect = p34.get_rect(center=(13000, 6500))
        p35_rect = p35.get_rect(center=(13500, 8500))
        p36_rect = p36.get_rect(center=(14200, 12000))

        p37_rect = p37.get_rect(center=(5500, 9000))

        p38_rect = p38.get_rect(center=(9000, 3200))

        p39_rect = p39.get_rect(center=(4400, 7000))

        p40_rect = p40.get_rect(center=(7100, 9500))

        p41_rect = p41.get_rect(center=(8200, 3900))
        p42_rect = p42.get_rect(center=(8900, 500))
        p43_rect = p43.get_rect(center=(8800, 7000))
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
        self.bg.blit(p13, p13_rect)
        self.bg.blit(p14, p14_rect)
        self.bg.blit(p15, p15_rect)
        self.bg.blit(p16, p16_rect)
        self.bg.blit(p17, p17_rect)
        self.bg.blit(p18, p18_rect)
        self.bg.blit(p19, p19_rect)
        self.bg.blit(p20, p20_rect)
        self.bg.blit(p21, p21_rect)
        self.bg.blit(p22, p22_rect)
        self.bg.blit(p23, p23_rect)
        self.bg.blit(p24, p24_rect)
        self.bg.blit(p25, p25_rect)

        self.bg.blit(p26, p26_rect)
        self.bg.blit(p27, p27_rect)
        self.bg.blit(p28, p28_rect)
        self.bg.blit(p29, p29_rect)
        self.bg.blit(p30, p30_rect)
        self.bg.blit(p31, p31_rect)
        self.bg.blit(p32, p32_rect)
        self.bg.blit(p33, p33_rect)
        self.bg.blit(p34, p34_rect)
        self.bg.blit(p35, p35_rect)
        self.bg.blit(p36, p36_rect)
        self.bg.blit(p37, p37_rect)
        self.bg.blit(p38, p38_rect)
        self.bg.blit(p39, p39_rect)
        self.bg.blit(p40, p40_rect)
        self.bg.blit(p41, p41_rect)
        self.bg.blit(p42, p42_rect)
        self.bg.blit(p43, p43_rect)

        pg.display.flip()

        return self.bg, self.bg_rect, self.bg2

    
    

