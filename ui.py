import pygame
from settings import *
from support import import_folder

class ui(pygame.sprite.Sprite):
    def __init__(self,player):
        super().__init__()
        if player == 1:
            self.image = pygame.transform.scale(pygame.image.load("game_files/ui/clear/clear_ui5.png").convert_alpha(), (int(385*screen_scale), int(120*screen_scale)))
            self.rect = self.image.get_rect(topleft = (0,0))
        else:
            self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load("game_files/ui/clear/clear_ui5.png").convert_alpha(), (int(385*screen_scale), int(120*screen_scale))),True,False)
            self.rect = self.image.get_rect(topright = (screen_res[0], 0))
        
        self.ui_path = "game_files/ui/clear"

        self.ui_list = import_folder(self.ui_path, int(385*screen_scale), int(120*screen_scale))

    def update(self, player, health):
        if player == 1:
            self.image = self.ui_list[health]
        else:
            self.image = pygame.transform.flip(self.ui_list[health],True,False)

class cooldown_ui(pygame.sprite.Sprite):
    def __init__(self,player):
        super().__init__()
        if player == 1:
            self.image = pygame.transform.scale(pygame.image.load("game_files/ui/cooldown/cooldown_ui6.png").convert_alpha(), (int(385*screen_scale), int(120*screen_scale)))
            self.rect = self.image.get_rect(topleft = (0,0))
        else:
            self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load("game_files/ui/cooldown/cooldown_ui6.png").convert_alpha(), (int(385*screen_scale), int(120*screen_scale))),True,False)
            self.rect = self.image.get_rect(topright = (screen_res[0], 0))

        self.ui_path = "game_files/ui/cooldown"
        
        self.ui_list = import_folder(self.ui_path, int(385*screen_scale), int(120*screen_scale))
    
    def update(self,player,frame):
        if player == 1:
            self.image = self.ui_list[frame]#on load les image et on les convert_alpha() direct c plus opti
        else:
            self.image = pygame.transform.flip(self.ui_list[frame],True,False)

class mugshot(pygame.sprite.Sprite):
    def __init__(self,player,color):
        super().__init__()

        full_path = "game_files/characters/" + color + "/mug_shot/Gunner_mugshot.png"

        if player == 1:
            self.image = pygame.transform.scale(pygame.image.load(full_path).convert_alpha(), (int(110*screen_scale), int(100*screen_scale)))
            self.rect = self.image.get_rect(topleft = (int(10*screen_scale), int(10*screen_scale)))
        else:
            self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load(full_path).convert_alpha(), (int(110*screen_scale), int(100*screen_scale))),True,False)
            self.rect = self.image.get_rect(topright = (screen_res[0] - int(10*screen_scale), int(10*screen_scale)))

class countdown(pygame.sprite.Sprite):
    # C'est pour le countdown 3,2,1 quand le jeux commence.
    def __init__(self):

        super().__init__()
        
        self.img_brut = pygame.image.load(f"game_files/font/font_img/number/1.png").convert_alpha()

        self.image = pygame.transform.scale(pygame.image.load(f"game_files/font/font_img/number/1.png").convert_alpha(), (int(self.img_brut.get_width()*(1/30)*screen_scale), int(self.img_brut.get_height()*(1/30)*screen_scale)))
        
        self.rect = self.image.get_rect(topleft = (screen_res[0]/2 - self.image.get_width()/2, screen_res[1]/3 - self.image.get_height()/2))

    def update(self,cooldown_frame, can_move):
        if can_move:
            self.kill()
        if cooldown_frame > 60:
            self.image = pygame.transform.scale(pygame.image.load(f"game_files/font/font_img/number/1.png"), (int(self.img_brut.get_width()*((cooldown_frame-60)/25)*screen_scale), int(self.img_brut.get_height()*((cooldown_frame-60)/25)*screen_scale)))
        elif cooldown_frame > 30:
            self.image = pygame.transform.scale(pygame.image.load(f"game_files/font/font_img/number/2.png"), (int(self.img_brut.get_width()*((cooldown_frame-30)/25)*screen_scale), int(self.img_brut.get_height()*((cooldown_frame-30)/25)*screen_scale)))
        else:
            self.image = pygame.transform.scale(pygame.image.load(f"game_files/font/font_img/number/3.png"), (int(self.img_brut.get_width()*(cooldown_frame/25)*screen_scale), int(self.img_brut.get_height()*(cooldown_frame/25)*screen_scale)))
        
        self.rect = self.image.get_rect(topleft = (screen_res[0]/2 - self.image.get_width()/2, screen_res[1]/3.5 - self.image.get_height()/2))
