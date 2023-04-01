import pygame
from random import uniform
pygame.init()
width,height =1536 ,801
screen = pygame.display.set_mode((width,height))
screen.fill("white")
run = True
xpos ,ypos = width/2,height/2
clock = pygame.time.Clock()
a = xpos
b = ypos
angle =0
for i in range(100):
    pygame.draw.line(screen,"black",(uniform(0,width),uniform(0,height)),(uniform(0,width),uniform(0,height)))
while run:
    # screen.fill("white")
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    
    pygame.display.update()
pygame.quit()