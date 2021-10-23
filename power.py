import sys, pygame
from settings import *
import random as rd
from menu import txt
from support import import_folder

#####################################################################################
###############     W. I. P.
#####################################################################################
"""on pourra changer les pouvoir plus tard ^^"""
class PowerUp:
    def __init__(self, respawn_cooldown_seconds):
        self.size = pygame.math.Vector2(int(100*screen_scale), int(100*screen_scale))
        self.posible_images = import_folder('game_files/power_ups', self.size.x, self.size.y)
        print(len(self.posible_images), self.posible_images)

        self.posible_pos = self.sort_power_spots(firstmap)
        self.pos, self.pow_img_index = self.pick_spot()

        self.image = self.posible_images[self.pow_img_index]
        self.rect = self.image.get_rect(topleft=self.pos)
        
        self.has_spawned = False
        self.timer = respawn_cooldown_seconds * DEFAULT_FPS
        self.cooldown = respawn_cooldown_seconds * DEFAULT_FPS

    def draw(self, win):
        self.update()
        if self.timer <= 255:
            self.image.set_alpha(255-self.timer)
            win.blit(self.image, self.pos)
        
    def Reset(self):
        self.has_spawned = False
        self.pick_new_spot()
        self.timer = rd.randint(0, 10) * DEFAULT_FPS + self.cooldown

    def update(self):
        self.timer -= 1
        if self.timer < 0:
            self.has_spawned = True

    def sort_power_spots(self, map):
        f = []
        for y in range(len(map)-1):
            for x in range(len(map[y])-1):
                if map[y][x] == 'PW':
                    f.append((x, y))
        
        return f

    def pick_spot(self):
        pos = self.posible_pos[rd.randint(0, len(self.posible_pos)-1)]
        p = pygame.math.Vector2(int((screen_res[0]/len(firstmap[pos[1]]))*pos[0]), int((screen_res[1]/len(firstmap))*pos[1]))
        index = rd.randint(0, len(self.posible_images)-1)
        print('index: ', index)
        return p, index

    def pick_new_spot(self):
        new, new_pwr = self.pick_spot()
        if self.pos == new:
            self.pick_new_spot()
        else:
            self.pos = new
            self.rect.x, self.rect.y = new.x, new.y
            self.pow_img_index = new_pwr
        
