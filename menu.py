import os
import sys, pygame
from settings import *
from config import cfg


class button:
    def __init__(self, x, y, transx, transy, image_path, alternate_img=None) -> None: 
        # NO *SCREEN_SCALE WHEN YOU  !! CALL !! BUTTON exemple: button(0, 0, 10, 20, "/d.png")
        # Donc si tu veux utiliser button() pour transx et transy tu met les valeur par defaut pour 1920x1080
        self.image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(), (int(transx*screen_scale), int(transy*screen_scale)))

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

    play_button = button(screen_res[0]/2, screen_res[1]/2, 601, 177, PLAY_BUTTON_PATH, PLAY_BUTTON_2ND_PATH)

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

def choose_char_menu():
    colors = []
    screen = pygame.display.set_mode(screen_res)
    pygame.display.set_caption("Choose your character")
    pygame.mouse.set_visible(True)

    double_check = True

    all_button = {"black":[], "green":[], "red":[], "blue":[], "yellow":[]}
    
    for value in all_button.keys():
        all_button[value] = [f"game_files/buttons/char_button/{value}/{value}_button1.png", f"game_files/buttons/char_button/{value}/{value}_button2.png"]

    BG_SURF = pygame.transform.scale(pygame.image.load("game_files/background/main_menu.png").convert_alpha(), (int(1920*screen_scale), int(1080*screen_scale)))

    CHOOSE_YOUR = pygame.transform.scale(pygame.image.load("game_files/font/font_img/choose_your.png").convert_alpha(), (int(862*screen_scale), int(88.5*screen_scale)))

    COLOR = pygame.transform.scale(pygame.image.load("game_files/font/font_img/color.png").convert_alpha(), (int(396.5*screen_scale), int(88.5*screen_scale)))

    LOCKER = pygame.transform.scale(pygame.image.load("game_files/buttons/char_button/lock/lock_button.png").convert_alpha(), (int(110*screen_scale), int(100*screen_scale)))

    yellow_button = button(1245*screen_scale, screen_res[1]/1.75, 110, 100, all_button["yellow"][0], all_button["yellow"][1])
    blue_button = button(1100*screen_scale, screen_res[1]/1.75, 110, 100, all_button["blue"][0], all_button["blue"][1])
    red_button = button(955*screen_scale, screen_res[1]/1.75, 110, 100, all_button["red"][0], all_button["red"][1])
    black_button = button(810*screen_scale, screen_res[1]/1.75, 110, 100, all_button["black"][0], all_button["black"][1])
    green_button = button(660*screen_scale, screen_res[1]/1.75, 110, 100, all_button["green"][0], all_button["green"][1])

    while True:
        if double_check:
            if not pygame.mouse.get_pressed()[0]:
                double_check = False

        mouse = pygame.mouse.get_pos()

        screen.blit(BG_SURF,(0,0))

        screen.blit(CHOOSE_YOUR,(screen_res[0]/2 - CHOOSE_YOUR.get_width()/2, screen_res[1]/2 - CHOOSE_YOUR.get_height()*2.4))

        screen.blit(COLOR,(screen_res[0]/2 - COLOR.get_width()/2, screen_res[1]/2 - COLOR.get_height()*1.2))

        yellow_button.draw(screen)
        blue_button.draw(screen)
        red_button.draw(screen)
        black_button.draw(screen)
        green_button.draw(screen)

        if not double_check:
            if "yellow" in colors:
                screen.blit(LOCKER,(1245*screen_scale- LOCKER.get_width()/2, screen_res[1]/1.75 - LOCKER.get_height()/2))
            else:
                if yellow_button.switch_image(mouse):
                    if pygame.mouse.get_pressed()[0]:
                        colors.append('yellow')

            if "blue" in colors:
                screen.blit(LOCKER,(1100*screen_scale- LOCKER.get_width()/2, screen_res[1]/1.75 - LOCKER.get_height()/2))
            else:
                if blue_button.switch_image(mouse):
                    if pygame.mouse.get_pressed()[0]:
                        colors.append('blue')
            
            if "red" in colors:
                screen.blit(LOCKER,(955*screen_scale- LOCKER.get_width()/2, screen_res[1]/1.75 - LOCKER.get_height()/2))
            else:
                if red_button.switch_image(mouse):
                    if pygame.mouse.get_pressed()[0]:
                        colors.append('red')

            if "black" in colors:
                screen.blit(LOCKER,(810*screen_scale- LOCKER.get_width()/2, screen_res[1]/1.75 - LOCKER.get_height()/2))
            else:
                if black_button.switch_image(mouse):
                    if pygame.mouse.get_pressed()[0]:
                        colors.append('black')

            if "green" in colors:
                screen.blit(LOCKER,(660*screen_scale- LOCKER.get_width()/2, screen_res[1]/1.75 - LOCKER.get_height()/2))
            else:
                if green_button.switch_image(mouse):
                    if pygame.mouse.get_pressed()[0]:
                        colors.append('green')
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
        pygame.display.update()

        if len(colors) >= 2:
            return colors

def end_screen(pid : int, winner_color : str):
    from main import main
    from ui import mugshot

    screen = pygame.display.set_mode(screen_res)
    WIDTH, HEIGHT = screen.get_width(), screen.get_height()
    pygame.mouse.set_visible(True)
    clock = pygame.time.Clock()

    BG = pygame.transform.scale(pygame.image.load('game_files/background/main_menu.png'), screen_res)
    winner_pl = mugshot(pid, winner_color)
    CADRE = pygame.transform.scale(pygame.image.load('game_files/ui/cadre.png'), (winner_pl.image.get_width(), winner_pl.image.get_height()))
    blit_pos = screen_res[0]/2 - winner_pl.image.get_width()/2, screen_res[1]/2 - winner_pl.image.get_height()/2

    winner_txt = pygame.transform.scale(pygame.image.load("game_files/font/font_img/the_winner_is.png"), (int(960*screen_scale), int(85.5*screen_scale))).convert_alpha()
    winner_txt_pos = (screen.get_width()/2 - winner_txt.get_width()/2, screen.get_height()/4 - winner_txt.get_height()/2)
    skip_button = button(WIDTH/2, (HEIGHT/5)*3.5, 314, 88.5, "game_files/buttons/skip1.png", "game_files/buttons/skip2.png")
    counter = 0

    while True:
        clock.tick(DEFAULT_FPS)
        screen.fill((118, 120, 134))
        screen.blit(BG, (0,0))
        mouse = pygame.mouse.get_pos()

        if counter >= cfg.end_screen_cd * DEFAULT_FPS:
            skip_button.draw(screen)
            if skip_button.switch_image(mouse):
                if pygame.mouse.get_pressed()[0]:
                    main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main()

        screen.blit(CADRE, blit_pos)
        screen.blit(winner_pl.image, blit_pos)
        screen.blit(winner_txt, winner_txt_pos)

        counter += 1
        pygame.display.update()