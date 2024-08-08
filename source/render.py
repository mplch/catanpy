import pygame
import source.constants as C


class MySurface:
    w = 0
    h = 0
    scale = 0
    surf_board = None

    def __init__(self, w, h):
        self.scale = get_scale((w, h))
        self.w = w // self.scale
        self.h = h // self.scale
        self.surf_board = pygame.Surface((self.w, self.h))
        print("Info: MySurface: scale, W, H:", self.scale, w, h)

    def create(self):
        # !!! surface init
        pass

    def scaleup(self):
        self.surf_board = pygame.transform.scale_by(
            self.surf_board, (self.scale, self.scale)
        )
        print("Info: MySurface: \"Scaling up.\"")

    def place_hex_2(self, surf_board, hextype, c, r):
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
    scale = mindim / C.TILES_RANGE // C.TILE_SIZE  # round_down  # capitals?
    print("scale:", scale)
    # test! vary! check tiling!
    return scale

"""
def surf_init(W, H, SCALE):
    
    surf_board = pygame.Surface((W // SCALE, H // SCALE))
    print(surf_board.get_size())
    return surf_board
"""


def get_font():
    return pygame.font.SysFont('Comic Sans MS', C.COORD_TILES_FONT_SIZE)


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