from random import randint

import source.gui_manager as gui_man

from source.gameboard_tables import default_map_table_transposed as map_table
from source.gameboard_tables import default_yield_table_transposed as yield_table

from source.get_dice_roll import get_dice_roll
from source.main_surface_class import MainSurface
from source.transforms import PixCoord


F = "Forest"
P = "Pasture"
M = "Mountains"
C = "Clay_pit"
E = "Field"

b = "Brick"
o = "Rock" # r,c! # Ore
s = "Sheep"
w = "Wood"
g = "Wheat" # grains

tile_list = ["Clay_pit", "Field", "Forest", "Mountains", "Pasture"]
card_list = ["Brick", "Rock", "Sheep", "Wood", "Wheat"]

tile_resource_dict = {
    F: w,
    P: s,
    M: o,
    C: b,
    E: g,
}


def get_resources_dict():
    """ ### PURE MAGIC ### """
    new_dict = dict()
    for i, (row, sow) in enumerate(zip(map_table, yield_table)):
        for j, (col, dol) in enumerate(zip(row, sow)):
            # print("col dol:", col, dol)
            entry = ( (i, j), col)
            if dol in ["Sea", 0, ' ']:
                continue
            if dol not in new_dict:
                new_dict[dol] = []
            new_dict[dol].append(entry)
    return new_dict


def evaluate_roll(
                inner_surface: MainSurface,
                inner_dict: dict,
                roll: int,
                ):

    if roll == 7:
        print("ROBBERY!")
        return

    for tile in inner_dict[roll]:
        print("evaluating:", tile)
        resource = tile_resource_dict[tile[1]]
        x = randint(0, inner_surface.w)
        y = randint(0, inner_surface.h)
        gui_man.show_resource_card(inner_surface, resource, PixCoord(x,y))

