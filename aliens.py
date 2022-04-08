# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 17:53:19 2022

@author: Boateng
"""
import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
    
    "This class indicates a single alien in the fleet"
    
    def __init__(self, setting, screen):
        super().__init__()
        self.setting = setting 
        self.screen = screen
        
        #loading of image 
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        
        #defining position of the alien at the top left 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        
    def blitme(self):
        # draw the aliens current positon
        
        self.screen.blit(self.image, self.rect)