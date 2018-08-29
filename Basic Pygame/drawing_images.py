import pygame

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Drawing Images')
clock = pygame.time.Clock()

ball_img = pygame.image.load('ball.png')
ball_img.set_colorkey((255, 255, 255))
ball_img = ball_img.convert_alpha()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    screen.blit(ball_img, (300, 300))
    pygame.display.update()
    clock.tick(60)
pygame.quit()
