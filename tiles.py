import pygame

class Tiles(pygame.sprite.Sprite):
    def __init__(self,pos,type):
        super().__init__()
        if type:
            self.image = pygame.transform.scale(pygame.image.load("game_files/platforms/Platform.png").convert_alpha(), (165, 155))
        else:
            self.image = pygame.transform.scale(pygame.image.load("game_files/platforms/Platform_Thin.png").convert_alpha(), (85, 155))
        self.rect = self.image.get_rect(topleft = pos)
    def update(self,x_shift):
        self.rect.x += x_shift