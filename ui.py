import pygame
from settings import *
from support import import_folder

class ui(pygame.sprite.Sprite):
    def __init__(self,player):
        super().__init__()
        if player == 1:
            self.image = pygame.transform.scale(pygame.image.load("game_files/ui/clear_ui5.png").convert_alpha(), (int(385*screen_scale), int(120*screen_scale)))
            self.rect = self.image.get_rect(topleft = (0,0))
        else:
            self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load("game_files/ui/clear_ui5.png").convert_alpha(), (int(385*screen_scale), int(120*screen_scale))),True,False)
            self.rect = self.image.get_rect(topright = (screen_res[0], 0))
        
        self.ui_path = "game_files/ui"

        self.ui_list = import_folder(self.ui_path, int(385*screen_scale), int(120*screen_scale))

    def update(self, player, health):
        if player == 1:
            self.image = self.ui_list[health].convert_alpha()
        else:
            self.image = pygame.transform.flip(self.ui_list[health],True,False).convert_alpha()