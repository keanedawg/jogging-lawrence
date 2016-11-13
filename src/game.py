import pygame

import map
import events
import person
import graphics

framerate = 30
ms_per_frame = (1. / framerate) / 1000

graphics.init(320 *2, 160 *2)

minotaur = person.Person(10, 10)
graphics.register(minotaur)
	
clock = pygame.time.Clock()

run = True
lag = 0
while(run):
	ms = clock.tick(framerate)
	lag = lag + ms - ms_per_frame
	events.update()
	minotaur.update()
	
	if lag > ms_per_frame:
		graphics.update()
		lag -= ms_per_frame
	
	for e in events.event_queue:
		if e.type == pygame.QUIT:
			run = False
			
		elif e.type == pygame.KEYUP:
			if e.key ==  pygame.K_F4 and (e.mod & pygame.KMOD_ALT):
				run = False

pygame.quit()
