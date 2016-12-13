##initialize audio
import pygame
import os
import constants as con

##load all audio
def load_audio():
	global slap_sound, duck_sound, jump_sound, end_song, bad_food, good_food, yay_sound
	end_song = pygame.mixer.Sound(os.path.join('audio','endTest.ogg'))
	end_song.set_volume(.5)
	
	duck_sound = pygame.mixer.Sound(os.path.join('audio','jl_duck.ogg'))
	duck_sound.set_volume(.4)
	
	slap_sound = pygame.mixer.Sound(os.path.join('audio','jl_slap.ogg'))
	slap_sound.set_volume(.8)

	jump_sound = pygame.mixer.Sound(os.path.join('audio','jl_jump.ogg'))
	jump_sound.set_volume(.9)

	bad_food = pygame.mixer.Sound(os.path.join('audio','jl_badFood.ogg'))
	bad_food.set_volume(.9)

	good_food = pygame.mixer.Sound(os.path.join('audio','jl_goodFood.ogg'))
	good_food.set_volume(.6)

	yay_sound = pygame.mixer.Sound(os.path.join('audio','jl_yay.ogg'))
	yay_sound.set_volume(.4)