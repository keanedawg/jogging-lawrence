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
import audio

ents = []

def game_start():
	global run,scene,lawrence,sc,ents,clock,lag,restart
	restart = False
	scene = scenery.Scenery()
	lawrence = person.Person()

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
	lag = 0
	if con.audio_support:
		pygame.mixer.music.play(-1)
		audio.yay_sound.play()

def game_loop():
	global events,run,scene,lawrence,sc,ents,clock,lag,restart,ms
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
					if e.type > objects.EntityType.HURDLE: # If it is a food.
						sc.addScore(e.hit())
					else:
						lawrence.collide(e)
						restart = True
						if con.audio_support:
							pygame.mixer.music.stop()

		if lag > con.ms_per_frame:
			graphics.update()
			lag -= con.ms_per_frame
	
		for e in events.event_queue:
			if e.type == pygame.QUIT:
				run = False
			elif e.type == pygame.KEYUP:
				if e.key ==  pygame.K_F4 and (e.mod & pygame.KMOD_ALT):
					run = False
		if restart:
			break

def game_end():
	global events,run,scene,lawrence,sc,ents,clock,lag,restart,ms
	del ents[:]
	graphics.reset()
	gamespeed.reset()
	sc.reset()

def main():
	global ents, sc, run
	run = True

	graphics.init(con.SCR_WIDTH, con.SCR_HEIGHT)
	sc = score.Score()

	try:
		pygame.mixer.pre_init(44100, -16, 2, 4096)
		pygame.mixer.init()
	except:
		print "You don't have audio support."
		con.audio_support = False

	if con.audio_support:
		audio.load_audio()
		pygame.mixer.music.load(os.path.join('audio','jl_music2.ogg'))
		pygame.mixer.music.set_volume(.9)

	while run:
		game_start()
		game_loop()
		game_end()

	pygame.quit()

if __name__ == "__main__":
	main()

