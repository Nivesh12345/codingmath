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
springpoint = vector(xpos,ypos)
weight=  particle(uniform(1,width),uniform(1,height),50,uniform(0,2*pi),0.5)
k =0.01+uniform(0,0.1)
weight.radius = 20
springlength = 100
weight.friction =0.1
while run:
    screen.fill("black")
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    x,y = pygame.mouse.get_pos()
    springpoint.setx(x)
    springpoint.sety(y)
    distance = springpoint.subtract(weight.position)
    distance.setlength(distance.getlength()-springlength)
    springforce = distance.multiply(k)
    weight.velocity.addto(springforce)
    weight.update()
    pygame.draw.circle(screen,"grey",(weight.position.getx(),weight.position.gety()),weight.radius)
    pygame.draw.circle(screen,"grey",(springpoint.getx(),springpoint.gety()),4)
    pygame.draw.line(screen,"grey",(springpoint.getx(),springpoint.gety()),(weight.position.getx(),weight.position.gety()),3)
    pygame.display.update()
pygame.quit()