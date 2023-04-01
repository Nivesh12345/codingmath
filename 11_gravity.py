import pygame
from math import *
from random import uniform
from Particle import *
pygame.init()
width,height =1536 ,801
screen = pygame.display.set_mode((width,height))
screen.fill("black")
run = True
xpos ,ypos = width/2,height/2
clock = pygame.time.Clock()
sun =particle(xpos,ypos,0,0)

planet =particle(xpos+200,ypos,10,-pi/2)

sun.mass = 40000
while run:
    screen.fill("black")
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    planet.gravityto(sun)
    planet.update()
    pygame.draw.circle(screen,"yellow",(sun.position.getx(),sun.position.gety()),20)
    pygame.draw.circle(screen,"grey",(planet.position.getx(),planet.position.gety()),10)
    pygame.display.update()
pygame.quit()