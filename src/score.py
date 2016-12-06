# NEED TO DRAW THE SCORE
import pygame as pg
import constants

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
        while x in xrange(0,5):
            if tmpScore != 0:
                digit = tmpScore % 10
                tmpScore /= 10
            else:
                digit = 0

            ind[x] = digit
            self.nums[ind[x]]
            
        img = self.sprite_sheet.subsurface(self.FRAMES[int(self.frame)])
        for 

    def addScore
        
    def reset(self):
        self.score = 0



        

