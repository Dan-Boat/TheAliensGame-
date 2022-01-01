# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 00:41:33 2021

@author: Boateng
Develop the ship for shooting the aliens
"""
#importing modules 
import pygame

class Ship():
    """Class for ship """
    def __init__(self, screen):
        self.screen = screen
        self.moving_right = False
        self.moving_left = False
        
        #loading image 
        path_to_image = "C:/Users/Boateng/Desktop/Python_Scripts/AlienGame/images/ship.bmp"
        self.image = pygame.image.load(path_to_image)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.screen.get_rect()
        
        #defining the default position of new ship 
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        """Draw the ship current location"""
        self.screen.screen.blit(self.image, self.rect)
    
    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        
        if self.moving_left:
            self.rect.centerx -=1
        
        