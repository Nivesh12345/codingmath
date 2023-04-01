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
p = particle(xpos,ypos,10,uniform(0,2*pi))
p.radius = 10
friction = 0.97
while run:
    screen.fill("black")
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    p.velocity.multiplyby(friction)
    p.update()
    pygame.draw.circle(screen,"grey",(p.position.getx(),p.position.gety()),p.radius)
    pygame.display.update()
pygame.quit()