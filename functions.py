import pygame
import sys
from shooter import Shooter
from settings import Settings
from bullets import Bullet
from pygame.sprite import Group

def check_events(shooter,settings,screen,bullets):
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					shooter.moving_up = True
				if event.key == pygame.K_DOWN:
					shooter.moving_down = True
				if event.key == pygame.K_SPACE:
					bullet = Bullet(shooter,settings,screen)
					bullets.add(bullet)
					
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					shooter.moving_up = False
				if event.key == pygame.K_DOWN:
					shooter.moving_down = False
				
					
	
def run_game():
	settings = Settings()
	pygame.init()
	bullets = Group()
	screen =pygame.display.set_mode((settings.sc_width,settings.sc_height))
	pygame.display.set_caption('kekrk')
	bg_color =settings.color
	human = Shooter(screen)

	while True:
		check_events(human,settings,screen,bullets)
		screen.fill(bg_color)
		human.update()
		bullets.update()
		for bullet in bullets.sprites():
			bullet.draw_bullet()
		for bullet in bullets.copy():
			if bullet.rect.x >= 1175:
				bullets.remove(bullet)
		human.blitme()
		pygame.display.flip()

run_game()
