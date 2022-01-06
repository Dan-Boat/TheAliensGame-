# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 00:39:33 2022

@author: Boateng
"""
import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):
    """class to manage the bullet routines"""
    def __init__(self, settings, screen, ship):
        super().__init__()
        self.screen =screen
        
        #create bullet positon and set its correct position
        self.rect = pygame.Rect(0,0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor
        
        
    def update(self):
        """move bullet up"""
        self.y -= self.speed_factor
        self.rect.y = self.y 
        
    def draw_bullet(self):
        """draw bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)