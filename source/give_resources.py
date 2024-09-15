from source.gameboard_tables import default_map_table_transposed as map_table
from source.gameboard_tables import default_yield_table_transposed as yield_table

from source.get_dice_roll import get_dice_roll


def get_resources_dict():
    """ ### PURE MAGIC ### """
    new_dict = dict()
    for i, (row, sow) in enumerate(zip(map_table, yield_table)):
        for j, (col, dol) in enumerate(zip(row, sow)):
            print("col dol:", col, dol)
            entry = ( (i, j), col)
            if dol in ["Sea", 0, ' ']:
                continue
            if dol not in new_dict:
                new_dict[dol] = []
            new_dict[dol].append(entry)
    return new_dict


def do_something(inner_dict: dict):
    roll = get_dice_roll()

    for tile in inner_dict[roll]:
