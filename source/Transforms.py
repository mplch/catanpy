import constants as C

# hex | pix | abs
# display coords dsp (?) NO.


def hex2pix(hex_coords, tile_size):

    c, r = hex_coords

    if c % 2 == C.DO_SHIFT_FIRST_COLUMN_DOWN:
        x = C.MAP_OFF_PIX_X + c * (tile_size - C.HOR_CON)
        y = C.MAP_OFF_PIX_Y + r * (tile_size - C.VER_CON)
        pix_coords = (x, y)

    else:
        x = C.MAP_OFF_PIX_X + c * (tile_size - C.HOR_CON)
        y = C.MAP_OFF_PIX_Y + r * (tile_size - C.VER_CON) + (tile_size - C.STRIP_HEIGHT) // 2
        pix_coords = (x, y)

    return pix_coords
