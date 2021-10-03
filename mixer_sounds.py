from os import walk
import pygame
from pygame import mixer

def import_sounds(path):
    foot_step_list = []

    for _,__,wav_files in walk(path):
        for sounds in wav_files:
            full_path = path + "/" + sounds
            foot_step = mixer.Sound(full_path)
            foot_step_list.append(foot_step)
    
    return foot_step_list