#!/usr/bin/env python3
# 202408032257-Polesovice

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
"""

# ----- IMPORTS -------------------------------------------------------

import pygame
from sys import exit as sys_exit
import source.mapgen as mapgen
import source.render as render

# ----- CONSTANTS -----------------------------------------------------

# ----- FUNCTIONS -----------------------------------------------------

# ----- SETUP ---------------------------------------------------------

pygame.init()
screen = render.screen_init()
dims = screen.get_size()
mySurface = render.MySurface(dims)
mapgen.draw_map_def_hex_v2(mySurface)
mySurface.scale_by()
screen.blit(mySurface.surf_board, (0,0))

# ----- EVENT LOOP ----------------------------------------------------

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.display.quit()
pygame.quit()
sys_exit()




