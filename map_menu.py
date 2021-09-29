"""
Creator: @Lorenzo_De_ZEN
"""

import sys, pygame
from settings import *

screen = pygame.display.set_mode((screen_res[0], screen_res[1]))

def update_map_menu(platform_y, platform_x, platform_surf, platform_thin_surf):
    for i in range(18):
        if i == 0:
            platform_y = 925
        else:
            platform_y = platform_y-60
        line_i = 17-i
        for i in range(12):
            if i == 0:
                platform_x = 1755
            else:
                platform_x = platform_x-160
            if firstmap[line_i][11-i] == "X":
                screen.blit(platform_surf,(platform_x,platform_y))
            elif firstmap[line_i][11-i] == " |":
                platform_x = platform_x+80
                screen.blit(platform_thin_surf,(platform_x,platform_y))
                platform_x = platform_x-80
            elif firstmap[line_i][11-i] == "| ":
                screen.blit(platform_thin_surf,(platform_x,platform_y))