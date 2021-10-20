screen_res_array = {"hd":[1920, 1080],"2":[1536, 864],"3":[1152, 648],"4":[768, 432],"5":[384, 216]}
screen_res = screen_res_array["hd"]
screen_scale = screen_res[0]/1920
window_name = "1v1 Shooter"
mouse_visible = False

# " " = nothing
# "X" = Platform
# "| " = Platform_Thin left
# " |" = Platform_Thin right
#"PW" = PowerUp
firstmap = [["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X"],
            ["| ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " |"],
            ["| ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " |"],
            ["| ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " |"],
            ["| ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " |"],
            ["| ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " |"],
            ["| ", "PW", " |", " ", " ", " ", " ", " ", " ", "| ", "PW", " |"],
            ["X", "X", "X", " ", " ", " ", " ", " ", " ", "X", "X", "X"],
            ["| ", " ", " ", " ", " ", "PW", "PW", " ", " ", " ", " ", " |"],
            ["| ", " ", " ", " ", " ", " |", "| ", " ", " ", " ", " ", " |"],
            ["| ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " |"],
            ["| ", " ", "PW", "PW", "PW", " ", " ", "PW", "PW", "PW", " ", " |"],
            ["| ", " ", " |", "X", "| ", " ", " ", " |", "X", "| ", " ", " |"],
            ["| ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " |"],
            ["| ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " |"],
            ["| ", "P", " ", " ", " ", "PW", "PW", " ", " ", " ", "P2", " |"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],]