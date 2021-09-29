"""
Creator: @Lorenzo_De_ZEN
"""

import sys, pygame
from settings import *

screen = pygame.display.set_mode((screen_res[0], screen_res[1]))

player_one_surf = pygame.image.load("game_files/characters/green/idle/Gunner_Idle1.png").convert_alpha()
player_one_surf = pygame.transform.scale(player_one_surf, (240, 240))