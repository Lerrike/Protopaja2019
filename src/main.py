import pygame, sys, time
from pygame.locals import *
from player import Player
from drawplayer import DrawPlayer
from Data_parse import data_parse

def main():
	pygame.init()
	surface = pygame.display.set_mode((750,500))
	pygame.display.set_caption('Aboense')
	
	white = [255, 255, 255]
	surface.fill(white)
	blue = [122,197,205]
	pygame.display.flip()
	pygame.draw.rect(surface, blue, (500,0,250,500),0)
	
	playerList = []
	for i in range(5):
		player = Player(i)
		drawPlayer = DrawPlayer(surface, 0, i*100)
		drawPlayer.drawBox()
		drawPlayer.drawStringData(player.return_number(), player.return_heart(), player.return_breath(),\
				player.return_xPos(), player.return_yPos())
		drawPlayer.drawGraph(player.return_heartList(), player.return_breathList())
		drawPlayer.drawPosition(player.return_xPos(), player.return_yPos())
		
		combination = []
		combination.append(player)
		combination.append(drawPlayer)
		playerList.append(combination)
	
	dict = {}
	for x in range(5):
		dict["file{0}".format(x)] = open("player{0}".format(x),"r")
	
	pygame.display.flip()
	while True:
		time.sleep(.01)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				for file in dict.values():
					file.close()
				sys.exit()
		
		white = [255, 255, 255]
		surface.fill(white)
		blue = [122,197,205]
		pygame.draw.rect(surface, blue, (500,0,250,500),0)
		#i = 0
		for i in range(5):
			file = dict["file{0}".format(i)]
			line = file.readline()
			line = line.rstrip()
			list = data_parse(line)
			combination = playerList[i]
			player = combination[0]
			drawPlayer = combination[1]
			player.update_all(int(list[0]), int(list[1]),int(list[2]), int(list[3]))
			drawPlayer.drawBox()
			drawPlayer.drawStringData(player.return_number(), player.return_heart(), player.return_breath(),\
				player.return_xPos(), player.return_yPos())
			drawPlayer.drawGraph(player.return_heartList(), player.return_breathList())
			drawPlayer.drawPosition(player.return_xPos(), player.return_yPos())
			#i = i + 1
		
		pygame.display.flip()
		time.sleep(1)
		

if __name__ == '__main__':
	main()