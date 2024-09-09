from random import shuffle
import source.constants as C

# default_plate = "textures/plates/Field.png"

cake_stack = []

folder_plates = "textures/plates/"
folder_cakes = "textures/cakes/"

cake_dir = {
    "Clay_pit": 3,
    "Desert": 1,
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

"""
hex_stack = []

folder = "textures/hexes/"

hexdir = {
    "Clay_pit": 3,
    "Desert": 1,
    "Field": 4,
    "Forest": 4,
    "Mountains": 3,
    "Pasture": 4,
    "Sea": 0,
}

for key, val in hexdir.items():
    for _ in range(val):
        hex_stack.append(key)

shuffle(hex_stack)
"""

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
    # !!!
    "0": 1,  # Desert!
}

for key, val in yield_dir.items():
    for _ in range(val):
        yield_stack.append(key)

if C.YIELDS_DO_RANDOM_SHUFFLE:
    shuffle(yield_stack)
else:
    """ places yield in columns """

    letters = """
A = 5
B = 2
C = 6
D = 3
E = 8
F = 10
G = 9
H = 12
I = 11
J = 4
K = 8
L = 10
M = 9
N = 4
O = 5
P = 6
Q = 3
R = 11
_ = 0
""".strip('\n').split('\n')  # Desert ZERO !!!

    # for i in letters: print(i)
    # print(letters)

    numbers = []

    for oc in letters:
        new = oc[4:]
        # print(new)
        numbers.append(new)

    yield_stack = numbers

    # tady je jen problem, ze musim zetony
    # polozit ve spravnem poradi
    # navic je to trochu hnus, ale asi nevim,
    # jak to udelat lepe...
