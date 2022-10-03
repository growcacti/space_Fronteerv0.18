import pygame as pg
import math
from math import tan, copysign
from math import pi, hypot, cos, sin, atan2, degrees, radians
from pygame.math import Vector2
from constants import Constants
import get_info
class Player:
    def __init__(
        self, image, x, y, angle=0.0, length=4, max_rotation=10, max_acceleration=5.0):
        self.orig_image = image
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = angle
        self.length = length
        self.max_acceleration = 250
        self.max_rotation = max_rotation
        self.max_velocity = 820
        self.thrust = 500
        self.sim_inertia = 2  # iner
        self.font = pg.font.Font(None, 18)
        self.acceleration = 0.0
        self.rotation = 0.0
        self.camera = Vector2(0, 0)  # Assigned the camera as an attribute.
        self.direction = Vector2(0, 0)
        self.mask = pg.mask.from_surface(self.image)
    def update(self, dt):
        con = Constants
        self.velocity += (self.acceleration * dt, 0)
        self.velocity.x = max(
            -self.max_velocity, min(self.velocity.x, self.max_velocity)
        )

        if self.rotation:
            turning_radius = self.length / tan(radians(self.rotation))
            angular_velocity = self.velocity.x / turning_radius / 2
        else:
            angular_velocity = 0

        vel = self.velocity.rotate(-self.angle) * dt
        self.position += vel
        self.camera += vel  # Update the camera position as well.
        # If you use the rect as the blit position, you should update it, too.
        self.rect.center = self.position
        self.angle += degrees(angular_velocity) * dt
       
        self.image = pg.transform.rotozoom(self.orig_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
        
        #self.direction = self.angle
        self.direction = pg.Vector2(1, 0).rotate(-self.angle)
        pg.display.set_caption("Space Fronteerer")
 
        text1 = self.font.render("position: " + str(self.position), True, con.WHITE)
       
        con.screen.blit(text1, (con.WIDTH - 200, con.HEIGHT - 750))
    
        origin = (650, 400)
        destination = self.rect.center
        svp = math.sqrt (vel[0] ** 2 + vel[1]**2) * 671000000
        sp = abs(svp) // 100000
        
        distance, angle, x_ref, y_ref, op_ang, project =  get_info.info(origin, destination)
        dist = distance // 1
        show_angle = self.angle % 360
      
                
        projected = project[0] // 1, project[1] // 1
        text2 = self.font.render("Distance from Start: " + str(dist), True, con.WHITE)
        con.screen.blit(text2, (con.WIDTH - 200, con.HEIGHT - 780))
        text3 = self.font.render("Angle " + str(show_angle), True, con.WHITE)
        con.screen.blit(text3, (con.WIDTH - 200, con.HEIGHT - 770))
        text4 = self.font.render("Projection" + str(projected), True, con.WHITE)
        con.screen.blit(text4, (con.WIDTH - 300, con.HEIGHT - 790))
        text5 = self.font.render("MPH " + str(sp), True, con.WHITE)
        con.screen.blit(text5, (con.WIDTH - 200, con.HEIGHT - 760))
        self.project = project
        self.distance = distance
    
    
