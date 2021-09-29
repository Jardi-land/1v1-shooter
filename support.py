from os import walk
import pygame

def import_folder(path):
    surface_list = []

    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + "/" + image
            image_surf = pygame.transform.scale(pygame.image.load(full_path).convert_alpha(), (240, 240))
            surface_list.append(image_surf)
    
    return surface_list