from os import walk
import pygame

def import_folder(path, x, y):
    surface_list = []

    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + "/" + image
            image_surf = pygame.transform.scale(pygame.image.load(full_path).convert_alpha(), (int(x), int(y))).convert_alpha()
            surface_list.append(image_surf)
    
    return surface_list

"""Test class for animating sprites !!still need to be tested!!"""
class animation:
    @classmethod
    def __init__(self, x, y,  imgs : list, dt : float):
        self.pos = pygame.math.Vector2(x, y)
        self.images = imgs
        self.image_count = len(self.images)
        self.interval = dt
        self.total_time = self.image_count * self.interval
        self.timer = 0
        self.index = 0
        self.restart_when_finished = True

    @classmethod
    def __init__(self, x, y, imgs : list, tot_time : float):
        self.pos = pygame.math.Vector2(x, y)
        self.images = imgs
        self.image_count = len(self.images)
        self.total_time = tot_time
        self.interval = self.total_time / self.image_count
        self.timer = 0
        self.index = 0
        self.restart_when_finished = True

    def update(self, dt : float):
        self.timer += dt

        if self.timer >= self.interval:
            self.index += 1
            self.timer = 0

        if self.index > len(self.images) - 1:
            if self.restart_when_finished:
                self.index = 0
            else:
                self.index = len(self.images) - 1

    def draw(self, win):
        win.blit(self.images[self.index], self.pos)

    def set_animation_settings(self, imgs : list = {}, interval_time = 0, tot_time = 0):
        if imgs != {}:
            self.images = imgs
        
        if interval_time != 0:
            self.interval = interval_time

        if tot_time != 0:
            self.total_time = tot_time