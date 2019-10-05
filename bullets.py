import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self,shooter,settings,screen):
		super(Bullet,self).__init__()
		self.screen = screen
		self.rect = pygame.Rect(0,0,settings.bullet_width,settings.bullet_height)
		self.rect.centery  = shooter.rect.centery
		self.rect.x = shooter.rect.x
		self.rect.right = shooter.rect.right
		self.color = (0,255,0)
	def draw_bullet(self):
		pygame.draw.rect(self.screen,self.color,self.rect)
	def update(self):
		self.rect.x+=1
		
