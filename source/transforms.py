import source.constants as C

# hex | pix | abs
# display coords dsp (?) NO.


def tile_hex2pix(hex_coords, tile_size):
    # How to get default parameter from main surface clas??
    # Complication: Cyclic import
    # Maybe there is no better solution than to insert this function UNDER MainSurface class

    c, r = hex_coords

    if c % 2 == C.DO_SHIFT_FIRST_COLUMN_DOWN:
        x = C.MAP_OFF_PIX_X + c * (tile_size - C.HEX_OVERLAP_X)
        y = C.MAP_OFF_PIX_Y + r * (tile_size - C.HEX_OVERLAP_Y)

    else:
        x = C.MAP_OFF_PIX_X + c * (tile_size - C.HEX_OVERLAP_X)
        y = C.MAP_OFF_PIX_Y + r * (tile_size - C.HEX_OVERLAP_Y) + (tile_size - C.STRIP_HEIGHT) // 2 + C.REMOVE

    pix_coords = (x, y)

    return pix_coords


def node_hex2pix(hex_coords: tuple[int, int]):

    r, c = hex_coords

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

    if C.DO_SHIFT_FIRST_COLUMN_DOWN:
        y -= (C.TILE_SIZE - C.STRIP_HEIGHT) // 2 + C.REMOVE

    pix_coords = (x,y)

    return pix_coords


def transpose(old):

    r_new = len(old[0])
    c_new = len(old)

    new_matrix = []
    for i in range(r_new):
        new_row = []
        for j in range(c_new):
            new_row.append(old[j][i])
        new_matrix.append(new_row)

    return new_matrix
