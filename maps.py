import sys, pygame

screen_res = [1920, 1080]
screen_scale = [1920/screen_res[0], 1080/screen_res[1]]

# " " = nothing
# "X" = Platform
# "| " = Platform_Thin left
# " |" = Platform_Thin right
firstmap = [["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["X", " |", " ", "| ", "| ", " ", " ", " ", " ", " ", " ", " "],
            ["X", " |", " ", "| ", "| ", "X", " ", " ", " ", " ", " ", " "],
            ["X", " |", " ", "| ", "| ", "X", " ", " ", " ", " ", " ", " "],
            ["X", "X", "X", " ", "X", "X", "X", "X", "X", "X", "X", "X"],]

screen = pygame.display.set_mode((screen_res[0], screen_res[1]))

def update_map(platform_y, platform_x, platform, platform_thin):
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
            if firstmap[line_i][11-i] == "X":
                screen.blit(platform,(platform_x,platform_y))
            elif firstmap[line_i][11-i] == " |":
                platform_x = platform_x+80
                screen.blit(platform_thin,(platform_x,platform_y))
                platform_x = platform_x-80
            elif firstmap[line_i][11-i] == "| ":
                screen.blit(platform_thin,(platform_x,platform_y))