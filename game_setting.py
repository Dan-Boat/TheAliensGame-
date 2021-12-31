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
        self.screen_height = 800
        self.background_color = (230, 230, 230)