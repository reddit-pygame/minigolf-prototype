"""
This module initializes the display and creates dictionaries of resources.
"""

import os
import pygame as pg

from . import tools


SCREEN_SIZE = (1280, 720)
ORIGINAL_CAPTION = "Mini Golf"

#Initialization

pg.mixer.pre_init(44100, -16, 1, 512)

pg.init()
os.environ['SDL_VIDEO_CENTERED'] = "TRUE"
pg.display.set_caption(ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode(SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()


#Resource loading (Fonts and music just contain path names).
FONTS = tools.load_all_fonts(os.path.join("resources", "fonts"), accept=(".ttf", ".otf"))
MUSIC = tools.load_all_music(os.path.join("resources", "music"))
SFX   = tools.load_all_sfx(os.path.join("resources", "sound"))
GFX   = tools.load_all_gfx(os.path.join("resources", "graphics"))

pg.mixer.music.load(MUSIC["clay"])
pg.mixer.music.play(-1)

#copy the front nine for the back nine
for x in range(1, 10):
    GFX["hole{}".format(x + 9)] = GFX["hole{}".format(x)]
    GFX["green{}".format(x + 9)] = GFX["green{}".format(x)]
