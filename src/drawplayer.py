import pygame
from pygame.locals import *

class DrawPlayer():
	def __init__(self, surface, start_xPos, start_yPos):
		self.surface = surface
		self.start_xPos = start_xPos
		self.start_yPos = start_yPos
		
		self.number = 0
		self.hearth = 0
		self.breath = 0
		self.hearthGraph = []
		self.breathGraph = []
		self.positionCircle = 0
		
	def drawBox(self):
		pygame.draw.line(self.surface, pygame.Color(155,155,155), (self.start_xPos, self.start_yPos), (self.start_xPos+500, self.start_yPos))
		pygame.draw.line(self.surface, pygame.Color(155,155,155), (self.start_xPos, self.start_yPos+100), (self.start_xPos+500, self.start_yPos+100))
		pygame.draw.line(self.surface, pygame.Color(155,155,155), (self.start_xPos, self.start_yPos), (self.start_xPos+100, self.start_yPos))
		pygame.draw.line(self.surface, pygame.Color(155,155,155), (self.start_xPos+500, self.start_yPos), (self.start_xPos+500, self.start_yPos+100))
		pygame.draw.line(self.surface, pygame.Color(155,155,155), (self.start_xPos+250, self.start_yPos), (self.start_xPos+250, self.start_yPos+100))
		
	def drawStringData(self, name, hearth, breath):
		pygame.font.init()
		font = pygame.font.SysFont('Calibri', 15)
		self.number = font.render('#'+str(name), False, (155, 155, 155))
		self.surface.blit(self.number, (0, self.start_yPos))
		
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
		
	def drawPosition(self, xPos, yPos):
		if xPos <= 0:
			xPos = 0
		elif xPos >= 20:
			xPos = 20
		if yPos <= 0:
			yPos = 0
		elif yPos >= 40:
			yPos = 40
		center = [int(xPos*250/20) + 500, int(yPos*500/40)]
		self.positionCircle = pygame.draw.circle(self.surface, (255, 255, 0), center, 5)