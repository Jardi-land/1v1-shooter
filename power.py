import sys, pygame
from setting import *
import random as rd

class PowerUp:
    def __init__(self):
        self.powrt_id = {0:'instant_reload', 1:'double_double-jump'}
        self.pos = self.pick_spot()
        self.size = pygame.math.Vector2(100*screen_scale, 50*screen_scale)
        self.rect = pygame.Rect(self.pos, self.size)
        self.power = rd.randint(0, len(self.powrt_id)-1)

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), self.rect)

    def pick_spot(self):
        pos = []
        while len(pos) < 2:
            y = rd.randint(0, len(firstmap))
            x = rd.randint(0, len(firstmap[0]))
            if firstmap[x][y] != 'PW':
                continue
            else:
                pos.append(x)
                pos.append(y)
                break
        return pygame.math.Vector2(pos[0], pos[1])
        
#####################################################################################
###############     W. I. P.
#####################################################################################
