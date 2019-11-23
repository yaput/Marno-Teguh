import pygame

class Jalan(pygame.sprite.Sprite) :
	def __init__(self, x, y) :
		self.x = x
		self.y = y
		self.image = pygame.image.load('Gambar/jalan.png')
		self.rect = self.image.get_rect()
		self.height = 60
		self.width = 40
		self.gerak = 8
		
	
	def update(self) :
		self.x -= self.gerak
		
	def stopupdate(self) :
		self.x += 0
		
	def gambar(self, window) :
		window.blit(self.image, [self.x, self.y])
		
		

class Kotak:
	def __init__(self, x, y) :
		self.x = x
		self.y = y 
		self.width = 40
		self.height = 40
		self.gerak = 8
		
	def update(self) :
		self.x -= self.gerak
	
	def stopupdate(self) :
		self.x += 0
		
	def gambar(self, window) :
		pygame.draw.rect(window, (255, 255, 255), (self.x,self.y,self.width,self.height), 0)
	