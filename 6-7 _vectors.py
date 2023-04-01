from Particle import *
import pygame
pygame.init()
width,height =1536 ,801
screen = pygame.display.set_mode((width,height))
screen.fill("white")
run = True
xpos ,ypos = width/2,height/2
clock = pygame.time.Clock()
rad = -pi/180
v1 = vector(xpos,ypos)

# p = particle(xpos,ypos,10,)

v2 = vector(0,0)
v2.setlength(10)
v2.setangle(90*rad)
v3 = vector(0,0)
v3.setlength(10)
v3.setangle(-90*rad)




# v2.setangle(-pi/2)

while run:
    screen.fill("white")
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    v1.addto(v2)
   
    pygame.draw.circle(screen,"black",(v1.getx(),v1.gety()),10)
    pygame.display.update()
pygame.quit()