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
p = particle(xpos,ypos,3,uniform(1,2*pi))
p.radius =20
while run:
    screen.fill("black")
    clock.tick(60)
    if p.position.getx()-p.radius>width:
        p.position.setx(-p.radius)
    if p.position.getx()+p.radius<0:
        p.position.setx(width+p.radius)
    if p.position.gety()-p.radius>height:
        p.position.sety(-p.radius)
    if p.position.gety()+p.radius<0:
        p.position.sety(height+p.radius)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    p.update()
    pygame.draw.circle(screen,"grey",(p.position.getx(),p.position.gety()),p.radius)
    
    pygame.display.update()
pygame.quit()