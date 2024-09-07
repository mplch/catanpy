from random import randint

import source.pieces as pieces


def get_outer_ring_hexcoords():

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

    # I am NOT HAPPY with this
    # not ELEGANT

    return inner_ring


def draw_map_def_hex_outer(my_surface):

    outer = "Sea.png"

    outer_ring = get_outer_ring_hexcoords()

    for coords in outer_ring:
        my_surface.place_hex(outer, coords)


def draw_map_def_hex_inner(my_surface):
    for coords in get_inner_ring_hexcoords():
        hextype = pieces.hex_stack.pop()
        hextype += ".png"
        my_surface.place_hex(hextype, coords)


def draw_map_def_hex_yield_overlay(my_surface):
    for coords in get_inner_ring_hexcoords():

        yield_number = pieces.yield_stack.pop()

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