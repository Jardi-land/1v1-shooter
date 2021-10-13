import os
import sys, pygame
from settings import *


def main_menu():
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Main menu")
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)

    while True:
        screen.fill((0,0,0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return False