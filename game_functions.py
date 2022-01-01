# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 21:29:34 2022

@author: Boateng
Funtions that controls the movement of the ship
"""
import sys


import pygame 

def check_events(ship):
    """It reacts the the keypress and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # if the keyword is the right key, move the position
                
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                
                ship.moving_left = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
                
                
            
def update_screen(ai_settings, screen, ship):
    """updates the screen and flip to the new screen"""
    # redraw the screen during each pass through the loop 
    screen.fill(ai_settings.background_color)
    ship.blitme()
    
    #make the updated screen visible
    pygame.display.flip()
    
            