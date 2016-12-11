import pygame

images = {}
_width = None
_height = None
_screen = None
_backBuf = None

_entities = []
_map = None

def reset():
	del _entities[:]

# adds entity to entities - which holds what needs to be drawn
# each entity needs sprite_sheet, frame, weight
# , and FRAMES (ann array of x and y coods representing the positions on teh sprite sheet)
# also an x and y position
def register(entity):
	global _entities
	if entity not in _entities:
		_entities.append(entity)

# Creates graphics object. sets its width, height and title of the window of the game
def init(width, height, title = 'Jogging Lawrence'):
	global _width, _height, _screen, _backBuf
	_width = width * 2
	_height = height * 2
	
	pygame.display.init()
	# creates window
	_screen = pygame.display.set_mode((_width, _height), pygame.DOUBLEBUF)
	_backBuf = pygame.Surface((width, height))
	# sets title of the window
	pygame.display.set_caption(title)

# Draws all the entities.
def update():
	global _screen, _entities, _backBuf
	_backBuf.fill((0, 0, 0))
	for entity in _entities:
		entity.draw()

	pygame.transform.scale(_backBuf, (_width, _height), _screen)
	pygame.display.flip()

def blit(surface, pos):
	global _backBuf
	surface = pygame.transform.scale(surface, (surface.get_width(), surface.get_height()))
	_backBuf.blit(surface, (pos[0], pos[1]))	

def drawRect(rect):
	pygame.draw.rect(_backBuf, (0, 0, 0), rect)
	
def load_image(path):
	global images
	if path in images:
		return images[path]
		
	image = pygame.image.load(path)
	image.convert()
	images[path] = image
	return image
