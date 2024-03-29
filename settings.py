screen_res_array = {"hd":[1920, 1080],"2":[1536, 864],"3":[1152, 648],"4":[768, 432],"5":[384, 216]}
screen_res = screen_res_array["2"]
screen_scale = screen_res[0]/1920
mouse_visible = False

window_name = "Gunner 1vs1"

DEFAULT_FPS = 60
TESTING = False

gravity = {'normal' : 0.8, 'low' : 0.2}

# " " = nothing
# "X" = Platform
# "| " = Platform_Thin left
# " |" = Platform_Thin right
#"PW" = PowerUp
firstmap = [["X",  "X",  "X",  "X",  "X",  "X",  "X",  "X",  "X",  "X",  "X",  "X"],#len = 12
            ["X",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  "X"],
            ["| ", " ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " |"],
            ["| ", " ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " |"],
            ["| ", " ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " |"],
            ["| ", " ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " |"],
            ["| ", "PW",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  "PW",  " |"],
            ["| ", " ", " |", " ",  " ",  " ",  " ",  " ",  " ",  "| ", " ", " |"],
            ["X",  "X",  "X",  " ",  " ",  "PW",  "PW",  " ",  " ",  "X",  "X",  "X"],
            ["| ", " ",  " ",  " ",  " ",  " ", " ", " ",  " ",  " ",  " ",  " |"],
            ["| ", " ",  " ",  " ",  " ",  " |", "| ", " ",  " ",  " ",  " ",  " |"],
            ["| ", " ",  "PW",  "PW",  "PW",  " ",  " ",  "PW",  "PW",  "PW",  " ",  " |"],
            ["| ", " ",  " ", " ", " ", " ",  " ",  " ", " ", " ", " ",  " |"],
            ["| ", " ",  " |", "X",  "| ", " ",  " ",  " |", "X",  "| ", " ",  " |"],
            ["| ", " ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " ",  " |"],
            ["| ", " ",  " ",  " ",  " ",  "PW",  "PW",  " ",  " ",  " ",  " ",  " |"],
            ["| ", "P",  " ",  " ",  " ",  " ", " ", " ",  " ",  " ",  "P2", " |"],
            ["X",  "X",  "X",  "X",  "X",  "X",  "X",  "X",  "X",  "X",  "X",  "X"],]
            #len = 18