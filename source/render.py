import pygame
from random import randint

import source.constants as C
import source.hexstack as hexstack


def get_dice_roll():
    dice1 = randint(2, 6)
    dice2 = randint(2, 6)
    roll = dice1 + dice2
    return roll


### STATIC functions (not methods) ###

def static_fun():
    # this function is static
    pass


class MySurface:
    w = 0
    h = 0

    scale = 0
    surf_board = pygame.Surface((0, 0))
    # surf_board = pygame.Surface((100,100))

    def __init__(self, wh):
        self.scale = get_scale(wh)
        self.w = wh[0] // self.scale
        self.h = wh[1] // self.scale
        self.surf_board = pygame.Surface((self.w, self.h))
        print("Info: MySurface: scale, W, H:", self.scale, self.w, self.h)

    def create(self):
        # !!! surface init
        pass

    def scale_by(self, scale=None):
        if scale is None:
            scale = self.scale
        self.surf_board = pygame.transform.scale_by(
            self.surf_board, (scale, scale)
        )
        print("Info: MySurface: \"Scaling by factor of\"", scale)

    # restructuralize place_hex and puttile and print coords function

    def put_tile(self, hextype, coords):
        file = hexstack.folder + hextype
        img = pygame.image.load(file).convert_alpha()
        # load all images just once, then just copy them (directly place)
        #    img = pygame.transform.scale_by(img, (SCA, SCA)) # haha
        # img = pygame.transform.rotate(img, -90)
        img = pygame.transform.rotate(img, 0)
        self.surf_board.blit(img, coords)
        # return surf_board
        # self.surf_board = surf_board

    def coord_print_tile(self, c, r, x, y):
        my_font = get_coords_font()
        text_surface = my_font.render(f"({c}, {r})", False, C.COORD_TILES_FONT_COLOR)
        self.surf_board.blit(text_surface, (x + C.COORD_TILE_X_OFFSET, y + C.COORD_TILE_Y_OFFSET))
        # return surf_board

    def tile_yield_overlay(self, coords: tuple, yield_number):

        ### to be removed and "cooked" in outer scope  -- for another use purposes ####
        # yield_number = mapg
        # (...)
        # (1) Co dela python 'yield' keyword?
        # (2) Mam chaos v HIERARCHII MODULU, ANEB CO IMPORTUJE CO. Lepsi reseni? Name space?
        #     -->  Budovat funkce, co se volaji z hlavniho vlakna? May not be a solution... idk..

        x, y = coords
        my_font = get_yield_font()
        text_surface = my_font.render(str(yield_number), False, C.TILE_YIELD_OVERLAY_FONT_COLOR)  # .toString() ??
        self.surf_board.blit(text_surface, (x + C.TILE_YIELD_OVERLAY_X_OFFSET, y + C.TILE_YIELD_OVERLAY_Y_OFFSET))

    def place_hex(self, hextype, c, r):
        # uz si nepamatuji, co melo byt con,
        # connect urcite ne, conformation...nevim
        x_off, y_off = 200, 5
        hor_con, ver_con = 10, 6
        do_shift_first_column_down = 1  # bool 0 or 1
        if c % 2 == do_shift_first_column_down:
            x = x_off + c * (C.TILE_SIZE - hor_con)
            y = y_off + r * (C.TILE_SIZE - ver_con)
            self.put_tile(hextype, (x, y))
            # WHAAT? UNEXPECTED ARGUMENT??
            # Does it mean, that object does not save me anything?!
            # self.coord_print_tile(c, r, x, y)
            # self.tile_yield_overlay((x,y), get_dice_roll())  # Default par

            ### FUNCTION ASSEMBLY
            # put together beforehands, whould all should happen while placement

        else:
            x = x_off + c * (C.TILE_SIZE - hor_con)
            y = y_off + r * (C.TILE_SIZE - ver_con) + C.TILE_SIZE // 2 - 3  # magic number 3 ?!
            self.put_tile(hextype, (x, y))
            # self.coord_print_tile(c, r, x, y)
            # self.tile_yield_overlay((x, y), get_dice_roll())  # Default par
        # return surf_board


    ### DUPLICIT FUNCTION !!!
    def place_yield(self, coords, yield_number):

        c, r = coords

        x_off, y_off = 200, 5
        hor_con, ver_con = 10, 6
        do_shift_first_column_down = 1  # bool 0 or 1
        if c % 2 == do_shift_first_column_down:
            x = x_off + c * (C.TILE_SIZE - hor_con)
            y = y_off + r * (C.TILE_SIZE - ver_con)
            # self.put_tile(hextype, (x, y))
            # self.coord_print_tile(c, r, x, y)
            self.tile_yield_overlay((x, y), get_dice_roll())
        else:
            x = x_off + c * (C.TILE_SIZE - hor_con)
            y = y_off + r * (C.TILE_SIZE - ver_con) + C.TILE_SIZE // 2 - 3  # magic number 3 ?!
            # self.put_tile(hextype, (x, y))
            # self.coord_print_tile(c, r, x, y)
            self.tile_yield_overlay((x, y), get_dice_roll())

################################################################
###############################################################

def screen_init():
    pygame.font.init()
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    W, H = screen.get_size()
    print(f"Screen size: {W} x {H}")
    return screen
#################################################################


def get_scale(dims):
    # w, h = dims
    """
    * HANDLE FULLSCREEN LOGIC,
    * calculate 'SCA' scalar accordingly to user's display
    """
    mindim = min(dims)
    scale = mindim // C.TILES_RANGE // C.TILE_SIZE  # round_down  # capitals?
    print("scale:", scale)
    # test! vary! check tiling!
    scale = 1 if scale == 0 else scale
    return scale

"""
def surf_init(W, H, SCALE):
    
    surf_board = pygame.Surface((W // SCALE, H // SCALE))
    print(surf_board.get_size())
    return surf_board
"""


def get_coords_font():
    return pygame.font.SysFont('Comic Sans MS', C.COORD_TILES_FONT_SIZE)

def get_yield_font():
    return pygame.font.SysFont('Comic Sans MS', C.TILE_YIELD_OVERLAY_FONT_SIZE)


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