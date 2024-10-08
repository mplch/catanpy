#!/usr/bin/env python3
# 202408032257-Polesovice
from idlelib.debugobj import myrepr

# ----- IMPORTS -------------------------------------------------------

import pygame
from sys import exit as sys_exit



import source.constants as C
import source.settings as settings
import source.sprites as sprites
import source.main_surface_class as main_surface
import source.mapgen_v2 as mapgen_v2
import source.node_v2 as nodes_v2
import source.gui_manager as gui_man
import source.give_resources as give_resources
import source.sprite_constants_importer as SPRITE_CONSTANTS

from source.get_dice_roll import get_dice_roll
from source.player_inventory import Inventory

from source.transforms import HexCoord, PixCoord, AbsCoord

# ----- NOTES ---------------------------------------------------------

"""
 * pygame --> proper WINDOW startup?
 * NOMENCLATURE: Tile, hex, circle (cake), ring. DONE. (Not documented.)
   DOCUMENTATION? < graphical OVERVIEW
 * -function-assembly- --> TRANSFORMS. (All-in-one placement? Tile+Overlay)
 * SPRITES vs PIECES modules COLLISION --> unite
 * Transforms: tile_hex2pix: tile_size get default parameter from MainSurface class?
 * NOMENCLATURE: Size? Pix, hex.. (Abs/Scr/Dsp)  -->  Coordinates & Position?
   --> Made coordinates CLASSes
   --> Position ??!
 * SCALING: There are no fixed dimensions : MainSurface (Canvas?) gets scaled down
   accordingly to user's display, so that all pixels are scaled by an INTEGER NUMBER
   TLRD; (1) Scale down -> (2) Put sprites -> (3) Scale up .
 * Zajimave pozorovani, ze pygame window se spusti na te obrazovce, kde je kurzor.
 * Classes without default parameters - only type declaration and constructor? Should work.
 * Ports might be a "Sea token" - similarly to "Yield token".
 * Center yield numbers --> NOT NEED TO --> .. well, maybe for overlay..
 * NAMING CONVENTION: file_name.py ClassName, objectName, object_in_function_name... HUH?
 * CleverNote: Atlas je pridan jako .promenna tridy MainSurface
"""

# ----- IDEAS ---------------------------------------------------------

"""
 * Natural disasters 
 * No Main Menu -> Instant play
   Get player directly to latest/new game.
   In-game Menu.
 * End Screen
   photos of Czechia landscapes
   cleared of most industrial disruptions
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
    
(7) #### !!!!!!!! ####
         c, r = rc
    #### !!!!!!!! ####
--> coordinates might be messed up!!

(8) Default settings

(9) Correct (r, c) --> MAP ROTATION
    Node are rr, cc
    Tiles are c, r
    ... Ale pritom nody davam taky po sloupcich a funguje to...
    
(10) Desert settings
     Center vs Random
     Zero Yield !
     
(11) Yields generator

(12) Generated mapa data structure (table)
     Need for giving resources
     Its just being draw directly

"""

# ----- CONSTANTS -----------------------------------------------------

# ----- FUNCTIONS -----------------------------------------------------

# ----- SETUP ---------------------------------------------------------

pygame.init()
screen = main_surface.screen_init()  # separate to file screen.py
mSurface = main_surface.MainSurface(screen.get_size(), C.MAP_SIZE)  # Name Collision !

atlas = sprites.Atlas()
atlas.init_all()
mSurface.set_atlas(atlas)

# mapgen_v2.draw_rect_map(mSurface, C.MAP_SIZE)
mapgen_v2.draw_map_from_table(mSurface)


# nodes_v1.draw_nodes_rect(mSurface, C.MAP_SIZE)
# nodes_v2.draw_inner_nodes(mSurface)

map_nodes_list = nodes_v2.get_valid_nodes_list()
nodeTable = nodes_v2.NodeTable(map_nodes_list)
# nodeTable.add_node(HexCoord(5, 6), "village_red")
nodeTable.add_node(HexCoord(5, 6), "r")
nodeTable.add_node(HexCoord(3, 3), "r")
nodeTable.add_node(HexCoord(10, 3), "R")
nodeTable.add_node(HexCoord(12, 4), "R")
print(nodeTable)


# nodes_v2.draw_node_from_table(mSurface, nodes_v2.global_node_table)
nodes_v2.draw_node_table(mSurface, nodeTable)


nodes_v2.highlight_hex_neighbour_nodes(mSurface, HexCoord(3, 3))


""" Shouldn't this be elsewhere ??? """
if settings.SHOW_YIELDS:
    # mapgen_v2.draw_yields_from_map_table(mSurface)
    # mapgen_v2.draw_yields_from_matrix(mSurface)
    mapgen_v2.draw_yields_from_table(mSurface)


players = ["red", "orange", "blue", "white"]
player_inventories = dict()
for player in players:
    player_inventories[player] = Inventory()



addict = give_resources.get_resources_dict()
print("dict:")
for entry, val in addict.items():
    print(' '*3, entry, val)


# roll = get_dice_roll()
# give_resources.evaluate_roll(mSurface, addict, roll)


gui_man.draw_card_deck_prototype(mSurface)


gui_man.show_card_decks(mSurface, 4)


mSurface.scale_by()
screen.blit(mSurface.surf_board, (0, 0))


# ----- EVENT LOOP ----------------------------------------------------

run = True
k_space_pressed_doubler = False
player_index = -1

while run:

    player_index += 1
    player_index %= 4  # Nice, I like this solution.

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

                    # AbsCoord !!!  # Nevidi, protoze AbsCoord je podtrida PixCoord
                    mSurface.put_text(AbsCoord(1550, 270), "Kostky vrhly:", 40, (100, 200, 50))
                    # Is instance of
                    mSurface.put_text(AbsCoord(1600, 320), str(roll), 100, (200, 200, 220))
                    give_resources.evaluate_roll(mSurface, addict, roll)

                    """ Player inventory?? """

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




