#!/usr/bin/env python2

import pygame

import events
import person
import graphics
import constants as con
import gamespeed
import scenery
import objects

graphics.init(con.SCR_WIDTH, con.SCR_HEIGHT)

scene = scenery.Scenery()
lawrence = person.Person()

ents = []
for x in xrange(1,51):
	if x % 4 == 0:
		ents.append(objects.Bird(x * 200))
	elif x % 4 == 1:
		ents.append(objects.Ball(x * 250))
	elif x % 4 == 2:
		ents.append(objects.Cone(x * 100))
	else:
		ents.append(objects.Hurdle(x * 200))

graphics.register(scene)
graphics.register(lawrence)

for e in ents:
	graphics.register(e)
	
clock = pygame.time.Clock()

run = True
lag = 0
while(run):
	ms = clock.tick(con.framerate)
	lag = lag + ms - con.ms_per_frame

	# Game Logic
	if lawrence.isAlive():
		gamespeed.update()

	events.update()
	lawrence.update()
	scene.update()
	for e in ents:
		e.update()

	# Collision
	if lawrence.isAlive():
		for e in ents:
			if lawrence.rect.colliderect(e.rect):
				lawrence.collide(e)
	
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
