class tiles(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image.normal = pygame.transform.scale(pygame.image.load("game_files/platforms/Platform.png").convert_alpha(), (165, 155))
        self.image.thin = pygame.transform.scale(pygame.image.load("game_files/platforms/Platform_Thin.png").convert_alpha(), (85, 155))
        self.rect = self.image.get_rect(topleft = pos)