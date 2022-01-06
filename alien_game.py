# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 01:14:44 2021

@author: Boateng
"""
#importing modules 
import sys
import pygame
from pygame.sprite import Group

#importing from paths 
from game_setting import Settings
from ship import Ship
import game_functions as gf


class AlienGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Game")
        
        #import ship
        self.ship = Ship(self.screen, self.settings)
        self.bullets = Group()


    def run_game(self):
        """Start the main loop for the game."""
       
        while True:
            # Watch for keyboard and mouse events
            
            gf.check_events(self.settings, self.screen, self.ship, self.bullets)
            self.ship.update()

            # Redraw the screen during each pass through the loop.
            # Make the most recently drawn screen visible.
            self.bullets.update()
            gf.update_screen(self.settings, self.screen, self.ship, self.bullets)

            
            #pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienGame()
    ai.run_game()
