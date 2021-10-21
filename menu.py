import os
import sys, pygame
from settings import *
"""temp"""
class txt:
    def __init__(self, x, y, color=(255,255,255), text='', pos_mode=0, font_size=30) -> None:
        """
        Simple text class. pos_mode = 0 draw text from the center and 1 from the top left.
        the class is made so that the x & y values of the topleft corner never go below 0.
        (je l'ai faite ^^)
        """
        newy = 0
        if y < font_size * .5 and pos_mode == 0:
            newy = y + int(font_size * .5)
        else:
            newy = y

        self.pos = pygame.math.Vector2(x, newy)
        self.color = color
        self.pos_mode = pos_mode
        self.font = pygame.font.SysFont('comicsans', font_size)
        self.text = text
    
    def draw(self, win):
        txt_ = self.font.render(str(self.text), 1, self.color)

        if self.pos.x < txt_.get_width() * .5 and self.pos_mode == 0:
            self.pos.x = int(txt_.get_width() * .5)

        if self.pos_mode == 0:
            win.blit(txt_, (self.pos.x - txt_.get_width()/2, self.pos.y - txt_.get_height()/2))
        else:
            win.blit(txt_, self.pos)

""""""

class button:
    def __init__(self, x, y, image_path, alternate_img=None) -> None:
        self.image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(), (int(601*screen_scale), int(177*screen_scale)))

        self.size = pygame.math.Vector2(self.image.get_width(), self.image.get_height())
        self.pos = pygame.math.Vector2(x - self.size.x *.5, y - self.size.y *.5)

        self.alternate_image = pygame.transform.scale(pygame.image.load(alternate_img).convert_alpha(), (int(self.size[0]), int(self.size[1]))) if alternate_img != None else None
        self.default_image = self.image

    def draw(self, win):
        win.blit(self.image, self.pos)

    def is_Over(self, pos):
        if self.pos.x < pos[0] and self.pos.x + self.size.x > pos[0]:
            if self.pos.y < pos[1] and self.pos.y + self.size.y > pos[1]:
                return True
        return False

    def switch_image(self, pos):
        if self.is_Over(pos):
            if self.alternate_image != None:
                self.image = self.alternate_image
            return True
        else:
            self.image = self.default_image
            return False

def main_menu() -> str:
    screen = pygame.display.set_mode(screen_res)
    pygame.display.set_caption("Main menu")
    pygame.mouse.set_visible(True)

    PLAY_BUTTON_PATH = 'game_files/buttons/play1.png'
    PLAY_BUTTON_2ND_PATH = 'game_files/buttons/play2.png'

    BG_SURF = pygame.transform.scale(pygame.image.load("game_files/background/main_menu.png").convert_alpha(), (int(1920*screen_scale), int(1080*screen_scale)))

    play_button = button(screen_res[0]/2, screen_res[1]/2, PLAY_BUTTON_PATH, PLAY_BUTTON_2ND_PATH)

    while True:
        mouse = pygame.mouse.get_pos()
        
        screen.blit(BG_SURF,(0,0))

        play_button.draw(screen)

        if play_button.switch_image(mouse):
            if pygame.mouse.get_pressed()[0]:
                return 'play'

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
        
        pygame.display.update()
