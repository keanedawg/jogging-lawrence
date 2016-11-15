import os

import pygame

import graphics
import events
import constants as con
import gamespeed

class Physics(object):
	# EARTH GRAVITY = 9.8 m/s - 1 m is about 22.8 px in this game.
	GRAVITY = 22.8 / con.framerate
	FALLING = GRAVITY * 6
	JUMP = 6.5
	SUPJUMP = 8.0
	FRAME_JUMP_DELAY = con.framerate / 14 # SUPER JUMP after a fraction of a second.

_SPR_DIM = 40
_SPR_ROWS = 6
_SPR_COLS = 12

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
	
class Person(pygame.Rect):
	FRAMES = [(x * _SPR_DIM, y * _SPR_DIM, _SPR_DIM, _SPR_DIM) for y in xrange(_SPR_ROWS) for x in xrange(_SPR_COLS)]

	def __init__(self):
		self.sprite_sheet = graphics.load_image(os.path.join("img", "jogging_lawrence.png"))
		self.w = _SPR_DIM
		self.h = _SPR_DIM

		self.jump_counter = 0
		self.jump_counter_enabled = False
		self.jump_released = False

		self.down_pressed = False

		self.x = 10
		self.y = con.GROUND_Y - self.h

		# Horizontal and Vertical Speeds
		self.hs = 0
		self.vs = 0

		self.on_ground = True # If on the ground.
		self.falling = False  # If down was pressed.

		self.action = Action.RUN
		self.weight = Weight.NORMAL

		self.frame = 0
		self.speed = 3

	# This gets called by the game loop.
	def update(self):
		self.input()
		self.checkDown()
		self.checkJump()
		self.move()
		
		self.updateFrame()

	# This handles gravity and movement.
	def move(self):
		self.y += self.vs

		# If not touching the ground.
		if self.y < con.GROUND_Y - self.h:
			# If not falling, then gravity. If falling, then falling gravity.
			self.vs += Physics.GRAVITY if not self.falling else Physics.FALLING
			self.on_ground = False
		else:
			self.y = con.GROUND_Y - self.h
			self.vs = 0
			# If on ground, then not falling. Duh.
			self.on_ground = True
			self.falling = False
			if self.action != Action.DUCK:
				self.action = Action.RUN

	# Based on the current action and weight, the frame is correctly updated.
	def updateFrame(self):
		self.frame = (self.frame + 0.05 * gamespeed.speed) % 3 + self.action * 3

	# Will jump if the timer has gone up.
	def checkJump(self):
		if self.jump_counter_enabled:
			self.jump_counter += 1

			if self.jump_counter >= Physics.FRAME_JUMP_DELAY:
				assert(self.on_ground) # Better be on the ground.

				self.jump_counter = 0
				self.jump_counter_enabled = False

				if self.jump_released:
					self.vs = -Physics.JUMP
				else:
					self.vs = -Physics.SUPJUMP

				self.jump_released = False
				self.action = Action.JUMP

	# This handles the input.
	def input(self):
		for event in events.event_queue:
			if event.type is pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self.pressSpace()
				elif event.key == pygame.K_DOWN:
					self.pressDown()
			elif event.type is pygame.KEYUP:
				if event.key == pygame.K_SPACE:
					self.releaseSpace()
				elif event.key == pygame.K_DOWN:
					self.releaseDown()

	# Starting the jump/jump timer.
	def pressSpace(self):
		if self.action == Action.RUN:
			self.jump_counter_enabled = True

	def releaseSpace(self):
		if self.jump_counter_enabled:
			self.jump_released = True

	def checkDown(self):
		if self.down_pressed and not self.jump_counter_enabled:
			if self.on_ground: # If on ground, then duck.
				self.action = Action.DUCK
			else: # If in air, then fall.
				self.falling = True

	# What happens when the player presses down.
	def pressDown(self):
		self.down_pressed = True

	def releaseDown(self):
		self.down_pressed = False

		if self.action == Action.DUCK:
			self.action = Action.RUN

	def draw(self):
		img = self.sprite_sheet.subsurface(self.FRAMES[_SPR_COLS * self.weight + int(self.frame)])
		graphics.blit(img, (self.x, self.y))
