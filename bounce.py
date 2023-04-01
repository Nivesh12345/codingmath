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
p = particle(xpos,ypos,5,uniform(0,2*pi),0.1)
p.radius = 40
p.bounce = -0.9
while run:
    screen.fill("black")
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if p.position.getx()+p.radius>width:
        p.position.setx(width-p.radius)
        p.velocity.setx(p.velocity.getx()*p.bounce)
    if p.position.getx()-p.radius<0:
        p.position.setx(p.radius)
        p.velocity.setx(p.velocity.getx()*p.bounce)
    if p.position.gety()+p.radius>height:
        p.position.sety(height-p.radius)
        p.velocity.sety(p.velocity.gety()*p.bounce)
    if p.position.gety()-p.radius<0:
        p.position.sety(p.radius)
        p.velocity.sety(p.velocity.gety()*p.bounce)
    p.update()
    pygame.draw.circle(screen,"grey",(p.position.getx(),p.position.gety()),p.radius)
    pygame.display.update()
pygame.quit()