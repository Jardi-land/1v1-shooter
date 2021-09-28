import sys, pygame
from maps import *

pygame.init()

screen_res = [1920, 1080]
screen_scale = [1920/screen_res[0], 1080/screen_res[1]]
window_name = "1v1 Shooter"

screen = pygame.display.set_mode((screen_res[0], screen_res[1]))
pygame.display.set_caption(window_name)
clock = pygame.time.Clock()

bg_surface = pygame.Surface((1920,1080))
bg_surface.fill((118, 120, 134, 255))

platform = pygame.image.load("platforms/Platform.png")
platform = pygame.transform.scale(platform, (165, 155))
platform_thin = pygame.image.load("platforms/Platform_Thin.png")
platform_thin = pygame.transform.scale(platform_thin, (85, 155))

platform_x = 1755
platform_y = 925

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(bg_surface,(0,0))
    update_map(platform_y, platform_x, platform, platform_thin)

    pygame.display.update()
    clock.tick(60)