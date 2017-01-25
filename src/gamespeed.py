# This module takes care of the slowly incrementing game speed.
import constants as con

# Constants
_START_SPEED = con.SCR_WIDTH * 4/8 / con.framerate
_MAX_SPEED = 6.0 * _START_SPEED
_SPEED_LEVELS = 16

# The level will speed up every X seconds.
_ACCELERATION_INTERVAL = int(20 * con.framerate)
_ACCELERATION = (_MAX_SPEED - _START_SPEED) / _SPEED_LEVELS

def update():
	global speed, frame, pos

	if frame % _ACCELERATION_INTERVAL == 0 and frame != 0:
		if speed >= _MAX_SPEED:
			speed = _MAX_SPEED
		else:
			speed += _ACCELERATION

	pos -= speed
	frame += 1

# Global variables.
speed = _START_SPEED # The current speed of the ground.
pos   = 0            # The position of the starting point of the ground.
frame = 0            # How many frames have been running.

def reset():
	global speed, frame, pos
	speed = _START_SPEED
	pos = 0
	frame = 0
