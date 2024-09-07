from random import shuffle

stack = []

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
        stack.append(key)

shuffle(stack)