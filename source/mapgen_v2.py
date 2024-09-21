from random import randint, choice



import source.settings as settings
import source.pieces as pieces
import source.gameboard_tables as gameboard_tables

from source.main_surface_class import MainSurface
from source.tiletype import TileType
from source.transforms import HexCoord
# from source.custom_type_classes import Matrix


OCCUPIED = 'O'  # WHERE THIS? Constants.py? Map_table_file.py?


""" Shouldn't this be a gen functions instead of draw? 
    (Sadly, they just read tables and dont generate anything.)
"""


def toss_yield_token(my_surface: MainSurface, hex_coord: HexCoord):
    """ Docstring """
    """ Where should this function live? """
    yield_number = pieces.yield_stack.pop()
    my_surface.put_yield(hex_coord, yield_number)


def draw_gameboard_from_tables():
    pass


def draw_map_from_table(my_surface: MainSurface,
                        map_table: list[list[str]]
                            =gameboard_tables.default_map_table_transposed,
                        # show_yields: bool =settings.SHOW_YIELDS,
                        show_coords: bool =settings.SHOW_COORDS,
                        ):

    for r, row in enumerate(map_table):
        for c, tile_string in enumerate(row):

            hex_coord = HexCoord(r, c)

            print("    mapgen:", tile_string, "at", hex_coord)

            # if tile_string == OCCUPIED:
            #     cake_type = pieces.cake_stack.pop()
            #     hex_type = TileType("Land", cake_type)
            #     my_surface.place_hex(hex_type, hex_coord)
            #     if show_coords:
            #         my_surface.put_node_coord(hex_coord)
            #     # if show_yields:
            #     #     draw_tile_yield_overlay(my_surface, hex_coord)
            #     continue

            if tile_string == "Sea":
                tile_type = TileType("Sea", "Sea")
                my_surface.place_hex(tile_type, hex_coord)
                if show_coords:
                    my_surface.put_node_coord(hex_coord)
                continue

            # predefined tiles handler
            # need to remove them from hex_stack (!)

            if tile_string == "Desert":
                tile_type = TileType("Desert", "Desert")
                my_surface.place_hex(tile_type, hex_coord)
                if show_coords:
                    my_surface.put_node_coord(hex_coord)
                continue

            if tile_string == ' ':
                if show_coords:
                    my_surface.put_node_coord(hex_coord)
                continue

            if tile_string in pieces.cake_dir:
                # check count (!)
                tile_type = TileType("Land", tile_string)
                my_surface.place_hex(tile_type, hex_coord)
                if show_coords:
                    my_surface.put_node_coord(hex_coord)
                continue

            raise Exception("UNKNOWN tile string.")
    return


### OLD FUNC ###
def draw_rect_map(my_surface: MainSurface, n_m):
    n, m = n_m
    for r in range(n):
        for c in range(m):
            hex_coord = HexCoord(r, c)
            cake_type = choice(pieces.cake_stack)
            hex_type = TileType("TemPlate", cake_type)
            my_surface.place_hex(hex_type, hex_coord)
    return
### -------- ###


def draw_yields_from_table(my_surface: MainSurface,
                               yield_table: list[list[str]]
                                   =gameboard_tables.default_yield_table_transposed,
                               ):

    for r, row in enumerate(yield_table):
        for c, yield_num in enumerate(row):

            hex_coord = HexCoord(r, c)

            print("    yield num:", yield_num, "at", hex_coord)

            if yield_num == 0:  # Desert
                continue

            if str(yield_num) in pieces.yield_dir:
                my_surface.put_yield(hex_coord, yield_num)
                continue

            if yield_num == "Sea":
                continue

            if yield_num == ' ':
                continue

            raise Exception("UNKNOWN yield num.")

    return


# def draw_yields_from_matrix(my_surface: MainSurface,
#                            yield_matrix: Matrix =None,
#                            ):
#
#     if yield_matrix is None:
#         yield_matrix = Matrix()
#         default = gameboard_tables.default_map_table_transposed
#         yield_matrix.from_table(default)
#
#     # available_yields = pieces.yield_stack.copy()
#
#     for r, row in enumerate(yield_matrix.table):
#         for c, yield_num in enumerate(row):
#
#             hex_coord = HexCoord(r, c)
#
#             if yield_num == "Desert":
#                 continue
#
#             # if yield_num in available_yields:
#             #     available_yields.remove(yield_num)
#             if str(yield_num) in pieces.yield_dir:
#                 my_surface.put_yield(hex_coord, yield_num)
#                 continue
#
#             if yield_num == "Sea":
#                 continue
#
#             if yield_num == ' ':
#                 continue
#
#             raise Exception("UNKNOWN yield num.")
#
#     return


def draw_yields_from_map_table(my_surface: MainSurface,
                               map_table: list[list[str]]
                                   =gameboard_tables.default_map_table_transposed,
                               ):

    for r, row in enumerate(map_table):
        for c, tile_name in enumerate(row):

            hex_coord = HexCoord(r, c)

            if tile_name == "Desert":
                continue

            if tile_name == OCCUPIED:
                toss_yield_token(my_surface, hex_coord)
                continue

            if tile_name == "Sea":
                continue

            if tile_name == ' ':
                continue

            raise Exception("UNKNOWN yield num.")

    return

