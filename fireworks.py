import pygame
from Particle import *
pygame.init()
width,height =1536 ,801
screen = pygame.display.set_mode((width,height))
screen.fill("white")
run = True
xpos ,ypos = width/2,height/2
clock = pygame.time.Clock()

particles = []
num = 100
# gravity = vector(0,0.1)
for i in range(num):
    particles.append(particle(xpos,height/3,uniform(2,7),uniform(1,6*pi),0.1))
while run:
    screen.fill("black")
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for i in range(num):
        p = particles[i]
        # p.acclerate(gravity)
        p.update()
        pygame.draw.circle(screen,"grey",(p.position.getx(),p.position.gety()),5)
    pygame.display.update()
pygame.quit()