import pygame

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Drawing Rectangles")

clock = pygame.time.Clock()

my_circle_center = []
my_circle_radius = []
my_colors = []

num_circles = 10

for i in range(0, num_circles):
    my_circle_center.append((200 + i * 25, 200))
    my_circle_radius.append(10)
    my_colors.append((0, 100, 250))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    for i in range(0, num_circles):
        pygame.draw.circle(screen, my_colors[i], my_circle_center[i], my_circle_radius[i], 1)

    pygame.display.update()
    clock.tick(60)
pygame.quit()

