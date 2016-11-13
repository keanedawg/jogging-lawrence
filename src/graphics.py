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

def init(width, height, title = 'Minotaur "game"'):
	global _width, _height, _screen
	_width = width
	_height = height
	
	pygame.display.init()
	_screen = pygame.display.set_mode((_width, _height), pygame.DOUBLEBUF)
	pygame.display.set_caption(title)

def draw_map():
	global _screen, _map
	for x in xrange(_map.width):
		for y in xrange(_map.height):
			tile = _map[x, y]
			tilex = tile % 30
			tiley = tile / 30
	
			_screen.blit(
					_map.tileset.subsurface((tilex * 16, tiley * 16, 16, 16)),
					(x * 16, y * 16)
			)

def update():
	global _screen, _entities
	_screen.fill((0, 0, 0))
	draw_map()
	for entity in _entities:
		_screen.blit(pygame.transform.flip(
							entity.sprite_sheet.subsurface(
								entity.FRAMES[10 * entity.action + int(entity.frame)]
							), entity.facing_right, False
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