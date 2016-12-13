import os

import pygame

import graphics
import events
import constants as con
import gamespeed
import audio

OBJECT_SIZE=20
OBJECT_FRAME_SPEED=.025
OBJECT_NUM_OF_FRAMES=3
_OBJ_VS=-4.0
_GRAVITY = 22.8 / con.framerate

class EntityType(object):
	NONE        = -1
	BALL        = 0 # AIR
	BIRD        = 1 # AIR
	CONE        = 2 # GROUND
	HURDLE      = 3 # GROUND
	PIZZA 		= 4 # FAT
	HAMBURGER 	= 5 # FAT
	CHEESECAKE 	= 6 # FAT
	CELERY 		= 7 # SKINNY
	CARROT 		= 8 # SKINNY
	APPLE 		= 9 # SKINNY

class Food(object):
	# ss_off - The vertical offset for the sprite sheet.
	# xoff   - The starting x position. Relative to overall game's x.
	# ground - True if this is a ground obstacle. False if this is a flying obstacle.
	def __init__(self, ss_off, xoff, level):
		self.type = EntityType.NONE
		self.sprite_sheet = graphics.load_image(os.path.join("img", "objects.png"))
		self.xoff = xoff
		self.x = gamespeed.pos + self.xoff
		self.y = 0.
		self.rect = pygame.Rect(self.x, self.y, OBJECT_SIZE, OBJECT_SIZE)
		self.FRAMES = [(i * OBJECT_SIZE, ss_off * OBJECT_SIZE, OBJECT_SIZE, OBJECT_SIZE) for i in xrange(OBJECT_NUM_OF_FRAMES)]
		self.frame = i * OBJECT_SIZE
		self.gravity = False
		self.vs = 0.

		if level == 3:
			self.setToLevel3()
		elif level == 2:
			self.setToLevel2()
		else:
			self.setToLevel1()

	def setToLevel1(self):
		self.y = con.GROUND_Y - OBJECT_SIZE

	def setToLevel2(self):
		self.y = con.GROUND_Y - OBJECT_SIZE * 2

	def setToLevel3(self):
		self.y = con.GROUND_Y - OBJECT_SIZE * 3

	def hit(self):
		if self.gravity:
			return 0
		self.vs = -self.weight
		self.gravity = True
		if con.audio_support:
			self.sound.play()

		return self.val

	def draw(self):
		img = self.sprite_sheet.subsurface(self.FRAMES[int(self.frame)])
		graphics.blit(img, (self.x, self.y))
		#graphics.drawRect(self) # FOR TESTING

	def move(self):
		self.x = gamespeed.pos + self.xoff

		if self.gravity == True:
			self.y += self.vs
			self.vs += _GRAVITY

	def update(self):
		self.move()
		self.rect.x, self.rect.y = self.x, self.y
		if self.rect.y > con.SCR_HEIGHT:
			self.kill()

	def draw(self):
		img = self.sprite_sheet.subsurface(self.FRAMES[0])
		graphics.blit(img, (self.x, self.y))

	def kill(self):
		self.alive = False

########## Food ###############

class Pizza(Food):
	# The x is how far away from the starting point of the ground the bird is and remains.
	def __init__(self, xoff):
		# The type contains the vertical offset as well.
		super(Pizza, self).__init__(EntityType.PIZZA, xoff, True)
		self.type = EntityType.PIZZA
		self.val = -10
		self.weight = 6
		self.sound = audio.bad_food

class Hamburger(Food):
	# The x is how far away from the starting point of the ground the bird is and remains.
	def __init__(self, xoff):
		# The type contains the vertical offset as well.
		super(Hamburger, self).__init__(EntityType.HAMBURGER, xoff, False)
		self.type = EntityType.HAMBURGER
		self.val = -20
		self.weight = 5
		self.sound = audio.bad_food

class Cheesecake(Food):
	# The x is how far away from the starting point of the ground the bird is and remains.
	def __init__(self, xoff):
		# The type contains the vertical offset as well.
		super(Cheesecake, self).__init__(EntityType.CHEESECAKE, xoff, False)
		self.type = EntityType.CHEESECAKE
		self.val = -30
		self.weight = 4
		self.sound = audio.bad_food

class Celery(Food):
	# The x is how far away from the starting point of the ground the bird is and remains.
	def __init__(self, xoff):
		# The type contains the vertical offset as well.
		super(Celery, self).__init__(EntityType.CELERY, xoff, False)
		self.type = EntityType.CELERY
		self.val = 5
		self.weight = 9
		self.sound = audio.good_food

class Carrot(Food):
	# The x is how far away from the starting point of the ground the bird is and remains.
	def __init__(self, xoff):
		# The type contains the vertical offset as well.
		super(Carrot, self).__init__(EntityType.CARROT, xoff, False)
		self.type = EntityType.CARROT
		self.val = 10
		self.weight = 8
		self.sound = audio.good_food

class Apple(Food):
	# The x is how far away from the starting point of the ground the bird is and remains.
	def __init__(self, xoff):
		# The type contains the vertical offset as well.
		super(Apple, self).__init__(EntityType.APPLE, xoff, False)
		self.type = EntityType.APPLE
		self.val = 15
		self.weight = 7
		self.sound = audio.good_food

class Obstacle(object):
	# ss_off - The vertical offset for the sprite sheet.
	# xoff   - The starting x position. Relative to overall game's x.
	# ground - True if this is a ground obstacle. False if this is a flying obstacle.
	def __init__(self, ss_off, xoff, ground):
		self.type = EntityType.NONE
		self.sprite_sheet = graphics.load_image(os.path.join("img", "objects.png"))
		self.xoff = xoff
		self.x = gamespeed.pos + self.xoff
		self.y = 0.
		self.rect = pygame.Rect(self.x, self.y, OBJECT_SIZE, OBJECT_SIZE)
		self.FRAMES = [(i * OBJECT_SIZE, ss_off * OBJECT_SIZE, OBJECT_SIZE, OBJECT_SIZE) for i in xrange(OBJECT_NUM_OF_FRAMES)]
		self.frame = 0.
		self.gravity = False
		self.vs = 0.

		if ground:
			self.setToGround()
		else:
			self.setToFlying()

	def setToGround(self):
		self.y = con.GROUND_Y - OBJECT_SIZE

	def setToFlying(self):
		self.y = con.GROUND_Y - OBJECT_SIZE * 2

	def hit(self):
		self.vs = _OBJ_VS
		self.gravity = True

	def draw(self):
		img = self.sprite_sheet.subsurface(self.FRAMES[int(self.frame)])
		graphics.blit(img, (self.x, self.y))
		#graphics.drawRect(self) # FOR TESTING

	def updateFrame(self):
		self.frame = (self.frame + OBJECT_FRAME_SPEED * gamespeed.speed) % OBJECT_NUM_OF_FRAMES

	def move(self):
		self.x = gamespeed.pos + self.xoff

		if self.gravity == True:
			self.y += self.vs
			self.vs += _GRAVITY

	def update(self):
		self.move()
		self.updateFrame()
		self.rect.x, self.rect.y = self.x, self.y

########## OBSTACLES ###############

class Bird(Obstacle):
	# The x is how far away from the starting point of the ground the bird is and remains.
	def __init__(self, xoff):
		# The type contains the vertical offset as well.
		super(Bird, self).__init__(EntityType.BIRD, xoff, False)
		self.type = EntityType.BIRD

class Ball(Obstacle):
	def __init__(self, xoff):
		super(Ball, self).__init__(EntityType.BALL, xoff, False)
		self.type = EntityType.BALL

class Cone(Obstacle):
	def __init__(self, xoff):
		super(Cone, self).__init__(EntityType.CONE, xoff, True)
		self.type = EntityType.CONE

class Hurdle(Obstacle):
	def __init__(self, xoff):
		super(Hurdle, self).__init__(EntityType.HURDLE, xoff, True)
		self.type = EntityType.HURDLE
