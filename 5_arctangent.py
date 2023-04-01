import pygame
from math import *
pygame.init()
width,height = 1536,801
xpos,ypos = width/2,height/2
screen = pygame.display.set_mode((width,height))
surface = pygame.Surface((100,50),pygame.SRCALPHA)
# rotated_surface = surface

surface.fill("black")
run = True
rad=  180/pi
angle= 0
a= 0
lw =3
while run:
    screen.fill("black")
    arrowx = (cos(a)*300)+xpos
    arrowy = (sin(a)*300)+ypos
    x,y = pygame.mouse.get_pos(screen)
    dx = x-arrowx
    dy = y-arrowy
    a+=0.01
    
    if x!=0:
        angle=atan2(dy,dx)*-rad
        print(angle)
    # angle+=0.01
    A =(0,25)
    B =(70,0)
    C =(70,50)
    D =(100,25)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
    rotated_surface = pygame.transform.rotate(surface,angle)
    pygame.draw.line(surface,"white",A,D,lw)
    pygame.draw.line(surface,"white",B,D,lw)
    pygame.draw.line(surface,"white",C,D,lw)
    rect = rotated_surface.get_rect(center = (arrowx, arrowy))

    screen.blit(rotated_surface,(rect.x,rect.y))
    pygame.display.update()
pygame.quit()