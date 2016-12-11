import os

import pygame

import graphics
import events
import constants as con
import gamespeed
import audio
from objects import EntityType as et

class Physics(object):
	# EARTH GRAVITY = 9.8 m/s - 1 m is about 22.8 px in this game.
	GRAVITY = 22.8 / con.framerate
	FALLING = GRAVITY * 6
	JUMP = 7
	SUPJUMP = 8.0
	FRAME_JUMP_DELAY = con.framerate / 14 # SUPER JUMP after a fraction of a second.

_SPR_DIM = 40
_SPR_ROWS = 6
_SPR_COLS = 9

_RECT_W = 12
_RECT_H = 30

_RECT_XOFF = -13
_RECT_YOFF = 0
_RECT_YOFF_DUCK = 21

_GROUND_PLAYER_HEAD = con.GROUND_Y - _SPR_DIM # The location of the top of the player relative to the ground.
_GROUND_PLAYER_HEAD_DUCK = con.GROUND_Y - _SPR_DIM / 20 # The location of the top of the player relative to the ground when ducking.
_PLAYER_RECT_X_START = 23

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

class Person(object):
	FRAMES = [(x * _SPR_DIM, y * _SPR_DIM, _SPR_DIM, _SPR_DIM) for y in xrange(_SPR_ROWS) for x in xrange(_SPR_COLS)]

	def __init__(self):
		self.sprite_sheet = graphics.load_image(os.path.join("img", "jogging_lawrence.png"))
		self.rect = pygame.Rect(_PLAYER_RECT_X_START, _GROUND_PLAYER_HEAD, _RECT_W, _RECT_H)

		self.jump_counter = 0
		self.jump_counter_enabled = False
		self.jump_released = False

		self.down_pressed = False

		# Horizontal and Vertical Speeds
		self.hs = 0
		self.vs = 0
		self.alive = True

		self.on_ground = True # If on the ground.
		self.falling = False  # If down was pressed.

		self.action = Action.RUN
		self.weight = Weight.NORMAL

		self.frame = 0
		self.speed = 3

	# This gets called by the game loop.
	def update(self):
		if self.isAlive():
			self.input()
			self.checkDown()
			self.checkJump()
			self.move()
			# Moves the rectangle down if ducking.
			if self.action == Action.DUCK:
				self.rect.y += _RECT_YOFF_DUCK
			self.updateFrame()
		else:
			pass
			#self.move()
			#self.updateFrame()

	# This handles gravity and movement.
	def move(self):
		self.rect.y += self.vs

		# If not touching the ground.
		if self.rect.y < _GROUND_PLAYER_HEAD:
			# If not falling, then gravity. If falling, then falling gravity.
			self.vs += Physics.GRAVITY if not self.falling else Physics.FALLING
			self.on_ground = False
		else:
			self.rect.y = _GROUND_PLAYER_HEAD
			self.vs = 0
			# If on ground, then not falling. Duh.
			self.on_ground = True
			self.falling = False
			if self.action != Action.DUCK and self.alive == True:
				self.action = Action.RUN

	# Based on the current action and weight, the frame is correctly updated.
	def updateFrame(self):
		if self.action == Action.RUN:
			self.frame = (self.frame + 0.05 * gamespeed.speed) % 4
		else:
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

				if con.audio_support:
					audio.jump_sound.play()

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
				if not self.action == Action.DUCK and con.audio_support:
					##play duck audio
					if con.audio_support:
						audio.duck_sound.play()

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
		tmpFrame = 1 if self.action == Action.RUN and int(self.frame) == 3 else int(self.frame)
		img = self.sprite_sheet.subsurface(self.FRAMES[_SPR_COLS * self.weight + tmpFrame])
		graphics.blit(img, (self.rect.x + _RECT_XOFF, self.rect.y + _RECT_YOFF))
		# graphics.drawRect(self) # FOR TESTING

	def isAlive(self):
		return self.alive == True

	def kill(self):
		self.alive = False

	# Entity may be food or an obstacle. The difference is found by the type.
	def collide(self, entity):
		if entity.type == et.BALL or entity.type == et.BIRD or entity.type == et.CONE or entity.type == et.HURDLE:
			entity.hit()
			self.kill()
			if con.audio_support:
				audio.slap_sound.play()

		elif entity.type == et.PIZZA or entity.type == et.HAMBURGER or entity.type == et.CHEESECAKE:
			entity.hit()
			if con.audio_support:
				audio.bad_food.play()
			print "YUM!"
			# Get bigger

		elif entity.type == et.CELERY or entity.type == et.CARROT or entity.type == et.APPLE:
			entity.hit()
			if con.audio_support:
				audio.good_food.play()
			print "I'M STILL HUNGRY!"
			# Get thinner

		else:
			assert(False)
