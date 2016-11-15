#!/usr/bin/env python2
# So I (Alan) can execute the file easily.

import pygame

import map
import events
import person
import graphics
import constants as con
import gamespeed
import scenery

graphics.init(con.SCR_WIDTH, con.SCR_HEIGHT)

scene = scenery.Scenery()
minotaur = person.Person()

graphics.register(scene)
graphics.register(minotaur)
	
clock = pygame.time.Clock()

run = True
lag = 0
while(run):
	ms = clock.tick(con.framerate)
	lag = lag + ms - con.ms_per_frame
	gamespeed.update()
	events.update()
	minotaur.update()
	scene.update()
	
	if lag > con.ms_per_frame:
		graphics.update()
		lag -= con.ms_per_frame
	
	for e in events.event_queue:
		if e.type == pygame.QUIT:
			run = False
			
		elif e.type == pygame.KEYUP:
			if e.key ==  pygame.K_F4 and (e.mod & pygame.KMOD_ALT):
				run = False

pygame.quit()
