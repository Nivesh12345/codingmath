import sys, pygame
from pygame.locals import *

pygame.init()
SCREEN = pygame.display.set_mode((800, 600))
CLOCK  = pygame.time.Clock()

surface = pygame.Surface((100 , 50), pygame.SRCALPHA)

surface.fill((0, 0, 0))
rotated_surface = surface
rect = surface.get_rect()
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.fill((255, 255, 255))
    angle += 1
    rotated_surface = pygame.transform.rotate(surface, angle)
    rect = rotated_surface.get_rect(center = (100, 100))
    SCREEN.blit(rotated_surface, (rect.x, rect.y))

    pygame.display.update()
    CLOCK.tick(30)
