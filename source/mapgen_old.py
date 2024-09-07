"""
def draw_map_rectangle(w, h):
    for c in range(w):
        for r in range(h):
            type = random.choice(hexstack.lands)
            place_hex(type, c, r)
    for f in range(7):
        place_hex("Sea.png", 0, f)
        place_hex("Sea.png", 6, f)
        place_hex("Sea.png", f, 0)
        place_hex("Sea.png", f, 6)


def draw_map_def_hex_v1():
    draw_map_rectangle(7, 7)
    outer = "Template_vert.png"
    outer = "Sea.png"
    for f in range(7):
        place_hex(outer, 0, f)
        place_hex(outer, 6, f)
        place_hex(outer, f, 0)
        place_hex(outer, f, 6)
    place_hex(outer, 1, 1)
    place_hex(outer, 5, 1)
    place_hex(outer, 1, 5)
    place_hex(outer, 2, 5)
    place_hex(outer, 4, 5)
    place_hex(outer, 5, 5)
"""