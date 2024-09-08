import pygame
from random import randint

import source.constants as C
import source.pieces as pieces
from source.tiletype import TileType
from source.fonttype import FontType


# ----- NOTES ---------------------------------------------------------

"""
*
*
*
"""

# ----- BODY ----------------------------------------------------------


def get_dice_roll():
    dice1 = randint(2, 6)
    dice2 = randint(2, 6)
    roll = dice1 + dice2
    return roll


def static_fun():
    # this function is static
    # it is not a method
    pass


class MainSurface:  # MySurface --> RENAME? GameSurface? MainSurface? ScreenSurface??

    tile_size = 0
    w = 0
    h = 0
    scale = 0
    surf_board = pygame.Surface((0, 0))

    def __init__(self, wh):
        # HArdcoded
        self.tile_size = get_tile_size(pieces.folder_cakes+"Field"+".png")
        #
        self.scale = get_scale(wh, self.tile_size)
        self.w = wh[0] // self.scale
        self.h = wh[1] // self.scale
        self.surf_board = pygame.Surface((self.w, self.h))
        print("Info: MainSurface: scale, W, H:", self.scale, self.w, self.h)

    def create(self):
        # !!! surface init
        pass

    def scale_by(self, scale=None):
        if scale is None:
            scale = self.scale
        self.surf_board = pygame.transform.scale_by(
            self.surf_board, (scale, scale)
        )
        print("Info: MainSurface: \"Scaling by factor of\"", scale)

    def put_tile(self, file_path, coords):
        img = pygame.image.load(file_path).convert_alpha()
        # img = pygame.transform.rotate(img, 0)
        self.surf_board.blit(img, coords)

    def coord_print_tile(self, c, r, x, y):  # Coords CONDENSATION !
        my_font = get_coords_font()
        text_surface = my_font.render(f"({c}, {r})", False, C.CoordTiles.FONT_COLOR)
        dest_coords = (x + C.CoordTiles.X_OFFSET, y + C.CoordTiles.Y_OFFSET)
        self.surf_board.blit(text_surface, dest_coords)

    def tile_yield_overlay(self, coords: tuple, yield_number):
        x, y = coords
        my_font = get_yield_font()
        text_surface = my_font.render(str(yield_number), False, C.TileYield.OVERLAY_FONT_COLOR)
        dest_coords = (x + C.TileYield.OVERLAY_X_OFFSET, y + C.TileYield.OVERLAY_Y_OFFSET)
        self.surf_board.blit(text_surface, dest_coords)

    def place_hex(self, tile_type: TileType, hex_coords):
        c, r = hex_coords
        plate, cake = tile_type.tuple
        plate = pieces.folder_plates + plate
        cake = pieces.folder_cakes + cake
        x_off, y_off = 200, 5
        # uz si nepamatuji, co melo byt con,
        # connect urcite ne, conformation...nevim
        hor_con, ver_con = 10, 6
        do_shift_first_column_down = 1  # bool 0 or 1
        if c % 2 == do_shift_first_column_down:
            x = x_off + c * (self.tile_size - hor_con)
            y = y_off + r * (self.tile_size - ver_con)
            self.put_tile(plate, (x, y))
            self.put_tile(cake, (x, y))
            # self.coord_print_tile(c, r, x, y)
            # self.tile_yield_overlay((x,y), get_dice_roll())  # Default par

            ### FUNCTION ASSEMBLY
            # put together beforehands, whould all should happen while placement

        else:
            x = x_off + c * (self.tile_size - hor_con)
            y = y_off + r * (self.tile_size - ver_con) + self.tile_size // 2 - C.PLACE_HEX_VERTICAL_OFFSET
            self.put_tile(plate, (x, y))
            self.put_tile(cake, (x, y))
            # self.coord_print_tile(c, r, x, y)
            # self.tile_yield_overlay((x, y), get_dice_roll())  # Default par
        # return surf_board


    ### DUPLICIT FUNCTION !!!
    def place_yield(self, hex_coords, yield_number):

        c, r = hex_coords

        x_off, y_off = 200, 5
        hor_con, ver_con = 10, 6
        do_shift_first_column_down = 1  # bool 0 or 1
        if c % 2 == do_shift_first_column_down:
            x = x_off + c * (self.tile_size - hor_con)
            y = y_off + r * (self.tile_size - ver_con)
            # self.put_tile(hextype, (x, y))
            # self.coord_print_tile(c, r, x, y)
            self.tile_yield_overlay((x, y), yield_number)
        else:
            x = x_off + c * (self.tile_size - hor_con)
            y = y_off + r * (self.tile_size - ver_con) + self.tile_size // 2 - 3  # magic number 3 ?!
            # self.put_tile(hextype, (x, y))
            # self.coord_print_tile(c, r, x, y)
            self.tile_yield_overlay((x, y), yield_number)

    def put_text(self, pix_coords: tuple[int, int], text: str,
                 font_size: int = 32, font_color: tuple[int, int, int] = (180, 180, 100)):
        # Default argument into constants file
        my_font = pygame.font.SysFont('Comic Sans MS', font_size)
        text_surface = my_font.render(text, False, font_color)
        self.surf_board.blit(text_surface, pix_coords)
        return

################################################################
###############################################################


def screen_init():
    pygame.font.init()
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    W, H = screen.get_size()
    print(f"Screen size: {W} x {H}")
    return screen
#################################################################


def get_tile_size(template_tile_file_path):
    img = pygame.image.load(template_tile_file_path).convert_alpha()
    a,b = img.get_size()
    assert a == b
    return a


def get_scale(dimensions, tile_size, board_size=C.TILES_RANGE):
    """ FULLSCREEN: Calculates scale to adjust user's display. """
    scale = min(dimensions) // board_size // tile_size
    """ Rounded down by integer division. """
    scale = 1 if scale == 0 else scale
    print("Got scale:", scale)
    return scale


"""
def surf_init(W, H, SCALE):
    
    surf_board = pygame.Surface((W // SCALE, H // SCALE))
    print(surf_board.get_size())
    return surf_board
"""


def get_coords_font():
    return pygame.font.SysFont('Comic Sans MS', C.CoordTiles.FONT_SIZE)


def get_yield_font():
    return pygame.font.SysFont('Comic Sans MS', C.TileYield.OVERLAY_FONT_SIZE)


############################################


'''
def window_postinit(screen, surf_board):
    """ ---> This is the correct approach, but need to downscale bar.png
    # bottom_bar
    img = pygame.image.load("textures/gui/bar.png").convert_alpha()
    w, h = img.get_size()
    surf_board.blit(img, ((1920-w)//2, 1080-h))
    """

    surf_board = pygame.transform.scale_by(surf_board, (SCALE, SCALE))
    screen.blit(surf_board, (0, 0))

    """ this should go away """
    img = pygame.image.load("textures/gui/bar.png").convert_alpha()
    w, h = img.get_size()
    screen.blit(img, ((1920 - w) // 2, 1080 - h))

    pygame.display.flip()
'''
