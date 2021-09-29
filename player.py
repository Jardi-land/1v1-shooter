"""
Creator: @Lorenzo_De_ZEN
"""

import sys, pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((100,150))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft = pos)