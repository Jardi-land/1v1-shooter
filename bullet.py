import pygame
from settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos,direct):
        super().__init__()
        self.damage = 10
        if direct:
            # Right
            self.image = pygame.transform.scale(pygame.image.load("game_files/gun_files/SpongeBullet.png").convert_alpha(), (int(15*screen_scale), int(5*screen_scale)))
            self.speed = 100*screen_scale
        else:
            # Left
            self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load("game_files/gun_files/SpongeBullet.png").convert_alpha(), (int(15*screen_scale), int(5*screen_scale))),True,False)
            self.speed = -100*screen_scale

        self.rect = self.image.get_rect(topleft = pos)

    def update(self):
        # Make the bullet travel
        self.rect.x += self.speed
        
        # If bullet isn't in the screen
        if self.rect.x < 0 or self.rect.x > 1920 * screen_scale:
            self.kill()

class Muzzle_flash(pygame.sprite.Sprite):
    def __init__(self,pos,direct):
        super().__init__()
        if direct:
            # Right
            self.image = pygame.transform.scale(pygame.image.load("game_files/gun_files/MuzzleFlash.png").convert_alpha(), (int(40*screen_scale), int(40*screen_scale)))
            self.rect = self.image.get_rect(midleft = pos)
        else:
            # Left
            self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load("game_files/gun_files/MuzzleFlash.png").convert_alpha(), (int(40*screen_scale), int(40*screen_scale))),True,False)
            self.rect = self.image.get_rect(midright = (pos[0] + 15 *screen_scale, pos[1]))
    
    def update(self):
        # Make the Muzzle flash disapear
        self.kill()