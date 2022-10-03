import pygame as pg
import random
import sys
import math
from math import tan, copysign
from math import pi, hypot, cos, sin, atan2, degrees, radians
from pygame.math import Vector2
import bgp
import get_info
import comet
from player import Player
from nme import Nme
from bullets import *

from constants import Constants
pg.init()



con = Constants
screen = con.screen
        
def main():

        pg.init()
        bg, bg_rect, bg2 = bgp.background()
        clock = pg.time.Clock()
        ticks = 60
        fps= ticks
        exit = False
        font = pg.font.Font(None, 18)
        ship = pg.image.load("gx/SHIP888.png").convert_alpha()
        ship2 = pg.image.load("gx/ship91.png").convert_alpha()
        ship3 = pg.image.load("gx/nmefleet.png").convert_alpha()
        player = Player(ship, *con.screen.get_rect().center)
        comet_img = pg.image.load("gx/comet.png").convert_alpha()
        comet1 = comet.Comet(comet_img, (600), (200))  
      
        nme = Nme(ship2, (7000), (5000))
        nme2 = Nme(ship3, (3500), (3200))
        nme2nmedist = Vector2(50, 50)
        run = True
        surf = pg.Surface((3, 3))
        surf.set_colorkey((0,0,0))
        surfcomet = pg.Surface((4, 5))
        surfcomet.set_colorkey((0,0,0))
        con.screen.set_colorkey((0,0,0))
        projectiles = []
        bullets = [] 
        
        bullet = Bullet(player.position, player.direction)
        projectile = Projectile(player.position, player.direction)
        hit_count = 0
        
        while not exit:
            pos = pg.Vector2(player.position)
            ang = player.angle
            con.screen.fill(0)
            text8 = font.render("NME position: " + str(nme.position), True, con.WHITE)
       
            con.screen.blit(text8, (con.WIDTH - 1100, con.HEIGHT - 680))
##         
            bg.set_colorkey((0, 0, 0))
            bg2.set_colorkey((0, 0, 0)) 
            dt = clock.tick(fps) / 1000
           

         
            v1 = pg.math.Vector2(player.position)
            v2 = pg.math.Vector2(nme.position)
            v3 = pg.math.Vector2(nme2.position)
            off1 = pg.math.Vector2(-71, -70)
            pcam = pg.Vector2(player.camera)
            pppos = pg.Vector2(player.position - (player.rect.width /2, player.rect.height / 2)- pcam)
            ppbullet = pg.Vector2(player.position - (player.rect.width / 64, player.rect.height / 64)- pcam)
            nmebullet = pg.Vector2(nme.rect.center - pcam - off1)
            pdir = player.direction
            ndir = nme.direction
             # Event queue
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
                        return

                elif event.type == pg.QUIT:
                        pg.quit()
                        sys.exit()
                        return    
                elif event.type == pg.MOUSEWHEEL:
                    if event.y == 1:
                        player.rotation -= 120 * dt
                    elif event.y == -1:
                        player.rotation += 120 * dt
                elif pg.mouse.get_pressed()[2]:
                    bullets.append(Bullet(ppbullet, pdir))
                    for bullet in bullets:
                        bullet.draw(con.screen) 

                for bullet in bullets[:]:
                    bullet.update()
                    if not bg.get_rect().collidepoint(bullet.pos):
                        bullets.remove(bullet)
             
                      # User input & Controls
            pressed = pg.key.get_pressed()
            pressed2 = pg.mouse.get_pressed(num_buttons=5)
            if pressed[pg.K_UP] or pg.mouse.get_pressed()[0]:
                if player.velocity.x < 0:
                    player.acceleration = player.thrust
                else:
                    player.acceleration += 890 * dt
            elif pressed[pg.K_DOWN] or pg.mouse.get_pressed()[1]:
                if player.velocity.x > 0:
                    player.acceleration = -player.thrust
                else:
                    player.acceleration -= 1 * dt

            
               
            elif pressed[pg.K_h]:
                if abs(player.velocity.x) > dt * player.thrust:
                    player.acceleration = -copysign(
                        player.thrust, player.velocity.x
                    )
                else:
                    player.acceleration = -player.velocity.x / dt
            else:
                if abs(player.velocity.x) > dt * player.sim_inertia:
                    player.acceleration = -copysign(
                        player.sim_inertia, player.velocity.x
                    )
                else:
                    if dt != 0:
                        player.acceleration = -player.velocity.x / dt
            player.acceleration = max(
                -player.max_acceleration,
                min(player.acceleration, player.max_acceleration),
            )

            if pressed[pg.K_RIGHT] or event.type == pg.MOUSEWHEEL:
                player.rotation -= 20 * dt
                
            elif pressed[pg.K_LEFT] or pg.mouse.get_pressed(num_buttons=5)[4]:
                player.rotation += 20 * dt
               
            else:
                player.rotation = 0
            player.rotation = max(
                -player.max_rotation,
                min(player.rotation, player.max_rotation),
            )

        

 
            if pressed[pg.K_SPACE]:
                 projectiles.append(Projectile(ppbullet, pdir))
                 for projectile in projectiles:
                     projectile.draw(con.screen) 

            for projectile in projectiles[:]:
                projectile.update()
                if not bg.get_rect().collidepoint(projectile.pos):
                    projectiles.remove(projectile)
                           
            for projectile in projectiles:
                projectile.draw(con.screen) 
            
            
            player.update(dt)
            nme.update(dt)
            nme2.update(dt)
            comet1.update(dt)
            
                        #Variables created to shorten equation for final blit below personal preference to reduce one time long equations.
            # I think the equation might be used again with slight difference
            
            # With the camera being the same velocity set in the Player Class, now is the time to blit the math to the con.screen to
            # break free of the con.screen boundary, follow the player position always

            con.screen.blit(comet1.image, comet1.position - player.camera)
            bg.blit(surfcomet, comet1.rect)   
            con.screen.blit(bg2, bg_rect)     
            con.screen.blit(bg, -player.camera)
            con.screen.blit(player.image, pppos)
                  
         




            # the nme and other creations need the camera subtracted from for them to move independently
            # this took a long time to understand even after reading about it
            con.screen.blit(nme.image, nme.position - player.camera)
            con.screen.blit(nme2.image, nme2.position - player.camera)
            bg.blit(surf, nme.rect)
            bg.blit(surf, nme2.rect)
           
            nme.move_towards_player(pos, ang)
            nme2.move_towards_player(pos, ang) 
           
           
             

                          
            player_hits = 0
            vv = v1.distance_to(v2)
            vvv = v1.distance_to(v3)
            
##            def intersects_with():
##            
##                max_x = player.position[0]+ player.image.get_con.WIDTH()
##                max_y = player.position[1]+ player.image.get_con.HEIGHT()
##                
##                nmemax_x = nme.position[0] + nme.image.get_con.WIDTH()
##                nmemax_y = nme.position[1] + nme.image.get_con.HEIGHT()
##                if max_x < player.position[0]:
##                    
##                    return False
##
##                if max_y < player.position[1]:
##                    
##                    return False
##
##                if player.position[0] > nmemax_x:
##                    
##                    return False
##
##                if player.position[1] > nmemax_y:
##                    return False
##                if True:
##                 
##                    return True
##
##
      
           
            if v1.distance_to(v2) <= 20:
                 hit_count += 1
                 print("nmehit:")     
            if v1.distance_to(v2) < 500 and v1.distance_to(v2) > 100:
                 projectiles.append(Projectile(nmebullet, pdir))
                 for projectile in projectiles:
                     projectile.draw(con.screen) 

                                
               
                            
            if v1.distance_to(v3) <= 20:
                 hit_count += 1
                 print("nme2hit:")     

            if v2.distance_to(v3) <= 0:

                 print("hitnme")
                 
            text9 = font.render("NME dist: " + str(vv), True, con.WHITE)
       
            con.screen.blit(text9, (con.WIDTH - 1100, con.HEIGHT - 700))
            text10 = font.render("NME dist: " + str(vvv), True, con.WHITE)
       
            con.screen.blit(text10, (con.WIDTH - 1100, con.HEIGHT - 720))
            text11 = font.render("NME pos: " + str(v2), True, con.WHITE)
       
            con.screen.blit(text11, (con.WIDTH - 1100, con.HEIGHT - 740))
            

            text12 = font.render("hits" + str(hit_count), True, con.WHITE)
                    
            con.screen.blit(text12, (con.WIDTH - 200, con.HEIGHT - 800))
            
                   
             
          
            pg.display.flip()

       


        pg.quit()


if __name__ == "__main__":
    main()
    

