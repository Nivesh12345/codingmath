import pygame
from Particle import *
from random import uniform
pygame.init()
width,height =1536 ,801
screen = pygame.display.set_mode((width,height))
run = True
surface = pygame.Surface((100,50),pygame.SRCALPHA)
# rotated_surface = surface

surface.fill("black")
xpos ,ypos = width/2,height/2
clock = pygame.time.Clock()
ship = particle(xpos,ypos,0,0)
thrust = vector(0,0)
angle = 0
turningleft = False
turningright = False
thrusting = False
rad= (pi/180)
rad1= (180/pi)
angle1 = rad*0
angle2 = rad*90
angle3 = rad*-90
dis  =30 
di =60
angle = 0
ship.friction = 0.98
while run:
    screen.fill("black")
    clock.tick(100)
    a =ship.position.getx()
    b =ship.position.gety()
    A =(30,0)
    B =(100,25)
    C =(30,50)
    D =(0,25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_UP:
            thrusting =True
            
        
        if event.key == pygame.K_LEFT:
            turningleft =True 
        
        if event.key == pygame.K_RIGHT:
            turningright =True
    if event.type == pygame.KEYUP:
        
        if event.key == pygame.K_UP:
            thrusting = False
            
        
        if event.key == pygame.K_LEFT:
            turningleft = False 
        
        if event.key == pygame.K_RIGHT:
            turningright = False
    thrust.setangle(angle1)
    if thrusting:
        thrust.setlength(0.1)
        pygame.draw.line(surface,"white",(5,25),(30,25),3)
    else:
        thrust.setlength(0)
        pygame.draw.line(surface,"black",(5,25),(30,25),3)
    if ship.position.getx()>width:
        ship.position.setx(0)
    if ship.position.getx()<0:
        ship.position.setx(width)
    if ship.position.gety()>height:
        ship.position.sety(0)
    if ship.position.gety()<0:
        ship.position.sety(height)
    
    if turningleft:
        angle+=0.01*rad1
        angle1-=0.01
        
    if turningright:
        angle-=0.01*rad1
        angle1+=0.01
    ship.acclerate(thrust)
    ship.update()
    
    
    pygame.draw.polygon(surface,"white",[A,B,C],3)
    rotated_surface = pygame.transform.rotate(surface,angle)
    
    rect = rotated_surface.get_rect(center = (a, b))
    pygame.draw.polygon(surface,"white",[A,B,C],3)
    screen.blit(rotated_surface,(rect.x,rect.y))
    pygame.display.update()
pygame.quit()