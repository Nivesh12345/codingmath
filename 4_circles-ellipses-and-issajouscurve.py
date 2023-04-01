import pygame
from math import *
from random import uniform
pygame.init()
width,height =1536 ,801
screen = pygame.display.set_mode((width,height))
screen.fill("white")
run = True
xpos ,ypos = width/2,height/2
clock = pygame.time.Clock()

# speed= 0.1
# angle= 0
# -----forcircle---
# radius =200
# -------forellipse----
xradius =200
yradius =200
# ---------forlissajouscurve---------
xangle = 0
yangle = 0
xspeed =0.1
yspeed =0.131
while run:
    # screen.fill("white")
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # ----------------circle------------
    # x= (cos(angle)*radius)+xpos
    # y= (sin(angle)*radius)+ypos
    # angle+=speed
    # ----------------ellipse------------
    x= (cos(xangle)*xradius)+xpos
    y= (sin(yangle)*yradius)+ypos
    xangle+=xspeed
    yangle+=yspeed
    # ---------forlissajouscurve---------

    
    pygame.draw.circle(screen,"black",(x,y),10)
    
    pygame.display.update()
pygame.quit()