# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 21:29:34 2022

@author: Boateng
Funtions that controls the movement of the ship
"""
import sys
import pygame 
from bullets import Bullet
from aliens import Alien

            
def check_keydown_events(event, settings, screen, ship, bullets):
    """Respond for key presses."""
   
    if event.key == pygame.K_RIGHT:
        # if the keyword is the right key, move the position
        ship.moving_right = True
        
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)
    elif event.key == pygame.K_q:
        sys.exit()
                
def check_keyup_events(event, ship):
    """Respond for key releases"""                
    
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
            
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
            

def check_events(settings, screen, ship, bullets):
    """It reacts the the keypress and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
            
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
                
            
def update_screen(settings, screen, ship, bullets, aliens):
    """updates the screen and flip to the new screen"""
    # redraw the screen during each pass through the loop 
    screen.fill(settings.background_color)
    
    #draw bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    
    
    #make the updated screen visible
    pygame.display.flip()

    
def get_num_aliens_x(settings, alien_width):
     # define the number of aliens in a row
     # make spacing of aliens equal to one alien width 
     
    available_space_x = settings.screen_width - 2 * alien_width
    num_aliens_x = int(available_space_x / (2*alien_width))
    
    return num_aliens_x

def get_num_rows(settings, ship_height, alien_height):
    
    available_space_y = (settings.screen_height - (3 * alien_height) - ship_height)
    
    num_rows = int(available_space_y / (2 * alien_height))
    
    return num_rows



def create_alien(settings, screen, aliens, alien_number, row_num):
    
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_num
    aliens.add(alien)
    
    
    
def create_fleet(settings, screen, ship, aliens):
    
    """TO create full fleet of aliens"""
    
    alien = Alien(settings, screen)
    num_aliens_x = get_num_aliens_x(settings, alien.rect.width)
    num_rows = get_num_rows(settings, ship.rect.height, alien.rect.height)
    
    #use loop to create a list of aliens 
    
    for row_number in range(num_rows):
        
        for alien_number in range(num_aliens_x):
            
            create_alien(settings, screen, aliens, alien_number, row_number)
        
    
            