"""
Creator: @Lorenzo_De_ZEN
"""

import sys, pygame
from level import *
from player import *
from settings import *
from tiles import Tiles

pygame.init()

screen = pygame.display.set_mode((screen_res[0], screen_res[1]))
pygame.display.set_caption(window_name)
clock = pygame.time.Clock()

bg_surf = pygame.Surface((1920,1080))
bg_surf.fill((118, 120, 134, 255))

platform_x = 1755
platform_y = 925

level = Level(firstmap, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(bg_surf,(0,0))
    level.draw()

    pygame.display.update()
    clock.tick(60)