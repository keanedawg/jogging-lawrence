##initialize audio
import pygame
import os
import constants as con

##load all audio
def load_audio():
	global slap_sound, duck_sound, jump_sound, end_song
	end_song = pygame.mixer.Sound(os.path.join('audio','endTest.ogg'))
	end_song.set_volume(.5)
	
	duck_sound = pygame.mixer.Sound(os.path.join('audio','jl_duck.ogg'))
	duck_sound.set_volume(.5)
	
	slap_sound = pygame.mixer.Sound(os.path.join('audio','jl_slap.ogg'))
	jump_sound = pygame.mixer.Sound(os.path.join('audio','jl_jump.ogg'))












