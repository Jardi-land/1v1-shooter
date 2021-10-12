import pygame
from settings import *

class Tiles(pygame.sprite.Sprite):
    def __init__(self,pos,type):
        super().__init__()
        if type:
            # Normal
            self.image = pygame.transform.scale(pygame.image.load("game_files/platforms/Platform.png").convert_alpha(), (int(165*screen_scale), int(155*screen_scale)))
            self.colliderect = pygame.Rect(pos[0], pos[1] + 55*screen_scale, 165*screen_scale, 100*screen_scale)
        else:
            # Thin
            self.image = pygame.transform.scale(pygame.image.load("game_files/platforms/Platform_Thin.png").convert_alpha(), (int(85*screen_scale), int(155*screen_scale)))
            self.colliderect = pygame.Rect(pos[0], pos[1] + 55*screen_scale, 85*screen_scale, 100*screen_scale)

        self.rect = self.image.get_rect(topleft = pos)
    def update(self,x_shift):
        # Not used for the moment
        self.rect.x += x_shift