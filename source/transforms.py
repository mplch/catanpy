import source.constants as C

# hex | pix | abs

# ---------------------------------------------------------------------

class HexCoord:
    r = 0
    c = 0
    rc: tuple[int, int]

    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.rc = (r, c)

    def __str__(self):
        return f"({self.r}, {self.c})"


class PixCoord:
    x: int
    y: int
    xy: tuple[int, int]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xy = (x, y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    # Can I forbid to modify x,y / xy from outer scope?

    def update_tuple(self):
        self.xy = (self.x, self.y)

    def update_x_y(self):
        self.x, self.y = self.xy

    # __add__ method ??
    def add(self, other):  # other - PixCoord instead of Any type ?!
        self.x += other.x
        self.y += other.y
        self.update_tuple()


class AbsCoord(PixCoord):
    pass
# AbsCoord = PixCoord  # Remains PixCoord class


# ---------------------------------------------------------------------

def tile_hex2pix(hex_coord: HexCoord, tile_size: int =C.TILE_SIZE):
    # How to get default parameter from main surface clas??
    # Complication: Cyclic import
    # Maybe there is no better solution than to insert this function UNDER MainSurface class

    r, c = hex_coord.rc  # (?????!!)

    """ What is weird tho,
     is the reason - WHY should I add x to row and y to columns?? 
     Maybe its correct. I just dont see it. """

    if r % 2 == C.DO_SHIFT_FIRST_COLUMN_DOWN:
        x = C.MAP_OFF_PIX_X + r * (tile_size - C.HEX_OVERLAP_X)
        y = C.MAP_OFF_PIX_Y + c * (tile_size - C.HEX_OVERLAP_Y)

    else:
        x = C.MAP_OFF_PIX_X + r * (tile_size - C.HEX_OVERLAP_X)
        y = C.MAP_OFF_PIX_Y + c * (tile_size - C.HEX_OVERLAP_Y) + (tile_size - C.STRIP_HEIGHT) // 2 + C.REMOVE

    return PixCoord(x, y)


def node_hex2pix(hex_coord: HexCoord):

    """ I THINK HERE LIES THE PROBLEM """
    """ OR MAYBE IT DOES NOT """


    r, c = hex_coord.rc

    # Is it possible to SIMPLIFY the following?
    x = 0
    x += C.MAP_OFF_PIX_X
    x += C.NODE_OVERLAP_X
    x += c * C.HEX_HORI_EDGE_X
    x -= (c + 1) * C.NODE_STRIP
    x += (c // 2) * C.NEXT_COL_PAIR_OFFSET

    if c % 2 == 0:  # 1, 3, 5 ..
        x += (r % 2) * C.NODE_PULL_BACK
    else:
        x -= (r % 2) * C.NODE_PULL_BACK

    y = C.MAP_OFF_PIX_Y - C.STRIP_HEIGHT + r * C.HEX_HEIGHT // 2

    ### THIS IS NOT THE SOLUTION ###
    if C.DO_SHIFT_FIRST_COLUMN_DOWN:
        y -= (C.TILE_SIZE - C.STRIP_HEIGHT) // 2 + C.REMOVE

    # pix_coord = x, y
    # return pix_coord
    return PixCoord(x, y)
