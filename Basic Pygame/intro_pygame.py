

# The Game Loop
#
# This is the most basic of all Pygame programs
# which just creates a basic window. This window
# is 640x480 and will run until the event QUIT 
# occurs.  
################################################
# import pygame
#
# screen = pygame.display.set_mode((640, 480))
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()
################################################


# Drawing a rectangle
#
# Shapes are drawn by doing 'pygame.draw.(name)'
# where the (name) is the function name of the 
# shape you want to draw. Most shapes have 
# have different parameters, but they all start
# with 'screen, (R, G, B).' In the case of a
# rectangle the third parameter is a made of 
# two pairs which represent coordinates:
# ((x1, y1), (x2, y2))

# You can find a listing of all the functions here:
# https://www.pygame.org/docs/ref/draw.html
################################################
# import pygame
#
# screen = pygame.display.set_mode((640, 480))
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     pygame.draw.rect(screen, (0, 128, 128), ((50, 50), (100, 100)))
#     pygame.display.update()
# pygame.quit()
################################################


# Drawing a circle
#
# Shapes are drawn by doing 'pygame.draw.(name)'
# where the (name) is the function name of the 
# shape you want to draw. Most shapes have 
# have different parameters, but they all start
# with 'screen, (R, G, B).' with a circle the last
# two parameters are a point (x, y) which is the 
# center of the circle and the last is the radius.

# You can find a listing of all functions here:
# https://www.pygame.org/docs/ref/draw.html
################################################

# import pygame
#
# screen = pygame.display.set_mode((640, 480))
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     pygame.draw.circle(screen, (0, 128, 128), (250, 250), 50)
#     pygame.display.update()
# pygame.quit()
################################################



# Changing Colors
# The % keeps us from using RGB values over 255
################################################

# import pygame
#
# screen = pygame.display.set_mode((640, 480))
#
# running = True
# r = 0
# g = 150
# b = 100
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     pygame.draw.circle(screen, (r % 255, g % 255, b % 255), (250, 250), 50)
#     pygame.display.update()
#     r = r + 1
#     g = g + 1
#     b = b + 1
# pygame.quit()
################################################


# Game loop speed
# The clock makes sure we keep a consistent
# framerate
################################################

# import pygame
#
# screen = pygame.display.set_mode((640, 480))
# clock = pygame.time.Clock()
# running = True
#
# r = 0
# g = 150
# b = 100
#
# while running:
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     pygame.draw.circle(screen, (r % 255, g % 255, b % 255), (250, 250), 50)
#     pygame.display.update()
#     clock.tick(30)
#     r = r + 1
#     g = g + 1
#     b = b + 1
# pygame.quit()
################################################


# Moving Ball
# Just a simple moving ball
################################################

# import pygame
#
# screen = pygame.display.set_mode((640, 480))
# clock = pygame.time.Clock()
# running = True
# x = 50
# while running:
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     pygame.draw.circle(screen, (0, 150, 150), (int(x), 250), 50)
#     pygame.display.update()
#     clock.tick(30)
#     x = x + 10
# pygame.quit()
################################################


# Moving Ball and Clearing Screen
# Clearing the screen so the ball doesn't
# leave tracers after it.
################################################

# import pygame
#
# screen = pygame.display.set_mode((640, 480))
# clock = pygame.time.Clock()
# running = True
# x = 50
# while running:
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill((0, 0, 0))
#     pygame.draw.circle(screen, (0, 150, 150), (int(x), 250), 50)
#     pygame.display.flip()
#     clock.tick(60)
#     x = x + 2
# pygame.quit()
################################################


# Bouncing Ball
# Balls bounces only off the right and left
# walls
################################################

# import pygame
#
# screen = pygame.display.set_mode((640, 480))
# clock = pygame.time.Clock()
# running = True
# x = 50
# x_velocity = 2
# while running:
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill((0, 0, 0))
#     pygame.draw.circle(screen, (0, 150, 150), (int(x), 250), 50)
#     pygame.display.flip()
#     clock.tick(60)
#     x = x + x_velocity
#     if x > 590 or x < 50:
#         x_velocity = -x_velocity
#
# pygame.quit()
################################################


# Bouncing Ball all Directions
# Every direction bounce
################################################
#
# import pygame
#
# screen = pygame.display.set_mode((640, 480))
# clock = pygame.time.Clock()
# running = True
#
# x = 50
# x_velocity = 2
# y = 250
# y_velocity = 2
#
# while running:
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill((0, 0, 0))
#     pygame.draw.circle(screen, (0, 150, 150), (int(x), int(y)), 50)
#     pygame.display.flip()
#     clock.tick(60)
#     x = x + x_velocity
#     y = y + y_velocity
#     if x > 590 or x < 50:
#         x_velocity = -x_velocity
#     if y > 430 or y < 50:
#         y_velocity = -y_velocity
# pygame.quit()
################################################


