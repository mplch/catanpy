from random import shuffle

import source.settings as settings

# DEFAULT ?

cake_stack = []

folder_plates = "textures/plates/"
folder_cakes = "textures/cakes/"

cake_dir = {
    "Clay_pit": 3,
    # "Desert": 1,
    "Field": 4,
    "Forest": 4,
    "Mountains": 3,
    "Pasture": 4,
    "Sea": 0,
}

for key, val in cake_dir.items():
    for _ in range(val):
        cake_stack.append(key)

shuffle(cake_stack)

# ---------------------------------------------------------------------

yield_stack = []

yield_dir = {
    "2": 1,
    "3": 2,
    "4": 2,
    "5": 2,
    "6": 2,
    "8": 2,
    "9": 2,
    "10": 2,
    "11": 2,
    "12": 1,
    # "0": 1,  # Desert!
}

for key, val in yield_dir.items():
    for _ in range(val):
        yield_stack.append(key)

if settings.YIELDS_DO_RANDOM_SHUFFLE:
    shuffle(yield_stack)
