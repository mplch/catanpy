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
import source.hexstack as hexstack
import source.mapgen as mapgen
import source.render as render
# NOMENCLATURE: Tile, hex, circle (cake), ring.

#----- CONSTANTS ------------------------------------------------------

"""
SCA = 5
d = 160
s = 5  # scale: 5*32=160
# shouldn't be needed actually
"""

hx = "textures/hexes/Template_horiz.png"




#----- FUNCTIONS ------------------------------------------------------




#----- SETUP ------------------------------------------------------

pygame.init()
screen = render.screen_init()


# render.window_postinit(screen, surf_board)

mymymysurface = render.MySurface

mapgen.draw_map_def_hex_v2(mymymysurface)

screen.blit(mymymysurface.surf_board, (0,0))


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




