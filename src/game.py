#!/usr/bin/env python2
import pygame
import random

import os
import events
import person
import graphics
import constants as con
import gamespeed
import scenery
import objects
import score

pygame.mixer.pre_init(44100, -16, 2, 4096)

graphics.init(con.SCR_WIDTH, con.SCR_HEIGHT)

pygame.mixer.init()

pygame.mixer.music.load(os.path.join('audio','jl_music.mp3'))
pygame.mixer.music.play(-1)

scene = scenery.Scenery()
lawrence = person.Person()
sc = score.Score()

ents = []
for x in xrange(6,500):
	if x % 2 == 0:
		if x < 100:
			y = random.randint(0,7)
			if y == 1:
				ents.append(objects.Bird((x * 90) + random.randint(0,40)))
			elif y == 2:
				ents.append(objects.Ball((x * 90) + random.randint(0,40)))
			elif y == 3:
				ents.append(objects.Cone((x * 90) + random.randint(0,40)))
			elif y == 4:
				ents.append(objects.Hurdle((x * 90) + random.randint(0,40)))
			elif y == 5:
				z = random.randint(1,3)
				if z == 1:
					ents.append(objects.Pizza((x * 90) + random.randint(0,40)))
				elif z == 2:
					ents.append(objects.Hamburger((x * 90) + random.randint(0,40)))
				elif z == 3:
					ents.append(objects.Cheesecake((x * 90) + random.randint(0,40)))
			elif y == 6:
				z = random.randint(1,3)
				if z == 1:
					ents.append(objects.Celery((x * 90) + random.randint(0,40)))
				elif z == 2:
					ents.append(objects.Carrot((x * 90) + random.randint(0,40)))
				elif z == 3:
					ents.append(objects.Apple((x * 90) + random.randint(0,40)))
		elif x >= 100 and x < 300:
			y = random.randint(0,7)
			if y == 1:
				ents.append(objects.Bird((x * 85) + random.randint(0,40)))
			elif y == 2:
				ents.append(objects.Ball((x * 85) + random.randint(0,40)))
			elif y == 3:
				ents.append(objects.Cone((x * 85) + random.randint(0,40)))
			elif y == 4:
				ents.append(objects.Hurdle((x * 85) + random.randint(0,40)))
			elif y == 5:
				ents.append(objects.Cone(x * 85))
				ents.append(objects.Cone((x * 85) + 20))
			elif y == 6:
				z = random.randint(1,3)
				if z == 1:
					ents.append(objects.Pizza((x * 85) + random.randint(0,40)))
				elif z == 2:
					ents.append(objects.Hamburger((x * 85) + random.randint(0,40)))
				elif z == 3:
					ents.append(objects.Cheesecake((x * 85) + random.randint(0,40)))
			elif y == 7:
				z = random.randint(1,3)
				if z == 1:
					ents.append(objects.Celery((x * 85) + random.randint(0,40)))
				elif z == 2:
					ents.append(objects.Carrot((x * 85) + random.randint(0,40)))
				elif z == 3:
					ents.append(objects.Apple((x * 85) + random.randint(0,40)))
		elif x >= 300:
			y = random.randint(0,6)
			if y == 1:
				ents.append(objects.Bird((x * 80) + random.randint(0,40)))
			elif y == 2:
				ents.append(objects.Ball((x * 80) + random.randint(0,40)))
			elif y == 3:
				ents.append(objects.Cone((x * 80) + random.randint(0,40)))
			elif y == 4:
				ents.append(objects.Hurdle((x * 80) + random.randint(0,40)))
			elif y == 5:
				ents.append(objects.Cone(x * 80))
				ents.append(objects.Cone((x * 80) + 20))
			elif y == 6:
				ents.append(objects.Cone(x * 80))
				ents.append(objects.Cone((x * 80) + 20))
				ents.append(objects.Cone((x * 80) + 40))
			elif y == 7:
				z = random.randint(1,3)
				if z == 1:
					ents.append(objects.Pizza((x * 80) + random.randint(0,40)))
				elif z == 2:
					ents.append(objects.Hamburger((x * 80) + random.randint(0,40)))
				elif z == 3:
					ents.append(objects.Cheesecake((x * 80) + random.randint(0,40)))
			elif y == 8:
				z = random.randint(1,3)
				if z == 1:
					ents.append(objects.Celery((x * 80) + random.randint(0,40)))
				elif z == 2:
					ents.append(objects.Carrot((x * 80) + random.randint(0,40)))
				elif z == 3:
					ents.append(objects.Apple((x * 80) + random.randint(0,40)))

graphics.register(scene)
graphics.register(lawrence)
graphics.register(sc)

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

        # Update Score
        if gamespeed.frame % 15 == 0:
                sc.addScore(1)

	# Collision
	if lawrence.isAlive():
		for e in ents:
			if lawrence.rect.colliderect(e.rect):
				lawrence.collide(e)

				pygame.mixer.stop

				effect = pygame.mixer.Sound(os.path.join('audio','jl_slap.ogg'))
				effect.play()

				pygame.mixer.music.load(os.path.join('audio','endTest.mp3'))
				pygame.mixer.music.play()

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
