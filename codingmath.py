import pygame
from Particle import *
from random import uniform
pygame.init()
width,height =1536 ,801
screen = pygame.display.set_mode((width,height))
run = True
xpos ,ypos = width/2,height/2
clock = pygame.time.Clock()
ship = particle(xpos,ypos,0,0)
thrust = vector(0,0)
angle = 0
turningleft = False
turningright = False
thrusting = False
rad= (pi/180)
angle1 = rad*0
angle2 = rad*90
angle3 = rad*-90
dis  =30 
di =60
while run:
    screen.fill("white")
    clock.tick(100)
    a =ship.position.getx()
    b =ship.position.gety()
    ex1 = (cos(angle1)*di)+ a
    ey1 = (sin(angle1)*di)+ b
    # angle1 -=speed
    # ---------------------secondpoint------------------       
    ex2 = (cos(angle2)*dis)+ a 
    ey2 = (sin(angle2)*dis)+ b
    # angle2 -=speed
    # ---------------------thirdpoint------------------       
    ex3 = (cos(angle3)*dis)+ a 
    ey3 = (sin(angle3)*dis)+ b
    # angle3 -=speed
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
    else:
        thrust.setlength(0)
    if ship.position.getx()>width:
        ship.position.setx(0)
    if ship.position.getx()<0:
        ship.position.setx(width)
    if ship.position.gety()>height:
        ship.position.sety(0)
    if ship.position.gety()<0:
        ship.position.sety(height)
    
    if turningleft:
            angle1 -=0.01 
            angle2 -=0.01 
            angle3 -=0.01 
        
    if turningright:
        angle1 +=0.01 
        angle2 +=0.01 
        angle3 +=0.01 
    ship.acclerate(thrust)
    ship.update()
    # pygame.draw.circle(screen,"black",(ship.position.getx(),ship.position.gety()),10)
    # pygame.draw.polygon(screen, "black",[(a,b), (a-100,b-50), (a-100,b+50)],2)
    pygame.draw.polygon(screen, "black",[(ex1,ey1), (ex2,ey2), (ex3,ey3)],2)
    pygame.display.update()
pygame.quit()