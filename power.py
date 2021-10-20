import sys, pygame
from settings import *
import random as rd

class PowerUp:
    def __init__(self):
        self.posible_pos = self.sort_power_spots(firstmap)
        self.pos = self.pick_spot()
        self.size = pygame.math.Vector2(int(100*screen_scale), int(100*screen_scale))
        self.rect = pygame.Rect(self.pos, self.size)

    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), self.rect)

    def sort_power_spots(self, map):
        f = []
        for y in range(len(map)-1):
            for x in range(len(map[y])-1):
                if map[y][x] == 'PW':
                    f.append((x, y))
        return f


    def pick_spot(self):
        pos = self.posible_pos[rd.randint(0, len(self.posible_pos)-1)]
        return pygame.math.Vector2(int((screen_res[0]/len(firstmap[pos[1]]))*pos[0]), int((screen_res[1]/len(firstmap))*pos[1]))

    def pick_new_spot(self):
        new : pygame.math.Vector2 = self.pick_spot()
        if self.pos == new:
            self.pick_new_spot()
        else:
            self.pos = new
            self.rect.x, self.rect.y = new.x, new.y
        
#####################################################################################
###############     W. I. P.
#####################################################################################
