
import pygame as pg
import math
from math import tan, copysign
from math import pi, hypot, cos, sin, atan2, degrees, radians
from pygame.math import Vector2
from constants import Constants as con
class Bullet:
    def __init__(self, pos, direction):
        self.x, self.y = pos
        self.pos = self.x, self.y
        self.dir = direction
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
            angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        self.bullet = pg.Surface((7, 2)).convert_alpha()
        self.bullet_rect = self.bullet.get_rect(center = self.pos)
        self.bullet.fill((255, 0, 255))
        self.bullet = pg.transform.rotate(self.bullet, angle)
        self.speed = 20
        self.update()
    def update(self):  
        self.pos = (self.pos[0]+self.dir[0]*self.speed, 
                    self.pos[1]+self.dir[1]*self.speed)

    def draw(self, surf):
        bullet_rect = self.bullet.get_rect(center = self.pos)
        con.screen.blit(self.bullet, bullet_rect)
        
class Projectile:
    def __init__(self, pos, direction):
        self.x, self.y = pos
        self.pos = self.x, self.y

        self.dir = direction
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
            angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        self.image = pg.Surface((8, 8))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pg.draw.circle(self.image, pg.Color("red"), (8, 1), 5)
##        self.projectile = pg.Surface((10, 6)).convert_alpha()
##        self.rect = self.image.get_rect(center = self.pos)
##        self.projectile.fill((255, 0, 0))
        self.image = pg.transform.rotate(self.image, angle)
        self.speed = 5
        self.update()
    def update(self):
        self.pos = (self.pos[0]+self.dir[0]*self.speed, 
                    self.pos[1]+self.dir[1]*self.speed)

    def draw(self, surf):
        self.rect = self.image.get_rect(center = self.pos)
        con.screen.blit(self.image, self.rect)
        

