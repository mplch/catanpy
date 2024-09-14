import source.pieces as pieces
from source.main_surface_class import MainSurface
from source.tiletype import TileType
from random import choice


def get_outer_ring_hex_coords():

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


def get_inner_ring_hex_coords():
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


def draw_map_def_hex_outer_ocean(my_surface):
    tile_type = TileType("Sea", "Sea")
    for coords in get_outer_ring_hex_coords():
        my_surface.place_hex(tile_type, coords)


# Hezkyy, tohle je vlastne funkce, ktera modifikuje objekt "z vnejsku"
def draw_map_def_hex_inner_land(my_surface):
    for coords in get_inner_ring_hex_coords():
        cake_type = pieces.cake_stack.pop()
        # hex_type = TileType("Land", cake_type)
        hex_type = TileType("TemPlate", cake_type)
        my_surface.place_hex(hex_type, coords)


def draw_map_def_hex_yield_overlay(my_surface):
    for coords in get_inner_ring_hex_coords():
        yield_number = pieces.yield_stack.pop()
        my_surface.place_yield(coords, yield_number)


def draw_map_def_hex_v2(m):
    draw_map_def_hex_outer_ocean(m)
    draw_map_def_hex_inner_land(m)
    draw_map_def_hex_yield_overlay(m)

def draw_rect_map(my_surface: MainSurface, n_m):
    n, m = n_m
    for r in range(n):
        for c in range(m):
            coords = r,c
            cake_type = choice(pieces.cake_stack)
            hex_type = TileType("TemPlate", cake_type)
            my_surface.place_hex(hex_type, coords)
    return
