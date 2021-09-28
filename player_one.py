import sys, pygame

screen_res = [1920, 1080]
screen_scale = [1920/screen_res[0], 1080/screen_res[1]]

screen = pygame.display.set_mode((screen_res[0], screen_res[1]))

player_one_surf = pygame.image.load("game_files/characters/green/idle/Gunner_Idle1.png").convert_alpha()
player_one_surf = pygame.transform.scale(player_one_surf, (240, 240))