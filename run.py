#!/usr/bin/env python3
# 202408032257-Polesovice

# ----- IMPORTS -------------------------------------------------------

import pygame
from sys import exit as sys_exit
from random import randint

import source.constants as C
import source.sprites as sprites
import source.main_surface_class as main_surface
# import source.mapgen as mapgen_v1
import source.mapgen_v2 as mapgen_v2
import source.node_edge as node_edge
# import source.gui_manager as gui_man

# ----- NOTES ---------------------------------------------------------

"""
* pygame --> proper WINDOW startup?
* NOMENCLATURE: Tile, hex, circle (cake), ring.
  DOCUMENTATION? < graphical OVERVIEW
* hexcoords & tilecoords = pixelcoords & displaycoords
* -function-assembly- --> TRANSFORMS. (All-in-one placement? Tile+Overlay)
* SPRITES vs PIECES modules COLLISION --> unite
* SEA CAKE (?)
* Transforms: tile_hex2pix: tile_size get default parameter from MainSurface class?
* From source.FileClass import *  --> class_file.ClassName() becomes just ClassName()
* NOMENCLATURE: Size? Pix, hex.. (Abs/Scr/Dsp)  -->  Coordinates & Position?
* transforms.py >> set funkci pro vypocet position of spritu pro edges and vertices (nodes)
* SCALING: There are no fixed dimensions : MainSurface (Canvas?) gets scaled down
  accordingly to user's display, so that all pixels are scaled by an INTEGER NUMBER
  TLRD; (1) Scale down -> (2) Put sprites -> (3) Scale up .
* Zajimave pozorovani, ze pygame window se spusti na te obrazovce, kde je kurzor.
"""

# ----- TODO ----------------------------------------------------------

"""
(1) blitovani textu
    # mSurface.put_text((15, 15), "Press 'Q' to exit.", 18, (255, 50, 50))

(2) gui_manager.py

(3) oddeleni karet

(4) Main loop - external key handler 
    Rozdeleni key_handleru v main loopu do externich funkci.

(5) Render loop
    Draw map again after refocus.
    
(6) Desert
    Correct placement and zero yield
"""

# ----- CONSTANTS -----------------------------------------------------

# ----- FUNCTIONS -----------------------------------------------------

def get_dice_roll():
    dice1 = randint(2, 6)
    dice2 = randint(2, 6)
    roll_ = dice1 + dice2
    return roll_

# ----- SETUP ---------------------------------------------------------

pygame.init()
screen = main_surface.screen_init()  # separate to file screen.py
mSurface = main_surface.MainSurface(screen.get_size(), C.MAP_SIZE)  # Name Collision !

atlas = sprites.Atlas()
atlas.init_all()
mSurface.set_atlas(atlas)


C.DO_SHIFT_FIRST_COLUMN_DOWN = True
# mapgen_v1.draw_rect_map(mSurface, MAP_SIZE)
mapgen_v2.draw_map_from_table(mSurface)
# node_edge.draw_nodes_rect(mSurface, MAP_SIZE)
node_edge.draw_default_map_nodes(mSurface)

CARD_BOTTOM_OFFSET = 5  # NOMENCLATURE: Margin + Padding
CARD_BETWEEN_OFFSET = 5
card_wh = atlas.atlas_dict["cards"]["Brick"].get_size()
# print("cards wh", card_wh)
x = mSurface.w // 3 + 20
y = mSurface.h - CARD_BOTTOM_OFFSET - card_wh[1]
for name, card in atlas.atlas_dict["cards"].items():
    x = x + card_wh[0] + CARD_BETWEEN_OFFSET
    card_coords = (x, y)
    mSurface.blit2(card, card_coords)


mSurface.scale_by()
screen.blit(mSurface.surf_board, (0, 0))


# ----- EVENT LOOP ----------------------------------------------------

run = True
k_space_pressed_doubler = False

while run:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("Quitting game.")
            run = False

        # keys = pygame.key.get_pressed()
        # if keys[pygame.KMOD_CTRL]:
        #     print("MOD_CTRL")
        # if keys[pygame.K_q]:
        #     print("KEY: q")
        # if keys[pygame.KMOD_CTRL] and keys[pygame.K_q]:
        #     run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                print("Key Q pressed. -> Quitting game.")
                run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Key SPACE pressed.")
                if k_space_pressed_doubler:
                    print("Second time. -> Rolling dice.")
                    roll = get_dice_roll()
                    # WARNING - Already scaled up!!! :/
                    # Different solution -needed- required!
                    # Requires a(!) different approach.
                    mSurface.put_text((1550, 270), "Kostky vrhly:", 40, (100, 200, 50))
                    mSurface.put_text((1600, 320), str(roll), 100, (200, 200, 220))
                    screen.blit(mSurface.surf_board, (0, 0))
                    # Asi bude nutna jina classa na gamescreen, ktera spoji board a gui
                    k_space_pressed_doubler = False
                else:
                    k_space_pressed_doubler = True
                    pygame.draw.rect(mSurface.surf_board, (50, 50, 50), pygame.Rect(1600, 320, 100, 100))
                    screen.blit(mSurface.surf_board, (0, 0))

    pygame.display.update()

pygame.display.quit()
pygame.quit()
sys_exit()




