import os

import pygame

import graphics
import events
import map


class Action(object):
	IDLE   = 0
	TAUNT  = 1
	WALK   = 2
	ATTACK = 3
	DIE    = 4
	
class Dir(object):
	UP    = 1
	DOWN  = 2
	LEFT  = 4
	RIGHT = 8

class Minotaur(object):
	FRAMES = [(x * 48, y *48, 48, 48) for y in xrange(5) for x in xrange(10)]

	def __init__(self, x = 0, y = 0):
		self.sprite_sheet = graphics.load_image(os.path.join("img", "minotaur spritesheet calciumtrice.png"))
		self.x = x
		self.y = y
		self.facing_right = False
		self.action = Action.IDLE
		self.frame = 0
		self.speed = 3
		self.directions = 0

	def update(self):
		for event in events.event_queue:
			if event.type is pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					self.directions = self.directions | Dir.UP
					if self.action == Action.IDLE:
						self.action = Action.WALK
				elif event.key == pygame.K_DOWN:
					self.directions = self.directions | Dir.DOWN
					if self.action == Action.IDLE:
						self.action = Action.WALK
				elif event.key == pygame.K_LEFT:
					self.directions = self.directions | Dir.LEFT
					self.facing_right = False
					if self.action == Action.IDLE:
						self.action = Action.WALK
				elif event.key == pygame.K_RIGHT:
					self.directions = self.directions | Dir.RIGHT
					self.facing_right = True
					if self.action == Action.IDLE:
						self.action = Action.WALK
				elif event.key == pygame.K_SPACE:
					self.action = Action.ATTACK
					self.frame = 0
					
			elif event.type is pygame.KEYUP:
				if event.key == pygame.K_UP:
					self.directions = self.directions & ~Dir.UP
				elif event.key == pygame.K_DOWN:
					self.directions = self.directions & ~Dir.DOWN
				elif event.key == pygame.K_LEFT:
					self.directions = self.directions & ~Dir.LEFT
					if self.directions & Dir.RIGHT:
						self.facing_right = True
				elif event.key == pygame.K_RIGHT:
					self.directions = self.directions & ~Dir.RIGHT
					if self.directions & Dir.LEFT:
						self.facing_right = True
				elif event.key == pygame.K_SPACE:
					self.action = Action.IDLE

		if (not self.directions) and (self.action == Action.WALK):
			self.action = Action.IDLE
					
		if self.directions & Dir.UP:
			rect = pygame.Rect(self.x, self.y - self.speed, 48, 48)
			if map.rect.contains(rect):
				self.y = rect.y
			else:
				self.y = 0
		if self.directions & Dir.DOWN:
			rect = pygame.Rect(self.x, self.y + self.speed, 48, 48)
			if map.rect.contains(rect):
				self.y = rect.y
			else:
				self.y = map.height - 48
		if self.directions & Dir.LEFT:
			rect = pygame.Rect(self.x - self.speed, self.y, 48, 48)
			if map.rect.contains(rect):
				self.x = rect.x
			else:
				self.x = 0
		if self.directions & Dir.RIGHT:
			rect = pygame.Rect(self.x + self.speed, self.y, 48, 48)
			if map.rect.contains(rect):
				self.x = rect.x
			else:
				self.x = map.width - 48
				
		self.frame = (self.frame + 0.5) % 10
