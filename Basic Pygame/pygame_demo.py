
import pygame

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

#Game Loop
running = True
red = 0
x = 300
x_vel = 3
y = 300
from random import randint
lst_circles = []
lst_colors = []
for i in range(0, 100):
    lst_circles.append(((randint(0, 600), (randint(0, 600)))))
    lst_colors.append((randint(0, 255), randint(0, 255), randint(0, 255)))
#Loops Forever
while running:
    #Checks for things happening (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for i in range(0, 100):
        pygame.draw.circle(screen,
                           lst_colors[i],
                           lst_circles[i],
                           50)

    x = x + x_vel
    if x > 550 or x < 50:
        x_vel = -x_vel


    clock.tick(30)
    pygame.display.update()


print(pygame.QUIT)
pygame.quit()

