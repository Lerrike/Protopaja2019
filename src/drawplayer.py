import pygame
from pygame.locals import *

class DrawPlayer():
	def __init__(self, surface, start_xPos, start_yPos):
		self.surface = surface
		self.start_xPos = start_xPos
		self.start_yPos = start_yPos
		
		pygame.draw.line(self.surface, pygame.Color(155,155,155), (start_xPos, start_yPos), (start_xPos+500, start_yPos))
		pygame.draw.line(self.surface, pygame.Color(155,155,155), (start_xPos, start_yPos+100), (start_xPos+500, start_yPos+100))
		pygame.draw.line(self.surface, pygame.Color(155,155,155), (start_xPos, start_yPos), (start_xPos+100, start_yPos))
		pygame.draw.line(self.surface, pygame.Color(155,155,155), (start_xPos+500, start_yPos), (start_xPos+500, start_yPos+100))
		pygame.draw.line(self.surface, pygame.Color(155,155,155), (start_xPos+250, start_yPos), (start_xPos+250, start_yPos+100))
		
	def drawStringData(self, name, hearth, breath):
		pygame.font.init()
		font = pygame.font.SysFont('Calibri', 30)
		textsurface = font.render('#'+str(name), False, (155, 155, 155))
		self.surface.blit(textsurface, (10, self.start_yPos+10))