import pygame
from Particle import *
pygame.init()
width,height =1536 ,801
screen = pygame.display.set_mode((width,height))
screen.fill("white")
run = True
xpos ,ypos = width/2,height/2
clock = pygame.time.Clock()
color = ["orange","red","yellow","green","purple"]
particles = []
particles1 = []
num = 1000
for i in range(num):
    x,y = pygame.mouse.get_pos()
    p =particle(x,y,uniform(0,22),-pi/2+(uniform(-0.2,0.4)),0.1)
    p1 =particle(x,y,uniform(0,22),-pi+(uniform(-0.2,0.4)),0.1)
    p.radius = uniform(0,12)
    p1.radius = uniform(0,12)
    particles.append(p)
    particles1.append(p1)
def removeDeadParticles():
    for i in range(len(particles)-1,0,-1):
        p = particles[i]
        if(p.position.getx()-p.radius>width or p.position.getx()+p.radius<0 or p.position.gety()-p.radius>height or p.position.gety()+p.radius<0):
            particles.pop(i)
        

while run:
    screen.fill("black")
    clock.tick(60)
    print(len(particles))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    x,y = pygame.mouse.get_pos()
    for i in range(len(particles)):
        p = particles[i]
        p.update()

        o = randint(0,4)
        pygame.draw.circle(screen,color[o],(p.position.getx(),p.position.gety()),p.radius)
        p1 = particles1[i]
        p1.update()

        o = randint(0,4)
        pygame.draw.circle(screen,color[o],(p1.position.getx(),p1.position.gety()),p1.radius)
        if p.position.gety()-p.radius>height:
            p.position.setx(xpos)
            p.position.sety(ypos)
            p.velocity.setlength(uniform(0,30))
            p.velocity.setangle((uniform(0,2*pi)))
        if p1.position.gety()-p1.radius>height:
            p1.position.setx(x)
            p1.position.sety(y)
            p1.velocity.setlength(uniform(0,30))
            p1.velocity.setangle((uniform(0,2*pi)))
    # removeDeadParticles()
    pygame.display.update()
pygame.quit()