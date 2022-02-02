import sys, pygame
from settings import *
import random as rd
from support import import_folder

"""on pourra changer les pouvoir plus tard ^^"""
class PowerUp(pygame.sprite.Sprite):
    def __init__(self, respawn_cooldown_seconds):
        super().__init__()
        self.size_heart = pygame.math.Vector2(int(105*screen_scale), int(105*screen_scale))
        self.size_timer = pygame.math.Vector2(int(87*screen_scale), int(125*screen_scale))
        self.appear_heart = import_folder('game_files/power_ups/heart/appear', self.size_heart.x, self.size_heart.y)
        self.disappear_heart = import_folder('game_files/power_ups/heart/disappear', self.size_timer.x, self.size_timer.y)
        self.appear_timer = import_folder('game_files/power_ups/timer/appear', self.size_timer.x, self.size_timer.y)
        self.disappear_timer = import_folder('game_files/power_ups/timer/disappear', self.size_timer.x, self.size_timer.y)
        self.posible_images = {0:{'appear' : self.appear_heart, 'disappear' : self.disappear_heart},
                               1:{'appear' : self.appear_timer, 'disappear' : self.disappear_timer}}

        self.frame_index = 0
        self.animation_speed = 0.25
        self.disappear = False

        self.posible_pos = self.sort_power_spots(firstmap)
        self.pos, self.power_type = self.pick_spot()

        self.image = self.posible_images[self.power_type]["appear"][0]
        self.rect = self.image.get_rect(topleft=self.pos)
        
        self.has_spawned = False
        self.timer = respawn_cooldown_seconds * DEFAULT_FPS
        self.cooldown = respawn_cooldown_seconds * DEFAULT_FPS


    def draw(self, win):
        self.update()
        self.len_animation = len(self.posible_images[self.power_type]["appear"]) / self.animation_speed
        if self.timer <= self.len_animation and self.timer > 0:
            self.animate = True
        else: self.animate = False
        
        if self.animate:
            self.image = self.posible_images[self.power_type]['appear'][int(self.frame_index)]
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.posible_images[self.power_type]["appear"]):
                self.frame_index = 0
            win.blit(self.image, self.pos)

        if self.has_spawned or self.timer < int(self.animation_speed * 100) + 1:
            win.blit(self.image, self.pos)
        
        if self.disappear:
            self.has_spawned = False
            self.image = self.posible_images[self.power_type]['disappear'][int(self.frame_index)]
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.posible_images[self.power_type]["disappear"]):
                self.disappear = False
                self.frame_index = 0
                self.pick_new_spot()
                self.timer = rd.randint(0, 10) * DEFAULT_FPS + self.cooldown
            else:
                win.blit(self.image, self.pos)
        
    def Reset(self):
        self.disappear = True
        
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
