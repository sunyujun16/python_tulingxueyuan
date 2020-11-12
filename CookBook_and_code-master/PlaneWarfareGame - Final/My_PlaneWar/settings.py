import os
import random

game_stats = 'run'

screen_width = 600
screen_height = 800

# Hero's attribute
hero_img_num = 0
hero_original_pos = [280, 780]
hero_step = 4
hero_lives = 3
hero_score = 0
hero_width = 97
hero_height = 124

# path and names of images
img_path = os.getcwd() + os.path.join('/Images/')
suffix = '.gif'
filename_sky = "sky"
filename_pause = "pause"
filename_start = "start"
filename_start_label = "start_label"
filename_gameover = "gameover"
filename_enemy = "smallplane"
filename_bee = "bee"
filename_bullet = "bullet"


def get_filename_hero():

    if 0 <= hero_img_num < 8:
        filename_hero = "hero0"
    elif 8 <= hero_img_num < 16:
        filename_hero = "hero1"
    elif 16 <= hero_img_num < 24:
        filename_hero = "hero2"
    elif 24 <= hero_img_num < 32:
        filename_hero = "hero3"
    elif 32 <= hero_img_num < 40:
        filename_hero = "hero4"

    return filename_hero


# Bees's attribute
bee_width = 60
bee_height = 50
bee_step = 0.9 * 2
bee_num = 3

# Enemies's attribute
enemy_width = 49
enemy_height = 36
enemy_step = 1.1 * 2
enemy_num = 3

# Bees's attribute
bullet_width = 8
bullet_height = 14
bullet_step = 5
bullet_num = 15

# Backup
pause_width = 400
pause_height = 654
start_width = 400
start_height = 654
gameover_width = 400
gameover_height = 654
smallplane_width = 49
smallplane_height = 36
bigplane_width = 69
bigplane_height = 99
