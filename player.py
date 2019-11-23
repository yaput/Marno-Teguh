import pygame



class Player(pygame.sprite.Sprite) :
	def __init__(self, x, y) :
		pygame.sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.image = pygame.image.load('Gambar/marnosheet1.png')
		self.rect = self.image.get_rect()
		self.height = 50
		self.width = 35
		self.velo = 0
		self.jatuh = False
		self.napak = False
		self.diem = True
		self.jump = False
		self.acc = 0
		self.hop = 60
		self.images = 5
		self.count = 0
		self.blakang = False
		self.death = False
		
		
	def lompat(self) :
		if self.napak == False :
			return
		self.velo = 8
		self.napak = False
		self.jump = True
		self.diem = True
		self.blakang = False
	
		
	def jalan_kanan(self) :
		self.acc = 0.5
		self.diem = False
		self.blakang = False
		
	def stop(self) :
		self.acc = 0
		self.diem = True
		
	def jalan_kiri(self) :
		self.acc = -2
		self.diem = False
		self.blakang = True
	
	def detectCollisions(self, x1,y1,w1,h1,x2,y2,w2,h2):
 
		if (x2+w2>=x1>=x2 and y2+h2>=y1>=y2):
 
			return True
 
		elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2):
 
			return True
 
		elif (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2):
	 
			return True
	 
		elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2):
	 
			return True
	 
		else:
	 
			return False
			
	
	
							
	def update(self, gravity, listjalan) :
		if self.velo < 0 :
			self.jatuh = True
		
		collision = False
		blockX, blockY = 0, 0
		
		for block in listjalan :
		
			collision = self.detectCollisions(self.x, self.y, self.width, self.height, block.x, block.y, block.width, block.height)
				
				
			if collision == True :
				blockX = block.x
				blockY = block.y
				break
				
		if collision == True :
			if self.jatuh == True :
				self.jatuh = False
				self.napak = True
				self.jump = False
				self.velo = 0
				self.y = blockY - self.height
			
				
		if collision == False :
				self.napak = False
		
		if self.napak == False :	
			self.velo += gravity
		
		self.y -= self.velo
		self.x += self.acc
		
		
		if self.diem == True :
			self.count = 0
		elif self.diem == False :
			if self.count >= self.images -2 :
				self.count = 1
			else :
				self.count+= 1
		
			
	def death(self) :
		if self.y>160 :
			self.death = True
		
	def gambar(self, window) :
		if self.jump == True :
			window.blit(self.image, [self.x, self.y], (4*self.width, 0, self.width, 70))
		else :
			window.blit(self.image, [self.x, self.y],(self.count*self.width, 0, self.width, 70))	
	
		