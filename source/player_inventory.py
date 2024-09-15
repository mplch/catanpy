## RENAME TO JUST INVENTORY

b = "Brick"
o = "Rock" # r,c! # Ore
s = "Sheep"
w = "Wood"
g = "Wheat" # grains

class Inventory:

    resource_counter: dict
    building_counter: dict

    resource_counter = {
        b: 0,
        o: 0,
        s: 0,
        w: 0,
        g: 0,
    }

    """ Later... """
    building_counter = {
        "village": 5,
        "city": 4,
        "road": 15,
    }

    def __init__(self):
        pass