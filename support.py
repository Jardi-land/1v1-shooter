import os.path
import pygame

def import_folder(path, x, y, name):
    surface_list = []
    surface_numb = 1

    while True:
        if os.path.exists(f"{path}/{name}{surface_numb}.png"):
            surface_list.append(pygame.transform.scale(pygame.image.load(f"{path}/{name}{surface_numb}.png").convert_alpha(), (int(x), int(y))))
            surface_numb += 1
        else: break

    if surface_numb == 1:
        print("path doesn't exist")

    return surface_list