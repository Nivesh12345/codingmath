import pygame
from math import *
from random import *
from Particle import *
pygame.init()
width,height =1536 ,801
screen = pygame.display.set_mode((width,height))
screen.fill("black")
run = True
xpos ,ypos = width/2,height/2
clock = pygame.time.Clock()
particleA = particle(randint(0,width),randint(0,height),randint(0,50),uniform(0,2*pi),0.8)
particleB = particle(randint(0,width),randint(0,height),randint(0,50),uniform(0,2*pi),0.8)
particleC = particle(randint(0,width),randint(0,height),randint(0,50),uniform(0,2*pi),0.8)

k =0.01
separation =100
particleA.friction =0.6
particleA.radius = 20
particleB.friction =0.6
particleB.radius = 20
particleC.friction =0.6
particleC.radius = 20

def spring(p0,p1,separatio):
    distance = p0.position.subtract(p1.position)
    distance.setlength(distance.getlength()-separatio)
    springforce = distance.multiply(k)
    p1.velocity.addto(springforce)
    p0.velocity.subtractfrom(springforce)
while run:
    screen.fill("black")
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    spring(particleA,particleB,separation)
    spring(particleB,particleC,separation)
    spring(particleC,particleA,separation)
    particleA.update()
    particleB.update()
    particleC.update()
    pygame.draw.circle(screen,"grey",(particleA.position.getx(),particleA.position.gety()),particleA.radius)
    pygame.draw.circle(screen,"grey",(particleB.position.getx(),particleB.position.gety()),particleB.radius)
    pygame.draw.circle(screen,"grey",(particleC.position.getx(),particleC.position.gety()),particleC.radius)
    pygame.draw.line(screen,"grey",(particleA.position.getx(),particleA.position.gety()),(particleB.position.getx(),particleB.position.gety()),3)
    pygame.draw.line(screen,"grey",(particleB.position.getx(),particleB.position.gety()),(particleC.position.getx(),particleC.position.gety()),3)
    pygame.draw.line(screen,"grey",(particleC.position.getx(),particleC.position.gety()),(particleA.position.getx(),particleA.position.gety()),3)
    pygame.display.update()
pygame.quit()