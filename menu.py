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


def main_menu() -> str:
    screen = pygame.display.set_mode(screen_res)
    pygame.display.set_caption("Main menu")
    pygame.mouse.set_visible(True)

    info_text = txt(screen.get_width()/2, screen.get_height()/2, text="Appuie sur n'importe qu'elle touche")
    important_info = txt(screen.get_width()/2, screen.get_height()/2 + 50, text="")

    while True:
        screen.fill((0,0,0))
        info_text.draw(screen)
        important_info.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.KEYDOWN:
                return 'play'
        
        pygame.display.update()