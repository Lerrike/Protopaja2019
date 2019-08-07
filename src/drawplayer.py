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
		
		self.hearth = font.render('Hearth:'+str(hearth), False, (255, 0, 0))
		self.surface.blit(self.hearth, (0, self.start_yPos+50))
		
		self.breath = font.render('Breath:'+str(breath), False, (0, 0, 255))
		self.surface.blit(self.breath, (125, self.start_yPos+50))
		
	def drawGraph(self, hearthList, breathList):
		pygame.draw.line(self.surface, pygame.Color(0, 0,0), (self.start_xPos+250+240, self.start_yPos), (self.start_xPos+250+240, self.start_yPos+100))
		
		i = 0
		prev_value = 0
		for value in hearthList:
			if prev_value:
				pygame.draw.line(self.surface, pygame.Color(255, 0,0), (self.start_xPos+250+240-i, self.start_yPos+100-prev_value/2), (self.start_xPos+250+240-i-1, self.start_yPos+100-value/2))
			prev_value = value
			i = i + 1
		
		i = 0
		prev_value = 0
		for value in breathList:
			if prev_value:
				pygame.draw.line(self.surface, pygame.Color(0, 0,255), (self.start_xPos+250+240-i, self.start_yPos+100-prev_value/2), (self.start_xPos+250+240-i-1, self.start_yPos+100-value/2))
			prev_value = value
			i = i + 1
		
	def drawPosition(self, xPos, yPos):
		center = [xPos + 500, yPos]
		self.positionCircle = pygame.draw.circle(self.surface, (155, 155, 155), center, 5)