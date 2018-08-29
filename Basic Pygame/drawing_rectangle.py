import pygame

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Drawing Rectangles')

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), (50, 50, 25, 25))
    pygame.display.update()
    clock.tick(60)
pygame.quit()
