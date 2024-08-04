#!/usr/bin/env python3
#202408032257-Polesovice

#----- NOTES ------------------------------------------------------

"""
* pygame transparent screen when run from explorer
* EDIT: Skaluji canvas --> RESI pozdejsi pokladani budov
* je potreba spravne zadefinovat transformacni souradnicove funkce
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

#----- FUNCTIONS ------------------------------------------------------

def putTile(file, coords):
    img = pygame.image.load(file).convert_alpha()
    # load all images just once, then just copy them (directly place)
    #    img = pygame.transform.scale_by(img, (SCA, SCA))
    surf_board.blit(img, coords)

def draw_map_ocean(w, h):
    x_off, y_off = 450, 50
    x_off, y_off = 85, 5
    hor_con, ver_con = 10, 6
    # uz si nepamatuji, co melo byt con,
    # connect urcite ne, conformation...nevim
    for c in range(w):
        if c % 2 == 0:
            for r in range(h):
                x = x_off + c * (tileSize - hor_con)
                y = y_off + r * (tileSize - ver_con)
                putTile(hx, (x, y))
        else:
            for r in range(h):
                x = x_off + c * (tileSize - hor_con)
                y = y_off + r * (tileSize - ver_con) + tileSize // 2 - 3  # magic number 3 ?!
                putTile(hx, (x, y))
    """
    * takto je to mozna nejprehlednejsi. --> Funguje to? funguje!
    """

#----- SETUP ------------------------------------------------------

pygame.init()
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

draw_map_ocean(7, 7)

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




