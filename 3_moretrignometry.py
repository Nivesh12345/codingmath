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
offset = 0.5
# offset = 50
# offset = height*0.4
speed= 0.1
angle= 0
basealpha =0.5
# baseradius =100
while run:
    screen.fill("white")
    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # alpha= (sin(angle)*offset)+basealpha
    # y= (sin(angle)*offset)+ypos
    # radius= (sin(angle)*offset)+baseradius


    # pygame.draw.circle(screen,((0,0,0,100)),(xpos,ypos),100)  solution in example1.py
    # pygame.draw.circle(screen,"black",(xpos,y),50)
    # pygame.draw.circle(screen,"black",(xpos,ypos),radius)
    angle+=speed
    pygame.display.update()
pygame.quit()