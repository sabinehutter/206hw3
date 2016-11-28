from pygame import *
from pygame.sprite import *
import pygame
import random, time
import os, sys
from pygame.locals import *

Width = 800
Height = 600


DELAY = 1000;
#creating initial colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
pink = (255, 153, 204)

pattyspeed = 10


# paused = False
# mute = False

height_of_screen = 800
x_position = 0
y_position = 0

clock = pygame.time.Clock()

# pygame.display.set_caption("Sabine's Hamburger Stacker Game")
# pygame.display.update()	

class Patty(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("beef.patty.bmp").convert()
		self.rect = self.image.get_react()

	def move(self, action):
		if action == "dropping":
			self.react.y += pattyspeed


class Cheese(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("cheese.bmp").convert()
		self.rect = self.image.get_rect()

class Tomato(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("tomato.bmp").convert()
		self.rect = self.image.get_rect()

class Bun(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("bun.bmp").convert()
		self.rect = self.image.get_rect()

	def move(self, key):
		x_move = 0;
		y_move = 0;

		if (key == K_RIGHT):
			x_move = self.x_dist
		elif (key == K_LEFT):
			x_move = -self.x_dist
		elif (key == K_UP):
			y_move = -self.y_dist
		elif (key == K_DOWN):
			y_move = self.y_dist

		self.rect.move_ip(x_move, y_move);



init()

gameDisplay = display.set_mode((Width, Height))
display.set_caption("Sabine's Pygame Hamburger Game")

f = font.Font(None, 25)

bun = Bun()

sprites = RenderPlain(bun)



gameExit = False
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	pygame.display.update()
