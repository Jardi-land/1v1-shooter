"""
Creator: @Lorenzo_De_ZEN
"""

import sys, pygame
from settings import *
from tiles import Tiles
from player import Player

class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.current_x = 0

    def setup_level(self,layout):
        self.Tiles = pygame.sprite.Group()
        self.Player = pygame.sprite.GroupSingle()

        for i in range(18):
                if i == 0:
                    platform_y = 925
                else:
                    platform_y = platform_y-60
                line_i = 17-i
                for i in range(12):
                    if i == 0:
                        platform_x = 1755
                    else:
                        platform_x = platform_x-160
                    if layout[line_i][11-i] == "X":
                        Tile = Tiles((platform_x,platform_y),1)
                        self.Tiles.add(Tile)
                    elif layout[line_i][11-i] == " |":
                        platform_x = platform_x+80
                        Tile = Tiles((platform_x,platform_y),0)
                        self.Tiles.add(Tile)
                        platform_x = platform_x-80
                    elif layout[line_i][11-i] == "| ":
                        Tile = Tiles((platform_x,platform_y),0)
                        self.Tiles.add(Tile)
                    elif layout[line_i][11-i] == "P":
                        player_sprite = Player((platform_x,platform_y))
                        self.Player.add(player_sprite)

    def horizontal_movement_collision(self):
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

    def vertical_movement_collision(self):
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
   
    def draw(self):
        #Tiles
        self.Tiles.update(self.world_shift)
        self.Tiles.draw(self.display_surface)

        #Player
        self.Player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.Player.draw(self.display_surface)