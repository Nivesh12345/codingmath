import pygame
from Particle import *
pygame.init()
width,height =1536 ,801
screen = pygame.display.set_mode((width,height))
screen.fill("white")
run = True
xpos ,ypos = width/2,height/2
clock = pygame.time.Clock()


p = particle(100,height,10,-pi/2)
accel =vector(0.1,0.1)
while run:
    screen.fill("black")
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    p.acclerate(accel)
    p.update()
    pygame.draw.circle(screen,"grey",(p.position.getx(),p.position.gety()),10)
    pygame.display.update()
pygame.quit()