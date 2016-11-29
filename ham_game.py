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
bunspeed = 5

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
		self.image = image.load("beef.patty.bmp").convert_alpha()
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


# class Cheese(Sprite):
# 	def __init__(self):
# 		Sprite.__init__(self)
# 		self.image = image.load("cheese.bmp").convert()
# 		self.rect = self.image.get_rect()

# class Tomato(Sprite):
# 	def __init__(self):
# 		Sprite.__init__(self)
# 		self.image = image.load("tomato.bmp").convert()
# 		self.rect = self.image.get_rect()

class Bun(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("bun.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = (pygame.transform.scale()

	def update(self):
		self.rect.x = x_position

#	def update(self, )



init()

gameDisplay = display.set_mode((Width, Height))
screen = gameDisplay
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
		y_position = 450;
		if event.key == pygame.K_LEFT or event.key == pygame.K_a:
			x_position -= bunspeed
		if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
			x_position += bunspeed

	screen.fill(white)
	t = f.render("Score = " + str(5), False, (0,0,0))
    # t = f.render("Score = " + str(hits), False, (0,0,0))
	# screen.blit(t, (320, 0))
	sprites.update()
	sprites.draw(screen)
	display.update()
