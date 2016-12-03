from pygame import *
from pygame.sprite import *
import pygame
import random, time
import os, sys
from pygame.locals import *

#Initialize width and height of screen
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

#Initial speeds of sprites
pattyspeed = 10
bunspeed = 5
maxpatty = 10
maxpizza = 10

#Initial positions 
height_of_screen = 800
x_position = 520
y_position = 420

clock = pygame.time.Clock()	

class Patty(Sprite):
#Initializing the patty sprite class
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("beef.patty.png").convert_alpha()
		self.rect = self.image.get_rect()
#Creates random position for the items to drop from
	def back_to_top(self):
		self.rect.y = random.randrange(-300, -20)
		self.rect.x = random.randrange(0, Height)
#If the sprite passes the bottom of the screen it goes back to the top of the screen
	def update(self):
		self.rect.y += 3
		if self.rect.y > 610:
			self.back_to_top()
#Updating the random position everytime it falls
	def reset (self):
		self.rect.y = random.randrange(-300, -20)


class Pizza(Sprite):
#Initializing the pizza sprite class
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("pizza.png").convert_alpha()
		self.rect = self.image.get_rect()
#Creates random position for the items to drop from
	def back_to_top(self):
		self.rect.y = random.randrange(-300, -20)
		self.rect.x = random.randrange(0, Height)
#If the sprite passes the bottom of the screen it goes back to the top of the screen
	def update(self):
		self.rect.y += 3
		if self.rect.y > 610:
			self.back_to_top()

class Hotdog(Sprite):
#Initializing the hotdog sprite class
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("hotdog.png").convert_alpha()
		self.rect = self.image.get_rect()
#Creates random position for the items to drop from
	def back_to_top(self):
		self.rect.y = random.randrange(-300, -20)
		self.rect.x = random.randrange(0, Height)
#If the sprite passes the bottom of the screen it goes back to the top of the screen
	def update(self):
		self.rect.y += 3
		if self.rect.y > 610:
			self.back_to_top()

class Bun(Sprite):
	#Initializing the bun sprite class
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("bun.png").convert_alpha()
		self.rect = self.image.get_rect()

#Defines x and y coordinates of the bun
	def update(self, x = 800):
		self.rect.x = x_position
		self.rect.y = y_position
#Setting the y positioning on the screen
	def reset(self):
		self.rect.y = random.randrange(-300, -20)
			


#Initialize game
init()

#creting the display screen and naming it
gameDisplay = display.set_mode((Width, Height))
screen = gameDisplay
display.set_caption("Sabine's Pygame Hamburger Game")
# back = pygame.image.load("restfront.png").convert_alpha
# back = pygame.transform.scale(back, (Width, Height))
# screen.blit(back, (0,0))

#Rendering all the sprites
f = font.Font(None, 25)
patty = Patty()
bun = Bun()
pizza = Pizza()
hotdog = Hotdog()
sprites = RenderPlain(bun, patty, pizza, hotdog)


game_over = False
hits = 0

clock = pygame.time.Clock()
#Creates an infinite lop of music until the game ends
mixer.music.load("themesong.wav")
mixer.music.play(-1)

#If the game is not exited
gameExit = False
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
#Once keys are pressed down the bun can move from left to right
	clock.tick(60)
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT or event.key == pygame.K_a:
			x_position -= bunspeed

		if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
			x_position += bunspeed
		
#If the bun is not moving and hits the patty the score goes up 1 point
		# if pygame.sprite.collide_rect(bun, patty):
		# 	hits += 1
		# 	patty.back_to_top()

#If the bun is moving and hits the patty the score goes up 1 point
		if bun.rect.colliderect(patty):
			hits += 1
			patty.back_to_top()

#If the bun is not moving and hits the pizza the score goes up 1 point
		# if pygame.sprite.collide_rect(bun, pizza):
		# 	hits = hits - 1
		# 	patty.back_to_top()

#If the bun is moving and hits the pizza the score goes down 1 point
		if bun.rect.colliderect(pizza):
			hits = hits - 1
			pizza.back_to_top()

#If the bun is not moving and hits the hotdog the score down 1 point
		# if pygame.sprite.collide_rect(bun, hotdog):
		# 	hits = hits - 1
		# 	patty.back_to_top()

#If the bun is moving and hits the hotdog the score goes down 1 point
		if bun.rect.colliderect(hotdog):
			hits = hits - 1
			hotdog.back_to_top()

		if bun.rect.y == (Height - 5):
			bun.rect.y = 10			
#Once the player has collected 5 hotdogs
	if hits == 5:
#Show the score
		t = f.render("Score = " + str(hits), False, (0,0,0))
		screen.blit(t, (320, 0))
		sprites.draw(screen)
		display.update()
#Show winner on a timed interval
		pygame.time.delay(3000)
		s = f.render("WINNER!!", 1, (0,0,0))
		screen.blit(s, (5, 480))
		sprites.draw(screen)
		display.update()
		
		pygame.time.delay(3000)
#creates background color, updates sprites, and updates the display
		screen.fill(white)
		patty.update()
		#patty.draw()
		sprites.update()
		sprites.draw(screen)
		display.update()
#Kill off all the sprites
		bun.kill()
		pizza.kill()
		patty.kill()
		hotdog.kill()
#creates background color, updates sprites, and updates the display
	screen.fill(white)
	patty.update()
	sprites.update()
	sprites.draw(screen)
	display.update()
	
