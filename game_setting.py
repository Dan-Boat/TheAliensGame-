# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 00:35:48 2021

@author: Boateng
Defining game settings
"""
class Settings():
    """ A class for declaring the settings of the game"""
    def __init__(self):
        # Initialize the game settings (pixels, color)
        self.screen_width = 1200
        self.screen_height = 600
        self.background_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        
        # bullet settings 
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height =15
        self.bullet_color = 60,60,60