import sys, pygame
from settings import *
import random as rd
from menu import txt
from support import import_folder

"""on pourra changer les pouvoir plus tard ^^"""
class PowerUp(pygame.sprite.Sprite):
    def __init__(self, respawn_cooldown_seconds):
        super().__init__()
        
        self.size = pygame.math.Vector2(int(125*screen_scale), int(125*screen_scale))
        appear = import_folder('game_files/power_ups/heart/appear', self.size.x, self.size.y)
        disappear = import_folder('game_files/power_ups/heart/disappear', self.size.x, self.size.y)
        self.posible_images = {0:{'appear' : appear, 'disappear' : disappear},
                               1:{'appear' : appear, 'disappear' : disappear}}

        self.frame_index = 0
        self.animation_speed = 0.125
        self.power_up_anim_finish = False

        self.posible_pos = self.sort_power_spots(firstmap)
        self.pos, self.power_type = self.pick_spot()

        self.image = appear[0]
        self.rect = self.image.get_rect(topleft=self.pos)
        
        self.has_spawned = False
        self.timer = respawn_cooldown_seconds * DEFAULT_FPS
        self.cooldown = respawn_cooldown_seconds * DEFAULT_FPS

    def draw(self, win):
        self.update()
        self.len_animation = len(self.posible_images[0]["appear"]) / self.animation_speed
        if self.timer <= self.len_animation and self.timer > 0:
            self.animate = True
        else: self.animate = False
        
        if self.animate:
            self.image = self.posible_images[0]['appear'][int(self.frame_index)]
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.posible_images[self.power_type]["appear"]):
                self.power_up_anim_finish = True
                self.frame_index = 0
            win.blit(self.image, self.pos)

        if self.has_spawned or self.timer < int(self.animation_speed * 100) + 1:
            win.blit(self.image, self.pos)
        
        
        # if self.timer <= 240/len(appear)
        # self.frame_index += self.animation_speed
        # self.image = self.posible_images[0]['appear'][int(self.frame_index)]

        # if self.frame_index >= len(self.posible_images[self.power_type]["appear"]):
        #     self.frame_index = 0

        # win.blit(self.image, self.pos)
        
    def Reset(self):
        self.has_spawned = False
        self.pick_new_spot()
        self.image = self.posible_images[0]
        self.timer = rd.randint(0, 10) * DEFAULT_FPS + self.cooldown

    def update(self):
        #for testing
        if TESTING:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_h]:
                self.force_heal()
            elif keys[pygame.K_g]:
                self.force_ammo()
            elif keys[pygame.K_j]:
                self.timer = 10
            elif keys[pygame.K_r]:
                self.Reset()
        ######################

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
        return p, index

    def pick_new_spot(self):
        new, new_pwr = self.pick_spot()
        if self.pos == new:
            self.pick_new_spot()
        else:
            self.pos = new
            self.rect.x, self.rect.y = new.x, new.y
            self.power_type = new_pwr

    ####################################
    ## FOR TESTING ONLY
    ####################################

    def force_heal(self):
        self.Reset()
        self.power_type = 0
        self.image = self.posible_images[self.power_type]

    def force_ammo(self):
        self.Reset()
        self.power_type = 1
        self.image = self.posible_images[self.power_type]
