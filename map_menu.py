"""
Creator: @Lorenzo_De_ZEN
"""

import sys, pygame
from settings import *
from tiles import Tiles

screen = pygame.display.set_mode((screen_res[0], screen_res[1]))

class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface
        self.setup_level(level_data)

    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
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
                        Tile = Tiles((platform_x,platform_y),1)
                        self.tiles.add(Tile)
                    elif firstmap[line_i][11-i] == " |":
                        platform_x = platform_x+80
                        Tile = Tiles((platform_x,platform_y),0)
                        self.tiles.add(Tile)
                        platform_x = platform_x-80
                    elif firstmap[line_i][11-i] == "| ":
                        Tile = Tiles((platform_x,platform_y),0)
                        self.tiles.add(Tile)
    def draw(self):
        self.tiles.draw(self.display_surface)