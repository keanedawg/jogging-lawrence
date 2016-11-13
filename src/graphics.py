import pygame

images = {}
_width = None
_height = None
_screen = None

_entities = []
_map = None

def register(entity):
	global _entities
	if entity not in _entities:
		_entities.append(entity)
		
def set_map(map):
	global _map
	_map = map

def init(width, height, title = 'Jogging Lawrence'):
	global _width, _height, _screen
	_width = width
	_height = height
	
	pygame.display.init()
	_screen = pygame.display.set_mode((_width, _height), pygame.DOUBLEBUF)
	pygame.display.set_caption(title)

def update():
	global _screen, _entities
	_screen.fill((0, 0, 0))
	draw_map()
	for entity in _entities:
		_screen.blit( entity.sprite_sheet.subsurface(
								entity.FRAMES[12 * entity.level + int(entity.frame)]
						),
						(entity.x, entity.y))
	pygame.display.flip()


def load_image(path):
	global images
	if path in images:
		return images[path]
		
	image = pygame.image.load(path)
	image.convert()
	images[path] = image
	return image
