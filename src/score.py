# NEED TO DRAW THE SCORE
import pygame as pg
import constants
import graphics
import os

class Score(object):
    def __init__(self):
        self._score = 0
        self.sprite_sheet = graphics.load_image(os.path.join("img", "score.png"))
        self.nums = [x*20 for x in xrange(0,10)]
        self.pad = 2
        self.wid = 20
        self.x = constants.SCR_HEIGHT + 3 * self.pad + 2.5 * self.wid # The right of the score.
        self.y = 5
        self._inds = [0 for x in xrange(0,5)]

    def draw(self):
        tmpScore = self._score
        digit = 0
        count = 0
        # Get each digit of the score.
        for x in xrange(0,5):
            if tmpScore != 0:
                digit = tmpScore % 10
                tmpScore /= 10
            else:
                digit = 0

            self._inds[x] = digit
            
        # Print out each digit, starting at the least significant digit.
        for x in xrange(0,5):
            self.nums[self._inds[x]]
            img = self.sprite_sheet.subsurface( (self._inds[x] * 20, 0, 20, 20) )
            xpos = self.x - (self.wid + self.pad) * (x + 1)
	    graphics.blit(img, (xpos, self.y, self.wid, self.wid) )

    def addScore(self,score):
        self._score += score
        if self._score < 0:
            self._score = 0

        
    def reset(self):
        self._score = 0
