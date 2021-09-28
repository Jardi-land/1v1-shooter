"""
Creator: @Lorenzo_De_ZEN
"""

import sys, pygame
from map_menu import *
from player_one import *

pygame.init()

screen_res = [1920, 1080]
screen_scale = [1920/screen_res[0], 1080/screen_res[1]]
window_name = "1v1 Shooter"

screen = pygame.display.set_mode((screen_res[0], screen_res[1]))
pygame.display.set_caption(window_name)
clock = pygame.time.Clock()

bg_surf = pygame.Surface((1920,1080))
bg_surf.fill((118, 120, 134, 255))

platform_surf = pygame.image.load("game_files/platforms/Platform.png").convert_alpha()
platform_surf = pygame.transform.scale(platform_surf, (165, 155))
platform_thin_surf = pygame.image.load("game_files/platforms/Platform_Thin.png").convert_alpha()
platform_thin_surf = pygame.transform.scale(platform_thin_surf, (85, 155))

platform_x = 1755
platform_y = 925

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(bg_surf,(0,0))
    update_map_menu(platform_y, platform_x, platform_surf, platform_thin_surf)

    pygame.display.update()
    clock.tick(60)