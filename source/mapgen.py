import pygame
from random import randint

import source.hexstack as hexstack
# import source.constants as C
# import source.render as render

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


def get_outer_ring_hexcoords():
    # hexcoords & tilecoords = pixelcoords & displaycoords
    outer_ring = []

    ### POLADIT !!!

    for f in range(7):
        outer_ring.append((0, f))
        outer_ring.append((6, f))
        outer_ring.append((f, 0))
        outer_ring.append((f, 6))
    outer_ring.append((1, 1))
    outer_ring.append((5, 1))
    for i in (1, 2, 4, 5):
        outer_ring.append((i, 5))

    return outer_ring


def get_inner_ring_hexcoords():
    inner_ring = []

    # hardcoded !!
    cols = range(1, 5 + 1)
    rows = (3, 4, 5, 4, 3)
    offsets = (2, 1, 1, 1, 2)
    pairs = zip(cols, rows, offsets)
    for column, tiles, off in pairs:
        for row in range(tiles):
            inner_ring.append((column, row + off))

    # i am NOT HAPPY with this
    # not ELEGANT

    return inner_ring


def draw_map_def_hex_outer(my_surface):

    outer = "Sea.png"

    outer_ring = get_outer_ring_hexcoords()

    for x,y in outer_ring:
        my_surface.place_hex(outer, x,y)  # TUPLE CONDENSATION !


def draw_map_def_hex_inner(my_surface):

    for coords in get_inner_ring_hexcoords():

        x,y=coords

        hextype = hexstack.stack.pop()
        hextype += ".png"
        my_surface.place_hex(hextype, x,y)


def draw_map_def_hex_yield_overlay(my_surface):

    for coords in get_inner_ring_hexcoords():
        # x, y = coords

        ### EXCEPT THIS IS INCORRECT
        yield_number = get_dice_roll()

        my_surface.place_yield(coords, yield_number)


def draw_map_def_hex_v2(m):
    draw_map_def_hex_outer(m)
    draw_map_def_hex_inner(m)
    draw_map_def_hex_yield_overlay(m)


def get_dice_roll():
    dice1 = randint(2, 6)
    dice2 = randint(2, 6)
    roll = dice1 + dice2
    return roll


############################################################