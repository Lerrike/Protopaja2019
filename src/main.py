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
	
	logo = pygame.image.load("Aboense(musta).png")
	logo = pygame.transform.scale(logo, (250,250))
	
	white = [255, 255, 255]
	blue = [81,167,249]
	#surface.fill(white)
	#pygame.draw.rect(surface, blue, (500,0,250,500),0)
	
	#playerList = [] #A combination of player and drawplayer classes in case if useful.
	#for i in range(5):
	#	player = Player(i)
	#	drawPlayer = DrawPlayer(surface, 0, i*100)
		#drawPlayer.drawBox()
		#drawPlayer.drawStringData(player.return_number(), player.return_heart(), player.return_breath(),\
		#		player.return_xPos(), player.return_yPos())
		#drawPlayer.drawGraph(player.return_heartList(), player.return_breathList())
		#drawPlayer.drawPosition(player.return_xPos(), player.return_yPos(), player.return_number())
		
	#	combination = []
	#	combination.append(player)
	#	combination.append(drawPlayer)
	#	playerList.append(combination)
		
	sock = socket.socket() #
	sock.settimeout(1) #
	sock.bind(('0.0.0.0', 8090 )) #
	sock.listen(0) #
	
	#dict = {}
	#for x in range(5):
	#	dict["file{0}".format(x)] = open("player{0}".format(x),"r")
	
	pygame.display.flip()
	playerList = []
	while True:
		time.sleep(.01)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				#for file in dict.values():
				#	file.close()
				if client:
					client.close()
				sys.exit()
		
		surface.fill(white)
		pygame.draw.rect(surface, blue, (500,0,250,250),0)
		pygame.draw.line(surface, pygame.Color(0,0,0), (550, 50), (700, 50))
		pygame.draw.line(surface, pygame.Color(0,0,0), (550, 200), (700,200))
		pygame.draw.line(surface, pygame.Color(0,0,0), (550, 50), (550, 200))
		pygame.draw.line(surface, pygame.Color(0,0,0), (700, 50), (700, 200))
		surface.blit(logo, (500, 250))
		client = 0
		
		try:
			client, addr = sock.accept()
			#file = dict["file{0}".format(i)]
			#line = file.readline()
			content = client.recv(1024)
			line = content.decode('utf-8')
			line = line.rstrip()
			list = data_parse(line)
			print(list)
			
			condition = False
			for sublist in playerList:
				if sublist[0].return_name() == list[0]:
					condition = True
					break
			if not condition:
				player = Player(list[0])
				drawPlayer = DrawPlayer(surface, 0, len(playerList)*100)
				sublist = [player, drawPlayer]
				playerList.append(sublist)
			else:
				combination = 0
				for sublist in playerList:
					if list[0] == sublist[0].return_name():
						combination = sublist
						break
				player = combination[0]
				drawPlayer = combination[1]
				player.update_all(float(list[1]), float(list[2]), int(list[3]), int(list[4]))
			for sublist in playerList:
				player = sublist[0]
				drawPlayer = sublist[1]
				drawPlayer.drawBox()
				drawPlayer.drawStringData(player.return_name(), player.return_heart(), player.return_breath(),\
					player.return_xPos(), player.return_yPos())
				drawPlayer.drawGraph(player.return_heartList(), player.return_breathList())
				drawPlayer.drawPosition(player.return_xPos(), player.return_yPos(), player.return_name())
			pygame.display.flip()
			
		except socket.timeout:
			print("Timeout, trying again.")
		except IndexError:
			print("Index out of bound")
		
		time.sleep(.1)
		

if __name__ == '__main__':
	main()