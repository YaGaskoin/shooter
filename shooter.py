import pygame

class Shooter():
	def __init__(self,screen):
		self.screen = screen
		self.image = pygame.image.load('photo.jpg')
		self.rect =self.image.get_rect()
		self.sc_rect = self.screen.get_rect()
		self.rect.x = 0
		self.rect.centery = self.sc_rect.centery
		self.moving_up = False
		self.moving_down = False
	def blitme(self):
		self.screen.blit(self.image,self.rect)
	def update(self):
		if self.moving_up == True and self.rect.centery >35:
			self.rect.centery-=1
		if self.moving_down == True and self.rect.centery <765:
			self.rect.centery+=1
