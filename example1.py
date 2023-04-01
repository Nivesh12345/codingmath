import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600), 0, 32)

surface1 = pygame.Surface((200,200))
surface1.set_colorkey((0,0,0))
# surface1.set_alpha(128)
pygame.draw.circle(surface1, "white", (100,100), 100)

surface2 = pygame.Surface((100,100))
# surface2.set_colorkey((0,0,0))
# surface2.set_alpha(128)
pygame.draw.circle(surface2, (255,0,0), (50,50), 50)


screen.blit(surface2, (120,120))


RUNNING = True
i = 0
while RUNNING:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    i+=0.1
    screen.blit(surface1, (400,300))
    pygame.display.update()

pygame.quit()