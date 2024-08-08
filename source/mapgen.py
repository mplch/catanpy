import pygame
import source.hexstack as hexstack
import source.constants as C
import source.render as render

# #######x
# hexstack.folder = hexstack.hexstack.folder
# hexstack.lands = hexstack.hexstack.lands
# hexstack.types = hexstack.hexstack.types
# #######

###########################
def putTile(surf_board, type, coords):
    file = hexstack.folder + type
    img = pygame.image.load(file).convert_alpha()
    # load all images just once, then just copy them (directly place)
    #    img = pygame.transform.scale_by(img, (SCA, SCA)) # haha
    img = pygame.transform.rotate(img, 90)
    surf_board.blit(img, coords)
    return surf_board

def coordPrintTile(surf_board, c, r, x, y):
    my_font = render.get_font()
    text_surface = my_font.render(f"({c}, {r})", False, C.COORD_TILES_FONT_COLOR)
    surf_board.blit(text_surface, (x+C.COORD_TILE_X_OFFSET, y+C.COORD_TILE_Y_OFFSET))
    return surf_board


def placeHex(surf_board, type, c, r):
    # uz si nepamatuji, co melo byt con,
    # connect urcite ne, conformation...nevim
    x_off, y_off = 200, 5
    hor_con, ver_con = 10, 6
    doShiftFirstColumnDown = 1  # bool 0 or 1
    if c % 2 == doShiftFirstColumnDown:
        x = x_off + c * (C.TILE_SIZE - hor_con)
        y = y_off + r * (C.TILE_SIZE - ver_con)
        surf_board = putTile(surf_board, type, (x, y))
        coordPrintTile(c, r, x, y)
    else:
        x = x_off + c * (C.TILE_SIZE - hor_con)
        y = y_off + r * (C.TILE_SIZE - ver_con) + C.TILE_SIZE // 2 - 3  # magic number 3 ?!
        surf_board = putTile(surf_board, type, (x, y))
        coordPrintTile(c, r, x, y)
    return surf_board

"""
def draw_map_rectangle(w, h):
    for c in range(w):
        for r in range(h):
            type = random.choice(hexstack.lands)
            placeHex(type, c, r)
    for f in range(7):
        placeHex("Sea.png", 0, f)
        placeHex("Sea.png", 6, f)
        placeHex("Sea.png", f, 0)
        placeHex("Sea.png", f, 6)


def draw_map_def_hex_v1():
    draw_map_rectangle(7, 7)
    outer = "Template_vert.png"
    outer = "Sea.png"
    for f in range(7):
        placeHex(outer, 0, f)
        placeHex(outer, 6, f)
        placeHex(outer, f, 0)
        placeHex(outer, f, 6)
    placeHex(outer, 1, 1)
    placeHex(outer, 5, 1)
    placeHex(outer, 1, 5)
    placeHex(outer, 2, 5)
    placeHex(outer, 4, 5)
    placeHex(outer, 5, 5)
"""

def draw_map_def_hex_outer():
    # draw_map_rectangle(7, 7)
    outer = "Template_vert.png"
    outer = "Sea.png"
    for f in range(7):
        placeHex(outer, 0, f)
        placeHex(outer, 6, f)
        # surf_board = placeHex(surf_board, outer, 0, f)
        # surf_board = placeHex(surf_board, outer, 6, f)
        ## tak tohle ne, tohle je za trest
        placeHex(outer, f, 0)
        placeHex(outer, f, 6)
    placeHex(outer, 1, 1)
    placeHex(outer, 5, 1)
    for i in (1, 2, 4, 5): placeHex(outer, i, 5)

def draw_map_def_hex_inner():
    # hardcoded !!
    COLS = range(1, 5+1)
    ROWS = (3, 4, 5, 4, 3)
    OFFSETS = (2, 1, 1, 1, 2)
    pairs = zip(COLS, ROWS, OFFSETS)
    for column, tiles, off in pairs:
        for row in range(tiles):
            type = hexstack.stack.pop()
            type += ".png"
            placeHex(type, column, row+off)

    # i am NOT HAPPY with this
    # not ELEGANT
def draw_map_def_hex_v2():
    draw_map_def_hex_outer()
    draw_map_def_hex_inner()

############################################################