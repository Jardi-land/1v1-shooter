"""
Creator: @Lorenzo_De_ZEN
"""

import sys, pygame
from level import *
from player import *
from settings import *
from tiles import Tiles
from menu import main_menu, choose_char_menu, end_screen

pygame.init()
def Game(player_1, player_2):

    screen = pygame.display.set_mode((screen_res[0], screen_res[1]))
    pygame.display.set_caption(window_name)
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(mouse_visible)
    py_con = pygame.image.load("game_files/characters/red/mug_shot/Gunner_mugshot.png").convert_alpha()
    pygame.display.set_icon(py_con)

    bg_surf = pygame.Surface((screen_res[0], screen_res[1]))
    bg_surf.fill((118, 120, 134, 255))


    level = Level(firstmap, screen, player_1, player_2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.blit(bg_surf,(0,0))
        won, winner_color, pid = level.draw()
        if won:
            end_screen(pid, winner_color)

        pygame.display.update()
        clock.tick(DEFAULT_FPS)


def main():
    action = main_menu()
    if action == 'play':
        player_1, player_2 = choose_char_menu()
        Game(player_1, player_2)

if __name__ == '__main__':
    main()