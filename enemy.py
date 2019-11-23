import pygame

class enemy :
	def __init__(self, x, y) :
		self.x = x
		self.y = y 
		self.image = pygame.image.load('')
		self.rect = self.image.get_rect()