import os

import pygame

import graphics
import events
import map

class Weight(object):
	ANOREXIC = 0
	SKINNY   = 1
	NORMAL   = 2
	FAT      = 3
	OBESE    = 4

class Action(object):
	RUN  = 0
	JUMP = 1
	DUCK = 2
	DIE  = 3
	
_SPR_DIM = 40
_SPR_ROWS = 6
_SPR_COLS = 12

class Person(pygame.Rect):
	FRAMES = [(x * _SPR_DIM, y * _SPR_DIM, _SPR_DIM, _SPR_DIM) for y in xrange(_SPR_ROWS) for x in xrange(_SPR_COLS)]

	def __init__(self, x = 0, y = 0):
		self.sprite_sheet = graphics.load_image(os.path.join("img", "jogging_lawrence.png"))
		self.x = x
		self.y = y

		self.w = _SPR_DIM
		self.h = _SPR_DIM

		self.action = Action.RUN
		self.weight = Weight.NORMAL

		self.frame = 0
		self.speed = 3

	def update(self):
		for event in events.event_queue:
			if event.type is pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self.jump()
			elif event.type is pygame.KEYUP:
				if event.key == pygame.K_SPACE:
					pass # Maybe something jumping related will go here.

		self.updateFrame()


	# Based on the current action and weight, the frame is correctly updated.
	def updateFrame(self):
		self.frame = (self.frame + 0.5) % 3 + self.action * 3

	def jump(self):
		print "You Jumped."
		pass # Nothing for now.
