"""
Creator: @Lorenzo_De_ZEN
"""

import sys, pygame
from settings import *
from tiles import Tiles
from player import Player, Player_2
from bullet import Bullet, Muzzle_flash
from ui import ui, cooldown_ui, mugshot
from power import PowerUp

class Level:
    def __init__(self,level_data,surface):
        # The Map
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.current_x = 0

        # Shooting
        self.Bullet_p1 = pygame.sprite.Group()
        self.Bullet_p2 = pygame.sprite.Group()
        self.Muzzle_p1 = pygame.sprite.GroupSingle()
        self.Muzzle_p2 = pygame.sprite.GroupSingle()

        # Ui
        self.ui_p1 = pygame.sprite.Group()
        self.ui_p2 = pygame.sprite.Group()

        self.ui_cooldown_p1 = pygame.sprite.Group()
        self.ui_cooldown_p2 = pygame.sprite.Group()

        self.mugshot_p1 = pygame.sprite.Group()
        self.mugshot_p2 = pygame.sprite.Group()

        self.ui_p1.add(ui(1))
        self.ui_p2.add(ui(2))

        self.ui_cooldown_p1.add(cooldown_ui(1))
        self.ui_cooldown_p2.add(cooldown_ui(2))

        self.mugshot_p1.add(mugshot(1, "green"))
        self.mugshot_p2.add(mugshot(2, "red"))

        #power up test
        self.pwup = PowerUp()
        

    def setup_level(self,layout):
        # Sprite(s) groups
        self.Tiles = pygame.sprite.Group()
        self.Player = pygame.sprite.GroupSingle()
        self.Player_2 = pygame.sprite.GroupSingle()

        # Map Core
        for i in range(18):
            if i == 0:
                platform_y = screen_res[1] - (155*screen_scale)
            else:
                platform_y -= (60*screen_scale)
            line_i = 17-i
            for i in range(12):
                if i == 0:
                    platform_x = screen_res[0] - (165*screen_scale)
                else:
                    platform_x -= (160*screen_scale)
                if layout[line_i][11-i] == "X":
                    Tile = Tiles((platform_x,platform_y),1)
                    self.Tiles.add(Tile)
                elif layout[line_i][11-i] == " |":
                    platform_x += (80*screen_scale)
                    Tile = Tiles((platform_x,platform_y),0)
                    self.Tiles.add(Tile)
                    platform_x -= (80*screen_scale)
                elif layout[line_i][11-i] == "| ":
                    Tile = Tiles((platform_x,platform_y),0)
                    self.Tiles.add(Tile)
                elif layout[line_i][11-i] == "P":
                    player_sprite = Player((platform_x,platform_y))
                    self.Player.add(player_sprite)
                elif layout[line_i][11-i] == "P2":
                    player_2_sprite = Player_2((platform_x,platform_y))
                    self.Player_2.add(player_2_sprite)

    def horizontal_movement_collision(self):
        # Player 1
        Player = self.Player.sprite
        Player.rect.x += Player.direction.x * Player.speed

        for sprite in self.Tiles.sprites():
            if sprite.colliderect.colliderect(Player.rect):
                if Player.direction.x < 0:
                    Player.rect.left = sprite.colliderect.right
                    Player.on_left = True
                    self.current_x = Player.rect.left
                elif Player.direction.x > 0:
                    Player.rect.right = sprite.colliderect.left
                    Player.on_right = True
                    self.current_x = Player.rect.right
        
        if Player.on_left and (Player.rect.left < self.current_x or Player.direction.x >= 0):
            Player.on_left = False

        if Player.on_right and (Player.rect.right > self.current_x or Player.direction.x <= 0):
            Player.on_right = False

        # Player 2
        Player_2 = self.Player_2.sprite
        Player_2.rect.x += Player_2.direction.x * Player_2.speed

        for sprite in self.Tiles.sprites():
            if sprite.colliderect.colliderect(Player_2.rect):
                if Player_2.direction.x < 0:
                    Player_2.rect.left = sprite.colliderect.right
                    Player_2.on_left = True
                    self.current_x = Player_2.rect.left
                elif Player_2.direction.x > 0:
                    Player_2.rect.right = sprite.colliderect.left
                    Player_2.on_right = True
                    self.current_x = Player_2.rect.right
        
        if Player_2.on_left and (Player_2.rect.left < self.current_x or Player_2.direction.x >= 0):
            Player_2.on_left = False

        if Player_2.on_right and (Player_2.rect.right > self.current_x or Player_2.direction.x <= 0):
            Player_2.on_right = False

    def vertical_movement_collision(self):
        # Player 1
        Player = self.Player.sprite
        Player.apply_gravity()

        for sprite in self.Tiles.sprites():
            if sprite.colliderect.colliderect(Player.rect):
                if Player.direction.y > 0:
                    Player.rect.bottom = sprite.colliderect.top
                    Player.direction.y = 0
                    Player.on_ground = True
                elif Player.direction.y < 0:
                    Player.rect.top = sprite.colliderect.bottom
                    Player.direction.y = 0
                    Player.on_ceiling = True
        
        if Player.on_ground and Player.direction.y < 0 or Player.direction.y > 1:
            Player.on_ground = False
        if Player.on_ceiling and Player.direction.y > 0:
            Player.on_ceiling = False

        # Player 2
        Player_2 = self.Player_2.sprite
        Player_2.apply_gravity()

        for sprite in self.Tiles.sprites():
            if sprite.colliderect.colliderect(Player_2.rect):
                if Player_2.direction.y > 0:
                    Player_2.rect.bottom = sprite.colliderect.top
                    Player_2.direction.y = 0
                    Player_2.on_ground = True
                elif Player_2.direction.y < 0:
                    Player_2.rect.top = sprite.colliderect.bottom
                    Player_2.direction.y = 0
                    Player_2.on_ceiling = True
        
        if Player_2.on_ground and Player_2.direction.y < 0 or Player_2.direction.y > 1:
            Player_2.on_ground = False
        if Player_2.on_ceiling and Player_2.direction.y > 0:
            Player_2.on_ceiling = False

    def bullet_display(self):
        Player = self.Player.sprite
        Player_2 = self.Player_2.sprite

        self.Bullet_p1.update()
        self.Bullet_p2.update()

        self.Muzzle_p1.update()
        self.Muzzle_p2.update()
        
        if Player.shooting():
            self.Bullet_p1.add(Bullet((Player.bullet_spot[0], Player.bullet_spot[1]), Player.facing_right))
            self.Muzzle_p1.add(Muzzle_flash((Player.bullet_spot[0], Player.bullet_spot[1]), Player.facing_right))


        if Player_2.shooting():
            self.Bullet_p2.add(Bullet((Player_2.bullet_spot[0], Player_2.bullet_spot[1]), Player_2.facing_right))
            self.Muzzle_p2.add(Muzzle_flash((Player_2.bullet_spot[0], Player_2.bullet_spot[1]), Player_2.facing_right))

    def bullet_collide(self):
        Player = self.Player.sprite
        Player_2 = self.Player_2.sprite

        # Bullet Player 1
        for sprite in self.Tiles.sprites():
            for bullet in self.Bullet_p1.sprites():
                if sprite.colliderect.colliderect(bullet.rect):
                    bullet.kill()
                elif bullet.rect.colliderect(Player_2.rect):
                    bullet.kill()
                    Player_2.health -= bullet.damage
                    self.ui_p2.update(2, Player_2.health)

        # Bullet Player 2
        for sprite in self.Tiles.sprites():
            for bullet in self.Bullet_p2.sprites():
                if sprite.colliderect.colliderect(bullet.rect):
                    bullet.kill()
                elif bullet.rect.colliderect(Player.rect):
                    bullet.kill()
                    Player.health -= bullet.damage
                    self.ui_p1.update(1, Player.health)

    def ui_cooldown(self):
        Player = self.Player.sprite
        Player_2 = self.Player_2.sprite
        
        self.ui_cooldown_p1.update(1, int(Player.cooldown_frame * 0.066))
        self.ui_cooldown_p2.update(2, int(Player_2.cooldown_frame * 0.066))

        self.ui_cooldown_p1.draw(self.display_surface)
        self.ui_cooldown_p2.draw(self.display_surface)

    def ui(self):
        self.ui_p1.draw(self.display_surface)
        self.ui_p2.draw(self.display_surface)

    def mugshot(self):
        self.mugshot_p1.draw(self.display_surface)
        self.mugshot_p2.draw(self.display_surface)

    def power_up_update(self):
        Player = self.Player.sprite
        Player_2 = self.Player_2.sprite
        self.pwup.draw(self.display_surface)
        
        if Player.rect.colliderect(self.pwup.rect):
            self.pwup.pick_new_spot()
            Player.health = Player.max_health
            self.ui_p1.update(1, Player.health)

        elif Player_2.rect.colliderect(self.pwup.rect):
            self.pwup.pick_new_spot()
            Player_2.health = Player_2.max_health
            self.ui_p2.update(2, Player_2.health)


    def draw(self):
        # Tiles
        self.Tiles.update(self.world_shift)
        self.Tiles.draw(self.display_surface)

        # Player (1/2)
        self.Player.update()
        self.Player_2.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()

        # Bullet
        self.bullet_display()
        self.bullet_collide()
        self.Bullet_p1.draw(self.display_surface)
        self.Bullet_p2.draw(self.display_surface)
        self.Muzzle_p1.draw(self.display_surface)
        self.Muzzle_p2.draw(self.display_surface)

        # Player (2/2)
        self.Player.draw(self.display_surface)
        self.Player_2.draw(self.display_surface)

        # Ui
        self.ui()
        self.ui_cooldown()
        self.mugshot()
        
        #pw
        self.power_up_update()