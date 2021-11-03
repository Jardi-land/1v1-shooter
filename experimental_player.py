"""
Creator: @Lorenzo_De_ZEN
"""

import sys, pygame
from settings import *
from pygame import mixer
from support import import_folder
from mixer_sounds import import_sounds

class Player_template(pygame.sprite.Sprite):
    def __init__(self, pos, player_color, player_id):
        super().__init__()
        self.import_character_assets(player_color)
        self.player_id = player_id

        # Animations
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations["idle"][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        # Step Sounds
        self.step_index = 0
        self.step_speed = 0.0525

        # Bullet
        self.bullet_spot = [self.rect.x, self.rect.y]
        self.cooldown_bol = False #comme ca on peut pas shooter direct
        self.cooldown_frame = 0 #Frame per sec = 60 => 1 sec

        # Player Movement
        self.direction = pygame.math.Vector2(0,0)
        self.can_move = False
        self.speed = 10*screen_scale
        self.gravity = 0.8*screen_scale
        self.jump_speed = -15*screen_scale
        self.double_jump = 2

        # Player Status
        self.status = "idle"

        if self.player_id == 1:
            self.facing_right = True
        else:
            self.facing_right = False

        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.stop_index_jump = False
        self.stop_index_crouch = False
        self.stop_index_death = False
        self.want_crouch = False
        self.max_health = 4
        self.health = self.max_health
        self.is_alive = True
        self.input = True

        # Player input
        self.single_w = True

    
    def import_character_assets(self,player_color):
        # Import all char. frames (and sounds)
        character_path = f"game_files/characters/{player_color}/"
        sound_path = "game_files/sounds/"
        self.animations = {"idle":[],"run":[],"jump":[],"crouch":[],"death":[]}
        self.animations_scale = {"idle":[int(140*screen_scale), int(165*screen_scale)],"run":[int(140*screen_scale), int(180*screen_scale)],"jump":[int(140*screen_scale), int(170*screen_scale)],"crouch":[int(140*screen_scale), int(170*screen_scale)],"death":[int(175*screen_scale), int(170*screen_scale)]}
        self.sounds = {"walk":[]}

        for animation in self.animations.keys():
            full_path = character_path + animation

            self.animations[animation] = import_folder(full_path, self.animations_scale[animation][0], self.animations_scale[animation][1])
        
        for sound in self.sounds.keys():
            full_path = sound_path + sound

            self.sounds[sound] = import_sounds(full_path)

    def animate(self):
        # Play the right animation
        self.animation = self.animations[self.status]

        if self.status == "jump":
            if self.stop_index_jump == False:
                self.frame_index += self.animation_speed
                if self.frame_index >= len(self.animation):
                    self.frame_index = 0
                if int(self.frame_index) == len(self.animation) - 1:
                    self.stop_index_jump = True

        elif self.status == "crouch":
            if self.stop_index_crouch == False:
                self.frame_index += self.animation_speed
                if self.frame_index >= len(self.animation):
                    self.frame_index = 0
                if int(self.frame_index) == len(self.animation) - 1:
                    self.stop_index_crouch = True

        elif self.status == "death":
            if self.stop_index_death == False:
                self.frame_index += self.animation_speed
                if self.frame_index >= len(self.animation):
                    self.frame_index = 0
                if int(self.frame_index) == len(self.animation) - 1:
                    self.stop_index_death = True

        else:
            self.stop_index_crouch = False
            self.stop_index_jump = False
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.animation):
                self.frame_index = 0

        self.image = self.animation[int(self.frame_index)]
        if self.facing_right:
            self.image = self.image
        else:
            flipped_image = pygame.transform.flip(self.image,True,False)
            self.image = flipped_image
        
        # Set the rect
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)

    def foot_step(self):
        # Foot step sounds
        self.step = self.sounds["walk"]

        self.last_step = int(self.step_index)

        self.step_index += self.step_speed
        if self.step_index >= len(self.step):
            self.step_index = 0
        

        self.step_sound = self.step[int(self.step_index)]

        if self.last_step != int(self.step_index):
            self.step_sound.play()

    def get_bullet_pos(self):
        # Find the right spot for the bullet
        self.right_idle_spot = [[self.rect.right, self.rect.top + (15 * 5) * screen_scale], [self.rect.right, self.rect.top + (15 * 5) * screen_scale], [self.rect.right, self.rect.top + (15 * 5) * screen_scale], [self.rect.right, self.rect.top + (16 * 5) * screen_scale], [self.rect.right, self.rect.top + (16 * 5) * screen_scale]]
        self.right_run_spot =   [[self.rect.right + self.speed, self.rect.top + (17 * 5) * screen_scale], [self.rect.right + self.speed, self.rect.top + (15 * 5) * screen_scale], [self.rect.right + self.speed, self.rect.top + (18 * 5) * screen_scale], [self.rect.right + self.speed, self.rect.top + (16 * 5) * screen_scale], [self.rect.right + self.speed, self.rect.top + (16 * 5) * screen_scale], [self.rect.right + self.speed, self.rect.top + (18 * 5) * screen_scale]]
        self.right_jump_spot = [[self.rect.right, self.rect.top + (17 * 5) * screen_scale], [self.rect.right, self.rect.top + (16 * 5) * screen_scale]]
        self.right_crouch_spot = [[self.rect.right, self.rect.top + (16 * 5) * screen_scale], [self.rect.right, self.rect.top + (17 * 5) * screen_scale], [self.rect.right, self.rect.top + (20 * 5) * screen_scale]]

        self.left_idle_spot = [[self.rect.left - (3 * 5) * screen_scale, self.rect.top + (15 * 5) * screen_scale], [self.rect.left - (3 * 5) * screen_scale, self.rect.top + (15 * 5) * screen_scale], [self.rect.left - (3 * 5) * screen_scale, self.rect.top + (15 * 5) * screen_scale], [self.rect.left - (3 * 5) * screen_scale, self.rect.top + (16 * 5) * screen_scale], [self.rect.left - (3 * 5) * screen_scale, self.rect.top + (16 * 5) * screen_scale]]
        self.left_run_spot =   [[self.rect.left - (3 * 5) * screen_scale - self.speed, self.rect.top + (17 * 5) * screen_scale], [self.rect.left - (3 * 5) * screen_scale - self.speed, self.rect.top + (15 * 5) * screen_scale], [self.rect.left - (3 * 5) * screen_scale - self.speed, self.rect.top + (18 * 5) * screen_scale], [self.rect.left - (3 * 5) * screen_scale - self.speed, self.rect.top + (16 * 5) * screen_scale], [self.rect.left - (3 * 5) * screen_scale - self.speed, self.rect.top + (16 * 5) * screen_scale], [self.rect.left - (3 * 5) * screen_scale - self.speed, self.rect.top + (18 * 5) * screen_scale]]
        self.left_jump_spot = [[self.rect.left - (3 * 5) * screen_scale, self.rect.top + (17 * 5) * screen_scale], [self.rect.left - (3 * 5) * screen_scale, self.rect.top + (16 * 5) * screen_scale]]
        self.left_crouch_spot = [[self.rect.left - (3 * 5) * screen_scale, self.rect.top + (16 * 5) * screen_scale], [self.rect.left - (3 * 5) * screen_scale, self.rect.top + (17 * 5) * screen_scale], [self.rect.left - (3 * 5) * screen_scale, self.rect.top + (20 * 5) * screen_scale]]
        
        if self.facing_right:
            if self.status == "idle":
                self.bullet_spot = self.right_idle_spot[int(self.frame_index)]
            elif self.status == "run":
                self.bullet_spot = self.right_run_spot[int(self.frame_index)]
            elif self.status == "jump" and self.direction.x != 0:
                self.bullet_spot = [self.right_jump_spot[int(self.frame_index)][0] + self.speed, self.right_jump_spot[int(self.frame_index)][1]]
            elif self.status == "jump":
                self.bullet_spot = self.right_jump_spot[int(self.frame_index)]
            elif self.status == "crouch":
                self.bullet_spot = self.right_crouch_spot[int(self.frame_index)]
        else:
            if self.status == "idle":
                self.bullet_spot = self.left_idle_spot[int(self.frame_index)]
            elif self.status == "run":
                self.bullet_spot = self.left_run_spot[int(self.frame_index)]
            elif self.status == "jump" and self.direction.x != 0:
                self.bullet_spot = [self.left_jump_spot[int(self.frame_index)][0] - self.speed, self.left_jump_spot[int(self.frame_index)][1]]
            elif self.status == "jump":
                self.bullet_spot = self.left_jump_spot[int(self.frame_index)]
            elif self.status == "crouch":
                self.bullet_spot = self.left_crouch_spot[int(self.frame_index)]

    def get_status(self):
        # Define the status for animations
        if not self.is_alive:
            self.status = "death"
            self.input = False
        elif self.direction.y < 0:
            self.status = "jump"
        elif self.direction.y > 1:
            self.status = "jump"
        else:
            if self.direction.x != 0 and self.on_ground:
                self.status = "run"
                self.foot_step()
            elif self.want_crouch:
                self.status = "crouch"
            elif self.on_ground:
                self.status = "idle"

    def shoot(self, shooting_key):
        # Shooting input + cooldown
        keys = pygame.key.get_pressed()
        if keys[shooting_key] and self.cooldown_bol and self.input:
            self.cooldown_frame = 0
            self.cooldown_bol = False
            return True
        else:
            if not self.cooldown_frame == 90:
                self.cooldown_frame += 1
                if self.cooldown_frame == 90:
                    self.cooldown_bol = True
            return False

    def handle_input(self, mov_right_key, mov_left_key, mov_up_key, mov_down_key):
        # Get inputs for movement
        keys = pygame.key.get_pressed()

        if keys[mov_right_key] and keys[mov_left_key] and self.input:
            self.direction.x = 0
        elif keys[mov_right_key] and self.input:
            self.direction.x = 1
            self.facing_right = True
        elif keys[mov_left_key] and self.input:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0

        if keys[mov_up_key] and keys[mov_down_key] and self.input:
            pass
        elif keys[mov_up_key] and self.double_jump > 0 and self.single_w and self.input:
            self.jump()
            self.single_w = False
            self.double_jump = self.double_jump - 2
        elif not keys[mov_up_key] and self.input:
            self.single_w = True
            if keys[mov_down_key] and self.on_ground and self.input:
                self.want_crouch = True
            else:
                self.want_crouch = False

        if self.on_ground:
            self.double_jump = 2

    def is_alive_func(self):
        # Change the player death status
        if self.health <= 0:
            self.is_alive = False

    def apply_gravity(self):
        # G for player
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        # Jump for the player
        self.direction.y = self.jump_speed

    def update(self):
        if self.can_move:
            self.get_input()

        self.get_status()

        if self.cooldown_bol:
            self.can_move = True

        self.animate()
        self.get_bullet_pos()
        self.is_alive_func()

class Player(Player_template):
    def __init__(self,pos, player_color):
        super().__init__(pos, player_color, 1)

    def get_input(self):
        super().handle_input(pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s)

    def shooting(self):
        return super().shoot(pygame.K_e)

class Player_2(Player_template):
    def __init__(self,pos, player_color):
        super().__init__(pos, player_color, 2)

    def get_input(self):
        super().handle_input(pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN)

    def shooting(self):
        return super().shoot(pygame.K_RCTRL)