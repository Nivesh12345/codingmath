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
sun =particle(xpos-200,ypos,0,0)
sun1 =particle(xpos+200,ypos,0,0)
mainsun =particle(xpos,ypos,0,0)

planets =[]
planets1 =[]
num = 3000
for i in range(num):

    planet =particle(uniform(300,width-300),uniform(200,height-200),uniform(-20,20),-pi/2)
    planet1 =particle(uniform(300,width-300),uniform(200,height-200),uniform(-20,20),pi/2)
    planets.append(planet)
    planets1.append(planet1)
    planet.mass = 20000
    planet1.mass = 50000
sun.mass = 40000
sun1.mass = 40000
mainsun.mass = 40000
while run:
    screen.fill("black")
    clock.tick(60)
    # sun.mass+=10000
    # sun1.mass+=10000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for i in range(num):
        planet = planets[i]
        planet1 = planets1[i]
        planet.gravityto(planet1)
        planet1.gravityto(planet)
        planet.update()
        planet1.update()
        pygame.draw.circle(screen,"grey",(planet.position.getx(),planet.position.gety()),3)
        pygame.draw.circle(screen,"grey",(planet1.position.getx(),planet1.position.gety()),3)
        # pygame.draw.rect(screen,"grey",(planet.position.getx(),planet.position.gety(),1,1))
        # pygame.draw.rect(screen,"grey",(planet1.position.getx(),planet1.position.gety(),1,1))
    # sun.gravityto(sun1)
    # sun1.gravityto(sun)
    # sun.update()
    # sun1.update()
    # pygame.draw.circle(screen,"yellow",(sun.position.getx(),sun.position.gety()),20)
    # pygame.draw.circle(screen,"yellow",(sun1.position.getx(),sun1.position.gety()),20)
    pygame.display.update()
pygame.quit()