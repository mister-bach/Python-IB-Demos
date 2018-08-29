import pygame
from random import random

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Drawing Rectangles")

clock = pygame.time.Clock()

my_circle_center = []
my_circle_radius = []
my_colors = []
my_velocity = []

num_circles = 10

for i in range(0, num_circles):
    my_circle_center.append((200 + i * 25, 230))
    my_circle_radius.append(10)
    my_colors.append((0, 255, 0))
    my_velocity.append((random() * 2 - 1, random() * 2 - 1))

print(my_velocity)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    for i in range(0, num_circles):
        x, y = my_circle_center[i]
        pygame.draw.circle(screen, my_colors[i],(int(x), int(y)), my_circle_radius[i], 1)
        x_velocity, y_velocity = my_velocity[i]
        x += x_velocity
        y += y_velocity
        my_circle_center[i] = (x, y)

    pygame.display.update()
    clock.tick(60)
pygame.quit()

