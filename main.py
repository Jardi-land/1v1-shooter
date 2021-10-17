"""
Creator: @Lorenzo_De_ZEN
"""

import sys, pygame
from level import *
from player import *
from settings import *
from tiles import Tiles
from menu import main_menu

pygame.init()
def main():

    screen = pygame.display.set_mode((screen_res[0], screen_res[1]))
    pygame.display.set_caption(window_name)
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(mouse_visible)

    bg_surf = pygame.Surface((screen_res[0], screen_res[1]))
    bg_surf.fill((118, 120, 134, 255))


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

if __name__ == '__main__':
    action = main_menu()#comme elle n'est appele qu'une fois 
    if action == 'play':#et on check seulement ce qu'elle retourne
        main()
