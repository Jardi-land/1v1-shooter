import pygame

class Tiles(pygame.sprite.Sprite):
    def __init__(self,pos,type):
        super().__init__()
        if type:
            self.image = pygame.transform.scale(pygame.image.load("game_files/platforms/Platform.png").convert_alpha(), (165, 155))
            self.colliderect = pygame.Rect(pos[0], pos[1] + 55, 165, 60)
        else:
            self.image = pygame.transform.scale(pygame.image.load("game_files/platforms/Platform_Thin.png").convert_alpha(), (85, 155))
            self.colliderect = pygame.Rect(pos[0], pos[1] + 55, 85, 60)

        self.rect = self.image.get_rect(topleft = pos)
        #self.colliderect = self.image.get_rect(topleft = (pos[0], pos[1] + 55))
    def update(self,x_shift):
        self.rect.x += x_shift