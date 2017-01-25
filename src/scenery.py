import pygame
import graphics
import constants as con
import gamespeed
import os

_BKGD_SPEED_DIVIDOR = .1 # How much slower the background moves from the game.
_FORE_Y_POS = con.SCR_HEIGHT - 30 # Where the foreground will be drawn.

class Scenery(object):
	def __init__(self):
		self.bkgdImg  = graphics.load_image(os.path.join("img", "city.png"))
		self.foreImg  = graphics.load_image(os.path.join("img", "street.png"))

		self.bkgd_W = self.bkgdImg.get_width()
		self.bkgd_X = 0.

		self.bkgd_X1 = self.bkgd_X
		self.bkgd_X2 = self.bkgd_X + self.bkgd_W

		self.fore_W = self.foreImg.get_width()
		self.fore_X = 0.

		self.fore_X1 = self.fore_X
		self.fore_X2 = self.fore_X - self.fore_W
		self.fore_X3 = self.fore_X + self.fore_W

	def update(self):
		self.bkgd_X = self.bkgd_X % self.bkgd_W
		self.bkgd_X1 = int(self.bkgd_X)
		self.bkgd_X2 = self.bkgd_X1 - self.bkgd_W

		self.bkgd_X = gamespeed.pos * _BKGD_SPEED_DIVIDOR

		self.fore_X = self.fore_X % self.fore_W

		self.fore_X1 = int(self.fore_X)
		self.fore_X2 = self.fore_X1 - self.fore_W
		self.fore_X3 = self.fore_X1 + self.fore_W

		self.fore_X = gamespeed.pos


	def draw(self):
		self.drawBackground()
		self.drawForeground()

	def drawBackground(self):
		# Blit twice for a continuing background.
		graphics.blit(self.bkgdImg, (self.bkgd_X1, 0))
		graphics.blit(self.bkgdImg, (self.bkgd_X2, 0))

	def drawForeground(self):
		graphics.blit(self.foreImg, (self.fore_X1, _FORE_Y_POS))
		graphics.blit(self.foreImg, (self.fore_X2, _FORE_Y_POS))
		graphics.blit(self.foreImg, (self.fore_X3, _FORE_Y_POS))

	def getGroundSpeed(self):
		pass
