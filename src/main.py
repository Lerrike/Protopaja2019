import pygame, sys, time
from pygame.locals import *
from player import Player
from drawplayer import DrawPlayer

def main():
	pygame.init()
	surface = pygame.display.set_mode((750,500))
	white = [255, 255, 255]
	surface.fill(white)
	pygame.display.set_caption('Aboense')
	
	drawPlayer1 = DrawPlayer(surface, 0, 0)
	
	pygame.display.flip()
	while True:
		time.sleep(.01)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()


if __name__ == '__main__':
	main()