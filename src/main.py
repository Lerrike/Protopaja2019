import pygame, sys, time, socket
from pygame.locals import *
from player import Player
from drawplayer import DrawPlayer
from Data_parse import data_parse

#Initializes pygame and has main loop. In the main loop receives data and draws it using Player and DrawPlayer.
def main():
	pygame.init()
	surface = pygame.display.set_mode((750,500))
	pygame.display.set_caption('Aboense')
	
	white = [255, 255, 255]
	surface.fill(white)
	blue = [122,197,205]
	pygame.draw.rect(surface, blue, (500,0,250,500),0)
	
	playerList = [] #A combination of player and drawplayer classes in case if useful.
	for i in range(5):
		player = Player(i)
		drawPlayer = DrawPlayer(surface, 0, i*100)
		#drawPlayer.drawBox()
		#drawPlayer.drawStringData(player.return_number(), player.return_heart(), player.return_breath(),\
		#		player.return_xPos(), player.return_yPos())
		#drawPlayer.drawGraph(player.return_heartList(), player.return_breathList())
		#drawPlayer.drawPosition(player.return_xPos(), player.return_yPos(), player.return_number())
		
		combination = []
		combination.append(player)
		combination.append(drawPlayer)
		playerList.append(combination)
		
	sock = socket.socket() #
	sock.settimeout(2) #
	sock.bind(('0.0.0.0', 8090 )) #
	sock.listen(0) #
	
	#dict = {}
	#for x in range(5):
	#	dict["file{0}".format(x)] = open("player{0}".format(x),"r")
	
	pygame.display.flip()
	while True:
		time.sleep(.01)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				#for file in dict.values():
				#	file.close()
				client.close()
				sys.exit()
		
		white = [255, 255, 255]
		surface.fill(white)
		blue = [122,197,205]
		pygame.draw.rect(surface, blue, (500,0,250,500),0)
		try:
			client, addr = sock.accept()
			for i in range(1):
				#file = dict["file{0}".format(i)]
				#line = file.readline()
				content = client.recv(1024)
				line = content.decode('utf-8')
				line = line.rstrip()
				list = data_parse(line)
				combination = playerList[i]
				player = combination[0]
				drawPlayer = combination[1]
				print(list)
				player.update_all(float(list[0]), float(list[1]), float(list[2]), float(list[3]))
				drawPlayer.drawBox()
				drawPlayer.drawStringData(player.return_number(), player.return_heart(), player.return_breath(),\
					player.return_xPos(), player.return_yPos())
				drawPlayer.drawGraph(player.return_heartList(), player.return_breathList())
				drawPlayer.drawPosition(player.return_xPos(), player.return_yPos(), player.return_number())
			pygame.display.flip()
			
		except socket.timeout:
			print("Timeout, trying again.")
		
		time.sleep(.1)
		

if __name__ == '__main__':
	main()