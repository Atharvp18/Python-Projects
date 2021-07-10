import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
    #For initializing game ,settings and screen object
    pygame.init()
    #For creating a screen object
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Create play button
    play_button = Button(ai_settings,screen,"Play")

    #Create a stats instance & create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    
    #Making a ship, a group of bullets & aliens
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    
    #Create a fleet of aliens
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #Main loop for the game
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update() 
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets) 
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets) 
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button) 
       
run_game()                
