import pygame
from math import *
from random import uniform
pygame.init()
width,height =1536 ,801
screen = pygame.display.set_mode((width,height))
screen.fill("white")
run = True
xpos ,ypos = width/2,height/2
clock = pygame.time.Clock()
angle = 0
while(angle<2*pi):
    # print(sin(angle))
    x = angle*200
    y = (sin(angle)*-200)+ypos
    angle+=0.01
    pygame.draw.rect(screen,"black",(x,y,5,5))
while run:
    # screen.fill("white")
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # x = angle*200
    # y = (sin(angle)*-200)+ypos
    # angle+=0.01
    # pygame.draw.rect(screen,"black",(x,y,5,5))
    pygame.display.update()
pygame.quit()