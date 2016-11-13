import pygame

event_queue = []
_event_buffer = []

def new_event(event):
	global _event_buffer
	_event_buffer.append(event)

def update():
	global event_queue, _event_buffer
	event_queue = pygame.event.get()
	event_queue.extend(_event_buffer)
	_event_buffer = []