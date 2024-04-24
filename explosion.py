import pygame
from pygame.sprite import Sprite
from pygame.locals import *
import random

#create Explosion class

class Explosion(Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		for num in range(1, 6):
			img = pygame.image.load(f"images/exp{num}.png")
			img = pygame.transform.scale(img, (100, 100))
			self.images.append(img)
		self.index = 0
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.counter = 0
		self.exp_coordinate_x = 0
		self.exp_coordinate_y = 0

	def update(self):
		explosion_speed = 4
		#update explosion animation
		self.counter += 1
		self.exp_coordinate_x=random.randint(50,1000) # Varies from large to small
		self.exp_coordinate_y=random.randint(50,1000)

		if self.counter >= explosion_speed and self.index < len(self.images) - 1:
			self.counter = 0
			self.index += 1
			self.image = self.images[self.index]
			# Make explosion more dynamic but randomizing how large it is. Use the same coordinates if you want to keep
			# explosion semi-proportional (e.g. x,x)
			self.image = pygame.transform.scale(self.image,(self.exp_coordinate_x,self.exp_coordinate_x))


		#if the animation is complete, reset animation index
		if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
			self.kill()                   