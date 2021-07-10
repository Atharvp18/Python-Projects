import sys
import pygame
from game_stats import GameStats
import pygame.sprite
from time import sleep
from bullet import Bullet
from alien import Alien
import sound_effects as se

#Checks for keypress
def check_keydown_events(event,ai_settings,screen,stats,ship,bullets):
    if event.key == pygame.K_d:
        ship.moving_right = True

    elif event.key == pygame.K_a:
        ship.moving_left = True

    elif event.key == pygame.K_w:
        ship.moving_up = True

    elif event.key == pygame.K_s:
        ship.moving_down = True        
    
    elif event.key == pygame.K_p:
        stats.game_active = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)    

#Checks for keyrelease
def check_keyup_events(event,ship): 
    if event.key == pygame.K_d:
        ship.moving_right = False  

    elif event.key == pygame.K_a:
        ship.moving_left = False  

    elif event.key == pygame.K_w:
        ship.moving_up = False

    elif event.key == pygame.K_s:
        ship.moving_down = False           

def fire_bullet(ai_settings,screen,ship,bullets):
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        se.bullet_sound.play()
        se.bullet_sound.set_volume(0.7)
 
def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    #Detects all the events of mouse and keyboard
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,stats,ship,bullets)
                
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)   

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    #Reset the stats & start a new game when play is clicked
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #Reset the game settings
        ai_settings.initialize_dynamic_settings()

        #Hide mouse cursor
        pygame.mouse.set_visible(False)    
        stats.reset_stats()
        stats.game_active = True

        #Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        #Empty the groups of aliens and bullets
        aliens.empty()
        bullets.empty()

        #Create a new fleet of aliens & center the ship
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    #Update bullet positions
    bullets.update()

    #Get rid of bullets when they go above the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)        

def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    #Check for any bullets that have hit aliens and remove them both
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points
            sb.prep_score()
            se.alien_sound.play()
            se.alien_sound.set_volume(0.7)
        check_high_score(stats,sb)    

    if len(aliens) == 0:
        #If all the aliens die delete bullets,speed up game and make new fleet,start a new level
        bullets.empty()
        ai_settings.increase_speed()
        #Increase Level
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings,screen,ship,aliens)

def update_screen(ai_settings,screen,stats,sb,ship,alien,bullets,play_button):
    #Give background color everytime the loop runs
    background_image = pygame.image.load("images/background.png").convert()
    screen.blit(background_image, [0, 0])
    #Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.draw(screen)

    #Draw the score
    sb.show_score()

    #Draw the play button when game is inactive
    if not stats.game_active:
        play_button.draw_button()
        
    #Update the screen every second
    pygame.display.flip()

def get_number_aliens_x(ai_settings,alien_width):
    #Find the number of aliens which can fit in a row
    available_space_X = ai_settings.screen_width - (2*alien_width)      
    number_aliens_x = int(available_space_X / (2*alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    #Find the number of rows of aliens that can fit 
    available_space_y = (ai_settings.screen_height-(3*alien_height)-ship_height)
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    #Create an alien & find space between aliens should be equal to one alien width
    alien = Alien(ai_settings,screen)
    alien.x = alien.rect.width + (2*alien.rect.width*alien_number)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + (2*alien.rect.height*row_number)
    aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
    #Create an alien and find the number of aliens in a row
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)  
    
    #Creating the first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            #Creating aliens and placing them in rows
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets):
    if stats.ships_left > 0:
        #Decrement ships left
        stats.ships_left -=1
        se.lose_sound.play()
        se.lose_sound.set_volume(0.7)

        #Update scoreboard
        sb.prep_ships()

        #Empty the groups: aliens and bullets
        aliens.empty()
        bullets.empty()

        #Creating a new fleet and centering the ship
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

        sleep(0.5)

    else:
        stats.game_active = False   
        pygame.mouse.set_visible(True) 

def check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        #Check if any aliens have reached the bottom of the screen
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
            break

def update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets):
    #Updating the aliens position
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    #Check alien-ship collision
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)

    #Check for aliens hitting the bottom
    check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets)    

def check_high_score(stats,sb):
    #Check if there is a new high score
    if stats.score > stats.high_score:
        stats.high_score = stats.score    
        sb.prep_high_score()