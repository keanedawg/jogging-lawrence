# This module takes care of the slowly incrementing game speed.
import constants as con

# Constants
_START_SPEED = int(con.SCR_WIDTH * 3/8 / con.framerate)
_MAX_SPEED = 2.0 * _START_SPEED
_SPEED_LEVELS = 3.0

# The level will speed up every X seconds.
_ACCELERATION_INTERVAL = int(5 * con.framerate)
_ACCELERATION = (_MAX_SPEED - _START_SPEED) / _SPEED_LEVELS

def update():
	global speed, frame

	if frame % _ACCELERATION_INTERVAL == 0 and frame != 0:
		if speed >= _MAX_SPEED:
			speed = _MAX_SPEED
		else:
			speed += _ACCELERATION

	frame += 1

speed = _START_SPEED
frame = 0

def reset():
	global speed, frame
	speed = _START_SPEED
	frame = 0
