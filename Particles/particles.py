import pygame
from pygame import gfxdraw
from random import random, randint

###########################################################################
#Create Point
#Defines it's own location, direction and draws itself
###########################################################################


class Point:
	def __init__(self, x, y, x_velocity, y_velocity):
		self.x_start = x
		self.y_start = y
		self.x = x
		self.y = y
		self.x_velocity = x_velocity
		self.y_velocity = y_velocity
		self.y_velocity_start = y_velocity
		self.gravity = 0.05
		self.color = pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))

	def update(self):
		self.x += self.x_velocity
		self.y += self.y_velocity

		self.y_velocity += self.gravity

		if self.x < 0 or self.x > 640 or self.y < 0 or self.y > 480:
			self.x = self.x_start
			self.y = self.y_start
			self.y_velocity = self.y_velocity_start

	def draw(self, screen):
		pygame.gfxdraw.aacircle(screen, int(self.x), int(self.y), 5, self.color)
		#screen.fill(self.color, ((self.x, self.y), (1, 1)))



###########################################################################
#Create pixel list
###########################################################################

def get_random_float(val):
	return (random() * 2 - 1) * val

width = 640
height = 480
pts = []
for i in range(500):
	pts.append(Point(int(width/2), int(height/2), get_random_float(2), get_random_float(2)))



###########################################################################
#Basic Pygame Window
###########################################################################


screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Basic Window')
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    #Draw stuff
    for pt in pts:
    	pt.draw(screen)
    	pt.update()

    pygame.display.update()
    clock.tick(60)
pygame.quit()


