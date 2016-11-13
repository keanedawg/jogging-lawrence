
import pygame

images = {}
_width = None
_height = None
_screen = None

_entities = []
_map = None

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
	global _width, _height, _screen
	_width = width
	_height = height
	
	pygame.display.init()
	# creates window
	_screen = pygame.display.set_mode((_width, _height), pygame.DOUBLEBUF)
	# sets title of the window
	pygame.display.set_caption(title)


def update():
	global _screen, _entities
	_screen.fill((0, 0, 0))
	for entity in _entities:
		_screen.blit( entity.sprite_sheet.subsurface(entity.FRAMES[12 * entity.weight + int(entity.frame)])
					,(entity.x, entity.y))	
	pygame.display.flip()


def load_image(path):
	global images
	if path in images:
		return images[path]
		
	image = pygame.image.load(path)
	image = pygame.transform.scale(image, (image.get_width() * 2, image.get_height() * 2))
	image.convert()
	images[path] = image
	return image
