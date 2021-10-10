import pygame
from settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos,direct):
        super().__init__()
        if direct:
            self.image = pygame.transform.scale(pygame.image.load("game_files/gun_files/SpongeBullet.png").convert_alpha(), (int(15*screen_scale), int(5*screen_scale)))
            self.speed = 50
        else:
            self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load("game_files/gun_files/SpongeBullet.png").convert_alpha(), (int(15*screen_scale), int(5*screen_scale))),True,False)
            self.speed = -40

        self.rect = self.image.get_rect(topleft = pos)

    def update(self):
        self.rect.x += self.speed