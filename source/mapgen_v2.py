from random import randint, choice

import source.pieces as pieces
import source.map_table_file as map_table_file
from source.main_surface_class import MainSurface
from source.tiletype import TileType


OCCUPIED = 'O'  # WHERE THIS? Constants.py? Map_table_file.py?


def draw_tile_yield_overlay(my_surface: MainSurface,
                            hex_coords: tuple[int, int]
                            ):
    yield_number = pieces.yield_stack.pop()
    my_surface.place_yield(hex_coords, yield_number)


def draw_map_from_table(my_surface: MainSurface,
                        map_table: list[list[str]]
                            =map_table_file.default_map_table_transposed,
                        draw_yields: bool =True
                        ):

    print(OCCUPIED)

    for r, row in enumerate(map_table):
        for c, tile_string in enumerate(row):

            hex_coords = (r, c)

            print(f"Draw Map INFO: {hex_coords}, >{tile_string}<")

            if tile_string == OCCUPIED:
                cake_type = pieces.cake_stack.pop()
                hex_type = TileType("Land", cake_type)
                my_surface.place_hex(hex_type, hex_coords)
                if draw_yields:
                    draw_tile_yield_overlay(my_surface, hex_coords)
                continue

            if tile_string == "Sea":
                tile_type = TileType("Sea", "Sea")
                my_surface.place_hex(tile_type, hex_coords)
                continue

            # predefined tiles handler
            # need to remove them from hex_stack (!)

            if tile_string == ' ':
                continue

            raise Exception("Error: map_gen_v2.py: UNKNOWN tile string.")


    return


### OLD FUNC ###
def draw_rect_map(my_surface: MainSurface, n_m):
    n, m = n_m
    for r in range(n):
        for c in range(m):
            coords = r,c
            cake_type = choice(pieces.cake_stack)
            hex_type = TileType("TemPlate", cake_type)
            my_surface.place_hex(hex_type, coords)
    return