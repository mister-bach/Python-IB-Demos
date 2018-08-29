import pygame

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Basic Window')
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    #Draw Stuff Here

    pygame.display.update()
    clock.tick(60)
pygame.quit()



