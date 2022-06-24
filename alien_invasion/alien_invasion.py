import pygame
from pygame.sprite import Group
import game_functions as gf

from settings import Settings
from game_stats import GameStats
from ship import Ship
from button import Button
from scoreboard import Scoreboard

def run_game():
	# Initialize game, settings and screen objects.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, \
									 ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# Make the play button.
	play_button = Button(ai_settings, screen, "Play")
	
	
	# Create an instance to store game statistics and create scoreboard.
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	
	# Make a ship, a group of aliens and a group of bullets.
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	
	# Start the main loop for the game.
	while True:
		gf.check_events(ai_settings, screen, stats, sb, play_button, \
						ship, aliens, bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, \
							  aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, \
							 bullets)
							 
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, \
						 bullets, play_button)	

		
run_game()
