import pygame, sys
from pygame.locals import *

def main():
	pygame.init()
	surface = pygame.display.set_mode((500,500))
	pygame.display.set_caption('Hello world!')
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

if __name__ == '__main__':
	main()