#Due December 2
from pygame import *
from pygame.sprite import *
import pygame
import random
import os, sys

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

# paused = False
# mute = False

height_of_screen = 800
x_position = 0
y_position = 0

clock = pygame.time.Clock()



# class Pygame_main:

# 	def __int__(self, width = 800, height = 800):
# 		pygame.init()
# 		self.width = width
# 		self.height = height 
# 		self.screen = pygame.display.set_mode((self.width, self.height))
# 		self.name = pygame.display.set_caption("Sabine's Pygame Stacker Game")

# 	def Main_game(self):
# 		self.Init_sprites();
# 		pygame.key.set_repeat(500, 30)
# 		self.background = pygame.Surface(self.screen.get_size())
# 		self.background = self.background.convert()
# 		self.background.fill(pink)

# 		while 1:
# 			for event in pygame.event.get():
# 				if event.type == pygame.QUIT: 
# 					sys.exit()
# 				elif event.type == KEYDOWN:
# 					if ((event.key == K_RIGHT)
# 					or (event.key == K_LEFT)
#  					or (event.key == K_UP)
# 					or (event.key == K_DOWN)):
# 						self.snake.move(event.key)
# 			collision_check = pygame.sprite.spritecollide(self.snake, self.pellet_sprites, True)
# 			self.snake.pellets = self.snake.pellets + len(collision_check)

# 			self.screen.blit(self.background, (0, 0))     
# 			if pygame.font:
# 				font = pygame.font.Font(None, 36)
# 				text = font.render("Pellets %s" % self.snake.pellets
#                                     , 1, (255, 0, 0))
# 				textpos = text.get_rect(centerx=self.background.get_width()/2)
# 				self.screen.blit(text, textpos)

# 			self.pellet_sprites.draw(self.screen)
# 			self.snake_sprites.draw(self.screen)
# 			pygame.display.flip()

	# def Init_sprites (self):
	# 	self.snake = Snake()
	# 	self.snake_sprites = pygame.sprite.RenderPlain((self.snake))

	# 	nNumHorizontal = int(self.width/64)
	# 	nNumVertical = int(self.height/64)       
 #        # """Create the Pellet group"""
	# 	self.pellet_sprites = pygame.sprite.Group()
 #        # """Create all of the pellets and add them to the 
 #        # pellet_sprites group"""
	# 	for x in range(nNumHorizontal):
	# 		for y in range(nNumVertical):
	# 			self.pellet_sprites.add(Pellet(pygame.Rect(x*64, y*64, 64, 64)))

class Snake(Sprite):

	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load('images/bunny.bmp').convert()
		self.rect = self.image.get_rect()
		self.pellets = 0

		self.x_dist = 2
		self.y_dist = 2

	def movement(self, key):

		xMove = 0;
		yMove = 0;
        
		if (key == K_RIGHT):
			xMove = self.x_dist
		elif (key == K_LEFT):
			xMove = -self.x_dist
		elif (key == K_UP):
			yMove = -self.y_dist
		elif (key == K_DOWN):
			yMove = self.y_dist

			self.rect.move_ip(xMove,yMove);

	def update(self, action):

		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: 
					sys.exit()
				elif event.type == KEYDOWN:
					if ((event.key == K_RIGHT)
					or (event.key == K_LEFT)
					or (event.key == K_UP)
					or (event.key == K_DOWN)):
						self.snake.move(event.key)

		lsteating = pygame.sprite.spritecollide(self.Snake, self.carrot.sprites, True)
		self.snake.pellets = self.snake.pellets +len(lsteating)

		if pygame.font:
			font = pygame.font.Font(None, 36)
			text = font.render("Pellets %s" % self.snake.pellets
                                    , 1, (255, 0, 0))
			textpos = text.get_rect(centerx=self.background.get_width()/2)
			self.screen.blit(text, textpos)

		self.pellet_sprites.draw(self.screen)
		self.snake_sprites.draw(self.screen)
		pygame.display.flip()

		gameExit = False

class Pellet(Sprite):

	def __init__(self, react = None):
		Sprite.__init__(self)
		self.image = image.load('images/carrot.bmp').convert()
		self.rect = self.image.get_rect()
		if rect != None:
			self.rect = rect


init()
gameDisplay = display.set_mode((Width, Height))
display.set_caption("Sabine's Pygame Stacker Game")

   

bunny = Snake()
carrot = Pellet()

sprites = RenderPlain(bunny, carrot)





# gameExit = False

# while not gameExit:
# 	for event in pygame.event.get():

# 		if event.type == KEYDOWN:
# 			if ((event.key == K_RIGHT)
# 			or (event.key == K_LEFT)
#  			or (event.key == K_UP)
# 			or (event.key == K_DOWN)):
# 				snake.move(event.key)
     
	# if pygame.font:
	# 	font = pygame.font.Font(None, 36)
	# 	text = font.render("Pellets %s" % self.snake.pellets
 #                                    , 1, (255, 0, 0))
	# 	textpos = text.get_rect(centerx=self.background.get_width()/2)
	# 	self.screen.blit(text, textpos)

	# self.pellet_sprites.draw(self.screen)
	# self.snake_sprites.draw(self.screen)
	# pygame.display.flip()































