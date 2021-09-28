import sys, pygame

pygame.init()

screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Shooter")
clock = pygame.time.Clock()

bg_surface = pygame.Surface((1920,1080))
bg_surface.fill((118, 120, 134, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface,(0,0))

    pygame.display.update()
    clock.tick(60)