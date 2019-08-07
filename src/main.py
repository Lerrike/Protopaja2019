import pygame, sys, time
from pygame.locals import *
from player import Player
from drawplayer import DrawPlayer

def main():
	pygame.init()
	surface = pygame.display.set_mode((750,500))
	white = [255, 255, 255]
	surface.fill(white)
	blue = [122,197,205]
	pygame.display.flip()
	
	pygame.draw.rect(surface, blue, (500,0,250,500),0)
	pygame.display.update()

    
	pygame.display.set_caption('Aboense')
	
	playerList = []
	for i in range(5):
		player = Player(i)
		drawPlayer = DrawPlayer(surface, 0, i*100)
		drawPlayer.drawStringData(player.return_number(), player.return_hearth(), player.return_breath())
		drawPlayer.drawGraph()
		drawPlayer.drawPosition(player.return_xPos(), player.return_yPos())
		combination = []
		combination.append(player)
		combination.append(drawPlayer)
		playerList.append(combination)
	
	pygame.display.flip()
	while True:
		time.sleep(.01)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()


if __name__ == '__main__':
	main()