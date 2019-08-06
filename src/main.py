import pygame, sys, time
from pygame.locals import *

def main():
	pygame.init()
	surface = pygame.display.set_mode((1000,500))
	pygame.display.set_caption('Aboense')
	
	while True:
		time.sleep(.01)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

if __name__ == '__main__':
	main()