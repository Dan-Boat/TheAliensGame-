# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 21:29:34 2022

@author: Boateng
Funtions that controls the movement of the ship
"""
import sys
import pygame 
from bullets import Bullet

            
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
                
            
def update_screen(settings, screen, ship, bullets):
    """updates the screen and flip to the new screen"""
    # redraw the screen during each pass through the loop 
    screen.fill(settings.background_color)
    
    #draw bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    
    #make the updated screen visible
    pygame.display.flip()
    
            