import pygame
import source.hexstack as hexstack
import source.constants as C
import source.render as render

# #######x
# hexstack.folder = hexstack.hexstack.folder
# hexstack.lands = hexstack.hexstack.lands
# hexstack.types = hexstack.hexstack.types
# #######

###########################


"""
def draw_map_rectangle(w, h):
    for c in range(w):
        for r in range(h):
            type = random.choice(hexstack.lands)
            place_hex(type, c, r)
    for f in range(7):
        place_hex("Sea.png", 0, f)
        place_hex("Sea.png", 6, f)
        place_hex("Sea.png", f, 0)
        place_hex("Sea.png", f, 6)


def draw_map_def_hex_v1():
    draw_map_rectangle(7, 7)
    outer = "Template_vert.png"
    outer = "Sea.png"
    for f in range(7):
        place_hex(outer, 0, f)
        place_hex(outer, 6, f)
        place_hex(outer, f, 0)
        place_hex(outer, f, 6)
    place_hex(outer, 1, 1)
    place_hex(outer, 5, 1)
    place_hex(outer, 1, 5)
    place_hex(outer, 2, 5)
    place_hex(outer, 4, 5)
    place_hex(outer, 5, 5)
"""


def draw_map_def_hex_outer(my_surface):
    # draw_map_rectangle(7, 7)
    outer = "Template_vert.png"
    outer = "Sea.png"
    for f in range(7):
        my_surface.place_hex(my_surface, outer, 0, f)
        my_surface.place_hex(my_surface, outer, 6, f)
        # surf_board = place_hex(surf_board, outer, 0, f)
        # surf_board = place_hex(surf_board, outer, 6, f)
        # tak tohle ne, tohle je za trest
        my_surface.place_hex(my_surface, outer, f, 0)
        my_surface.place_hex(my_surface, outer, f, 6)
    my_surface.place_hex(my_surface, outer, 1, 1)
    my_surface.place_hex(my_surface, outer, 5, 1)
    for i in (1, 2, 4, 5): my_surface.place_hex(my_surface, outer, i, 5)


def draw_map_def_hex_inner(my_surface):
    # hardcoded !!
    COLS = range(1, 5+1)
    ROWS = (3, 4, 5, 4, 3)
    OFFSETS = (2, 1, 1, 1, 2)
    pairs = zip(COLS, ROWS, OFFSETS)
    for column, tiles, off in pairs:
        for row in range(tiles):
            hextype = hexstack.stack.pop()
            hextype += ".png"
            my_surface.place_hex(my_surface, hextype, column, row+off)

    # i am NOT HAPPY with this
    # not ELEGANT
def draw_map_def_hex_v2(m):
    draw_map_def_hex_outer(m)
    draw_map_def_hex_inner(m)

############################################################