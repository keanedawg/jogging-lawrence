import pygame

import gamespeed
#import scenery

obstacles = []
food = []
coins = []
speed  = gamespeed.speed

_SPR_DIM = 20
_SPR_COL = 4
_SPR_ROW = 4

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


class Patch():
	def __init__(self):
		self.amountOfObstacles
		self.obstacles

	def generateObstacles():
		for i in xrange(randint(1,3)):
			if self.amountOfObstacles > 1 
			&& (self.obstacles[0].typeOfObstacle == Obstacles.CONE || self.obstacles[0].typeOfObstacle == Obstacles.HURDLE)
			self.obstacles.append(Obstacle())

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


def getInstances():
	allInstaces = obstacles + food + coins
	return allInstaces

def genHealthyFood():



def genUnhealthyFood():



def genGround():



def genFlying():


def genGroundPatch():
	gPatch = Patch()
	gPatch.amountOfObstacles = gPatch.generateObstacles


def genFlyingPatch():


def deleteInstances():


def update():

