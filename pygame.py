#Due December 2
import pygame
from pygame import *
import os, sys
from pygame.locals import *
from random import *

DELAY = 1000;
#creating initial colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
pink = (255, 153, 204)

#initalizing position variables
x_pos = 0
y_pos = 0


#Naming the screen that appears to 
pygame.display.set_caption("Sabine's Pygame Stacker Game")
#Close the screen using a tuple

class Flower(Sprite):
	def __int__(self):
		Sprite.__int__(self)
		self.image = image.load("Flower.jpeg").comvert_alpha()
		self.rect = self.image.get_rect()
	def move(self):
		randX = randint(0,600)
		randY = randint(0,400)
		self.rect.center = (randX, randY)
class Water_Can(Sprite):
	def __int__(self):
		Sprite.__int__(self)
		self.image = image.load("watercan.jpeg").comvert_alpha()
		self.rect = self.image.get_rect()
	def hit(self, target):
		return self.rect.colliderect(target)

init()
screen_create = display.set_mode((640,480))
display.set_caption("Water the Flowers")
mouse.set_visible(False)


flower = Flower()
can = Water_Can()

sprites = RenderPlain(flower, can)

while True:
    e = event.poll()
    if e.type == QUIT:
        quit()
        break

    elif e.type == MOUSEBUTTONDOWN:
        if shovel.hit(gold):
            mixer.Sound("cha-ching.wav").play()
            gold.move()
            hits += 1

            # reset timer
            time.set_timer(USEREVENT + 1, DELAY)
            
    elif e.type == USEREVENT + 1: # TIME has passed
        gold.move()

    # refill background color so that we can paint sprites in new locations
    screen.fill(bgcolor)
    t = f.render("Jackpot = " + str(hits), False, (0,0,0))
    screen.blit(t, (320, 0))        # draw text to screen.  Can you move it?

    # update and redraw sprites
    sprites.update()
    sprites.draw(screen)
    display.update()




























