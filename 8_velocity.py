import pygame
from Particle import *
pygame.init()
width,height =1536 ,801
screen = pygame.display.set_mode((width,height))
screen.fill("white")
run = True
xpos ,ypos = width/2,height/2
clock = pygame.time.Clock()
# position = vector(100,100)
# velocity =vector(0,0)
# velocity.setlength(3)
# velocity.setangle(pi/6) 
# p = particle(100,100,3,30)
particles = []
num = 1000
for i in range(num):
    particles.append(particle(xpos,ypos,uniform(0,4),uniform(0,2*pi)))
while run:
    screen.fill("black")
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # position.addto(velocity)
    # p.update()
    for i in range(num):
        p = particles[i]
        p.update()
        pygame.draw.circle(screen,"grey",(p.position.getx(),p.position.gety()),10)
    pygame.display.update()
pygame.quit()