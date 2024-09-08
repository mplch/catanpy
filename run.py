#!/usr/bin/env python3
# 202408032257-Polesovice

# ----- IMPORTS -------------------------------------------------------

import pygame
from sys import exit as sys_exit
import source.mapgen as mapgen
import source.render as render
import source.gui_manager as gui_man

# ----- NOTES ---------------------------------------------------------

"""
* pygame --> proper WINDOW startup?
* set funkci pro TRANSFORMACI souradnic
* CENTRICKE souradnice? : Asi spis neni nutne..
* NOMENCLATURE: Tile, hex, circle (cake), ring.
* DOCUMENTATION? < graphical OVERVIEW
* hexcoords & tilecoords = pixelcoords & displaycoords
"""

# ----- TODO ----------------------------------------------------------

"""
(*) render.py:
put_tile():
    * Image CACHING
    * Load all images just once, then just copy them
get_scale():
    * Test! vary! check tiling!
* RESTRUCTURE place_hex and put_tile and print_coords function
* Use of STATIC functions instead of methods
* TEMPLATE tiles ponechat ciste jako ilustrativni
  --> assertovat spravnost kazde krajiny (jak?
* Function SEPARATION, consider more FILES
* Argument order CONSISTENCY, e.g. coords
"""

# ----- CONSTANTS -----------------------------------------------------

# ----- FUNCTIONS -----------------------------------------------------

# ----- SETUP ---------------------------------------------------------

pygame.init()
screen = render.screen_init()
dims = screen.get_size()
mSurface = render.MainSurface(dims)
mapgen.draw_map_def_hex_v2(mSurface)
mSurface.put_text((300, 15), "AHOJ POZEMSTAAANE !!!")
mSurface.put_text((15, 15), "Presovani Quecka", 18, (255, 50, 50))
mSurface.put_text((15, 30), "Te vypne brasko. B-)", 18, (255, 50, 50))
mSurface.scale_by()
screen.blit(mSurface.surf_board, (0,0))

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
                    roll = mapgen.get_dice_roll()
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




