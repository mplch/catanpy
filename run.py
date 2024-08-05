#!/usr/bin/env python3
#202408032257-Polesovice

#----- NOTES ------------------------------------------------------

"""
* pygame transparent screen when run from explorer
* EDIT: Skaluji canvas --> RESI pozdejsi pokladani budov
* je potreba spravne zadefinovat transformacni souradnicove funkce
* mozna bych si usnadnil zivot CENTRICKOU geometrii - hexy, fonty...
"""

#----- IMPORTS ------------------------------------------------------

import pygame
from sys import exit as sys_exit
import random  # from

#----- CONSTANTS ------------------------------------------------------

"""
SCA = 5
d = 160
s = 5  # scale: 5*32=160
# shouldn't be needed actually
"""

hx = "textures/hexes/Template_horiz.png"

hexes = "textures/hexes/"
hextypes = "Claypit.png  Dessert.png  Field.png  Forest.png  \
Mountains.png  Pasture.png  Sea.png  Template_vert".split('  ')
# odeber png (a zpet pridej) --> hexes + type + ".png"
hexlands = "Claypit.png  Field.png  Forest.png  \
Mountains.png  Pasture.png".split('  ')
for t in hexlands: print(">",t,"<")

COORD_TILES_FONT_SIZE = 18
COORD_TILES_FONT_COLOR = (200, 50, 50)
COORD_TILES_FONT_COLOR = (0, 0, 0)
COORD_TILE_X_OFFSET = 9
COORD_TILE_Y_OFFSET = 20

#----- FUNCTIONS ------------------------------------------------------

def putTile(type, coords):
    file = hexes + type
    img = pygame.image.load(file).convert_alpha()
    # load all images just once, then just copy them (directly place)
    #    img = pygame.transform.scale_by(img, (SCA, SCA)) # haha
    img = pygame.transform.rotate(img, 90)
    surf_board.blit(img, coords)

def coordPrintTile(c, r, x, y):
    text_surface = my_font.render(f"({c}, {r})", False, COORD_TILES_FONT_COLOR)
    surf_board.blit(text_surface, (x+COORD_TILE_X_OFFSET, y+COORD_TILE_Y_OFFSET))


def placeHex(type, c, r):
    # uz si nepamatuji, co melo byt con,
    # connect urcite ne, conformation...nevim
    x_off, y_off = 200, 5
    hor_con, ver_con = 10, 6
    doShiftFirstColumnDown = 1  # bool 0 or 1
    if c % 2 == doShiftFirstColumnDown:
        x = x_off + c * (tileSize - hor_con)
        y = y_off + r * (tileSize - ver_con)
        putTile(type, (x, y))
        coordPrintTile(c, r, x, y)
    else:
        x = x_off + c * (tileSize - hor_con)
        y = y_off + r * (tileSize - ver_con) + tileSize // 2 - 3  # magic number 3 ?!
        putTile(type, (x, y))
        coordPrintTile(c, r, x, y)

def draw_map_rectangle(w, h):
    for c in range(w):
        for r in range(h):
            type = random.choice(hexlands)
            placeHex(type, c, r)
    for f in range(7):
        placeHex("Sea.png", 0, f)
        placeHex("Sea.png", 6, f)
        placeHex("Sea.png", f, 0)
        placeHex("Sea.png", f, 6)

    """
    * takto je to mozna nejprehlednejsi. --> Funguje to? funguje!
    """

def draw_map_def_hex_v1():
    draw_map_rectangle(7, 7)
    outer = "Template_vert.png"
    outer = "Sea.png"
    for f in range(7):
        placeHex(outer, 0, f)
        placeHex(outer, 6, f)
        placeHex(outer, f, 0)
        placeHex(outer, f, 6)
    placeHex(outer, 1, 1)
    placeHex(outer, 5, 1)
    placeHex(outer, 1, 5)
    placeHex(outer, 2, 5)
    placeHex(outer, 4, 5)
    placeHex(outer, 5, 5)

def draw_map_def_hex_outer():
    # draw_map_rectangle(7, 7)
    outer = "Template_vert.png"
    outer = "Sea.png"
    for f in range(7):
        placeHex(outer, 0, f)
        placeHex(outer, 6, f)
        placeHex(outer, f, 0)
        placeHex(outer, f, 6)
    placeHex(outer, 1, 1)
    placeHex(outer, 5, 1)
    for i in (1, 2, 4, 5): placeHex(outer, i, 5)

def draw_map_def_hex_inner():
    # hardcoded !!
    COLS = range(1, 5+1)
    ROWS = (3, 4, 5, 4, 3)
    OFFSETS = (2, 1, 1, 1, 2)
    pairs = zip(COLS, ROWS, OFFSETS)
    for column, tiles, off in pairs:
        for row in range(tiles):
            placeHex(random.choice(hexlands), column, row+off)

    # i am NOT HAPPY with this
    # not ELEGANT
def draw_map_def_hex_v2():
    draw_map_def_hex_outer()
    draw_map_def_hex_inner()


#----- SETUP ------------------------------------------------------

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', COORD_TILES_FONT_SIZE)
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
W, H = screen.get_size()
print(f"Screen size: {W} x {H}")
"""
* HANDLE FULLSCREEN LOGIC,
* calculate 'SCA' scalar accordingly to user's display
"""
tileSize = 46  # shouldn!t be needed
tilesRange = 7
mindim = min(W, H)
SCALE = mindim/tilesRange//tileSize # round_down  # capitals?
print("scale:", SCALE)
# test! vary! check tiling!
surf_board = pygame.Surface((W//SCALE, H//SCALE))
print(surf_board.get_size())


draw_map_def_hex_v2()


# placeHex("Sea.png", 1, 1)
# placeHex("Sea.png", 2, 1)
# placeHex("Sea.png", 4, 1)
# placeHex("Sea.png", 5, 1)
#
# placeHex("Sea.png", 1, 6)
# placeHex("Sea.png", 2, 6)
# placeHex("Sea.png", 4, 6)
# placeHex("Sea.png", 5, 6)




""" ---> This is the correct approach, but need to downscale bar.png
# bottom_bar
img = pygame.image.load("textures/gui/bar.png").convert_alpha()
w, h = img.get_size()
surf_board.blit(img, ((1920-w)//2, 1080-h))
"""

surf_board = pygame.transform.scale_by(surf_board, (SCALE, SCALE))
screen.blit(surf_board, (0,0))

""" this should go away """
img = pygame.image.load("textures/gui/bar.png").convert_alpha()
w, h = img.get_size()
screen.blit(img, ((1920-w)//2, 1080-h))

pygame.display.flip()

#----- EVENT LOOP ------------------------------------------------------

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.display.quit()
pygame.quit()
sys_exit()




