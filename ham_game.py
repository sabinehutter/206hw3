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
			if self.rect.y < Height:
				self.rect.x = random.randint(1, WIDTH -20)
				self.rect.y = (random.randint(0, HEIGHT -30))*(-1)

			elif action == "top":
				self.rect.x = random.randint(1, WIDTH -20)
				self.rect.y = (random.randint(0, HEIGHT -30))*(-1)


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

	def update(self, key):
		x_move = 0;
		y_move = 0;



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

	if event.type == pygame.KEYDOWN:
		x_delta=0;
		y_delta=0;
		if event.key == pygame.K_LEFT:
			x_delta -= 10
		if event.key == pygame.K_RIGHT:
			x_delta += 10
		if event.key == pygame.K_UP:
			y_delta -= 10
		if event.key == pygame.K_DOWN:
			y_delta += 10

	pygame.display.update()
