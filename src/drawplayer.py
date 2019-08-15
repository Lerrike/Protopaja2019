import pygame
from pygame.locals import *

#Pygame draw class. Draws the different sections to the pygame screen. DrawStringData draws readable data.
#DrawGraph draws the graph. DrawPosition draws the position.
class DrawPlayer():
	def __init__(self, surface, start_xPos, start_yPos):
		self.surface = surface
		self.start_xPos = start_xPos
		self.start_yPos = start_yPos
		
		self.number = 0
		self.hearth = 0
		self.breath = 0
		self.position = 0
		self.hearthGraph = []
		self.breathGraph = []
		self.positionCircle = 0
		
	def drawBox(self):
		pygame.draw.line(self.surface, pygame.Color(155,155,155), (self.start_xPos, self.start_yPos), (self.start_xPos+500, self.start_yPos))
		pygame.draw.line(self.surface, pygame.Color(155,155,155), (self.start_xPos, self.start_yPos+100), (self.start_xPos+500, self.start_yPos+100))
		pygame.draw.line(self.surface, pygame.Color(155,155,155), (self.start_xPos, self.start_yPos), (self.start_xPos+100, self.start_yPos))
		pygame.draw.line(self.surface, pygame.Color(155,155,155), (self.start_xPos+500, self.start_yPos), (self.start_xPos+500, self.start_yPos+100))
		pygame.draw.line(self.surface, pygame.Color(155,155,155), (self.start_xPos+250, self.start_yPos), (self.start_xPos+250, self.start_yPos+100))
		
	def drawStringData(self, name, hearth, breath, xPos, yPos):
		pygame.font.init()
		font = pygame.font.SysFont('Calibri', 15)
		self.number = font.render('#'+str(name), False, (0, 0, 0))
		self.surface.blit(self.number, (0, self.start_yPos))
		
		self.position = font.render('xPos:'+str(xPos)+", yPos:"+str(yPos), False, (0, 0, 0))
		self.surface.blit(self.position, (0, self.start_yPos+25))
		
		self.hearth = font.render('Current Heart:'+str(hearth), False, (255, 0, 0))
		self.surface.blit(self.hearth, (0, self.start_yPos+50))
		
		self.breath = font.render('Current Breath:'+str(breath), False, (0, 0, 255))
		self.surface.blit(self.breath, (0, self.start_yPos+75))
		
	def drawGraph(self, hearthList, breathList):
		pygame.draw.line(self.surface, pygame.Color(0, 0,0), (self.start_xPos+250+250, self.start_yPos), (self.start_xPos+250+250, self.start_yPos+100))
		
		i = 0
		prev_value = 0
		for value in hearthList:
			if prev_value:
				pygame.draw.line(self.surface, pygame.Color(255, 0,0), (self.start_xPos+250+250-i, self.start_yPos+100-prev_value/2), (self.start_xPos+250+250-i-1, self.start_yPos+100-value/2))
			prev_value = value
			i = i + 1
		
		i = 0
		prev_value = 0
		for value in breathList:
			if prev_value:
				pygame.draw.line(self.surface, pygame.Color(0, 0,255), (self.start_xPos+250+250-i, self.start_yPos+100-prev_value/2), (self.start_xPos+250+250-i-1, self.start_yPos+100-value/2))
			prev_value = value
			i = i + 1
		
	def drawPosition(self, xPos, yPos, name):
		#Limits the positions inside bounds.
		xPos = xPos + 1 #These two maps (0,0) to "1,1" on screen in a 5x5m square
		yPos = yPos + 1
		if xPos <= 0:
			xPos = 0
		elif xPos >= 5:
			xPos = 5
		if yPos <= 0:
			yPos = 0
		elif yPos >= 5:
			yPos = 5
		#Maps real life meters into pixels on the screen.
		xPos = int((xPos)*250/5) + 500 #Change these if neccessary.
		yPos = int((yPos)*250/5)
		center = [xPos, yPos]
		self.positionCircle = pygame.draw.circle(self.surface, (255, 255, 0), center, 10)
		
		pygame.font.init()
		font = pygame.font.SysFont('Calibri', 15)
		self.number = font.render(str(name), False, (0, 0, 0))
		self.surface.blit(self.number, (xPos-4, yPos-7))
		