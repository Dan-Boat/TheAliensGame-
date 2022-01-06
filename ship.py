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
    def __init__(self,screen,settings):
        self.screen = screen
        self.settings = settings
        
        self.moving_right = False
        self.moving_left = False
        
        #loading image 
        path_to_image = "C:/Users/Boateng/Desktop/Python_Scripts/AlienGame/images/ship.bmp"
        self.image = pygame.image.load(path_to_image)
        self.rect = self.image.get_rect()
        
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
       
        
        #defining the default position of new ship 
        self.center = float(self.rect.centerx)
       
       
        
    def blitme(self):
        """Draw the ship current location"""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        # limiting the movement outside the screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor
        
        # update the rect object to the center 
        self.rect.centerx = self.center
        
        