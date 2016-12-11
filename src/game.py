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

<<<<<<< HEAD
##start graphics
=======
run = True

def game_start():
	global run,scene,lawrence,sc,ents,clock,lag,restart
	restart = False
	scene = scenery.Scenery()
	lawrence = person.Person()

	for x in xrange(1,500):
		if x % 16 == 1:
			ents.append(objects.Bird(x * random.randint(50, 100)))
		elif x % 16 == 5:
			ents.append(objects.Ball(x * random.randint(50, 500)))
		elif x % 16 == 9:
			ents.append(objects.Cone(x * random.randint(50, 500)))
		elif x % 16 == 13:
			ents.append(objects.Hurdle(x * random.randint(50, 500)))
	
	graphics.register(scene)
	graphics.register(lawrence)
	graphics.register(sc)

	for e in ents:
		graphics.register(e)

	clock = pygame.time.Clock()
	
	lag = 0

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
					lawrence.collide(e)
					restart = True
					if con.audio_support:
						pygame.mixer.stop
	
						effect = pygame.mixer.Sound(os.path.join('audio','jl_slap.ogg'))
						effect.play()
	
						effect = pygame.mixer.Sound(os.path.join('audio','jl_slap.ogg'))
						effect.play()
	
						pygame.mixer.music.stop()
	
						pygame.mixer.music.load(os.path.join('audio','endTest.ogg'))
						pygame.mixer.music.set_volume(.5)
						pygame.mixer.music.play(-1)
	
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

>>>>>>> 046f492412d10a2b51e0a6077f66bcb807cf7b21
graphics.init(con.SCR_WIDTH, con.SCR_HEIGHT)
ents = []
sc = score.Score()

##start audio and check for audio support
try:
	pygame.mixer.pre_init(44100, -16, 2, 4096)
	pygame.mixer.init()
except:
	print "You don't have audio support."
   	con.audio_support = False

if con.audio_support:
	audio.load_audio()

	pygame.mixer.music.load(os.path.join('audio','jl_music.ogg'))
	pygame.mixer.music.set_volume(.9)
	pygame.mixer.music.play(-1)

<<<<<<< HEAD

scene = scenery.Scenery()
lawrence = person.Person()
sc = score.Score()

ents = []
for x in xrange(1,1000):
	if x % 16 == 1:
		ents.append(objects.Bird(x * random.randint(50, 500)))
	elif x % 16 == 5:
		ents.append(objects.Ball(x * random.randint(50, 500)))
	elif x % 16 == 9:
		ents.append(objects.Cone(x * random.randint(50, 500)))
	elif x % 16 == 13:
		ents.append(objects.Hurdle(x * random.randint(50, 500)))

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
				if con.audio_support:
					audio.main_song.stop()
					audio.end_song.play(-1)

	if lag > con.ms_per_frame:
		graphics.update()
		lag -= con.ms_per_frame

	for e in events.event_queue:
		if e.type == pygame.QUIT:
			run = False

		elif e.type == pygame.KEYUP:
			if e.key ==  pygame.K_F4 and (e.mod & pygame.KMOD_ALT):
				run = False
	
=======
while run:
	game_start()
	game_loop()
	game_end()

>>>>>>> 046f492412d10a2b51e0a6077f66bcb807cf7b21
pygame.quit()

