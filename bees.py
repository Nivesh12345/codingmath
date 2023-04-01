from venv import create
import pygame
from math import *
from random import *
pygame.init()
width,height =1536 ,801
screen = pygame.display.set_mode((width,height))
screen.fill("white")
run = True
xpos ,ypos = width/2,height/2
clock = pygame.time.Clock()
bees = []
numbees =1
class bee():
    def __init__(self,foo,bar) -> None:
        # print(foo,bar)
        self.anglex =uniform(0,2*pi)
        self.angley =uniform(0,2*pi)
        self.speedx = uniform(0.05,0.1)
        self.speedy = uniform(0.05,0.1)
        self.radius = 300+uniform(0,100)
    def update(self):
        x = cos(self.anglex)*self.radius
        y = sin(self.angley)*self.radius
        self.anglex+=self.speedx
        self.angley+=self.speedy
        xpos,ypos = pygame.mouse.get_pos()
        self.color = ["orange","red","yellow","green","purple"]
        self.o = randint(0,4)
        # pygame.draw.circle(screen,self.color[self.o],(xpos+x,ypos+y),2)
        pygame.draw.circle(screen,"black",(xpos+x,ypos+y),20)
for i in range(numbees):
    bees.append(bee("foo","bar"))
while run:
    screen.fill("white")
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for i in range(numbees):
        bees[i].update()
    pygame.display.update()
pygame.quit()