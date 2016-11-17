import os

import pygame

import graphics
import events
import constants as con
import gamespeed

class Food(object):
	PIZZA 		= 0
	HAMBURGER 	= 1
	CHEESECAKE 	= 2
	CELERY 		= 3
	CARROT 		= 4
	APPLE 		= 5

class Obstacles(object):
	CONE = 0
	HURDLE = 1
	BASEBALL = 3
	BIRD = 4

class Food(pygame.Rect):
	def __init__(self):
		self.sprite_sheet
		self.w = _SPR_DIM
		self.h = _SPR_DIM

		self.x = 10
		self.y = con.GROUND_Y - self.h

		# Horizontal and Vertical Speeds
		self.hs = 0
		self.vs = 0

		self.eaten = False
		self.isHealthy = False
		self.food = Food.PIZZA

		self.frame = 0
		self.speed = 3

	def update(self):
		checkEaten()
		if(self.eaten)
			destroyFruit()


	def checkEaten(self):
		# if hit 
		# self.eaten = True
		pass

	def destroyFruit(self):
		pass

	def updateFrame(self):
		self.frame = (self.frame + 0.05 * gamespeed.speed) % 3 * 3

	def draw(self):
		pass

class Obstacle(pygame.Rect):
	def __init__(self):
		self.img
		self.typeOfObstacle = Obstacles.CONE

		def setToGround(self):
			pass

		def setToFlying(self):
			pass

		def draw(self):
			pass
