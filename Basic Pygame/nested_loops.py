# Colored bars
###############################################

import pygame

width = 600
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    #############################################
    for i in range(0, 20):
        for j in range(0, 20):
            pygame.draw.rect(screen,
                            (0, (i * 10), 100),
                            (i * 30, j * 30, 30, 30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
###############################################