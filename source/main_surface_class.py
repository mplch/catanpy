import pygame
from random import randint

import source.constants as C
import source.transforms as transforms
from source.tiletype import TileType
from source.fonttype import FontType
from source.sprites import Atlas
from source.transforms import HexCoord, PixCoord

CAKES = "cakes"
PLATES = "plates"

# ----- NOTES ---------------------------------------------------------

"""
(*) main_surface_class.py:
put_tile():
    * Image CACHING
    * Load all images just once, then just copy them
get_scale():
    * Test! vary! check tiling!
* RESTRUCTURE place_hex and put_tile and print_coords function
* Use of STATIC functions instead of methods
* TEMPLATE tiles ponechat ciste jako ilustrativni
  --> assertovat spravnost kazde krajiny (jak?
* Function SEPARATION, consider more FILES
* Argument order CONSISTENCY, e.g. coords
* Infer 'tile_size' where needed automatically from class?
"""

# ----- BODY ----------------------------------------------------------


# def get_dice_roll():
#     dice1 = randint(2, 6)
#     dice2 = randint(2, 6)
#     roll = dice1 + dice2
#     return roll


def static_fun():
    # this function is static
    # it is not a method
    pass


class MainSurface:  # MySurface --> RENAME? GameSurface? main_surface? ScreenSurface??

    tile_size = 0
    w = 0
    h = 0
    scale = 0
    surf_board = pygame.Surface((0, 0))
    s_atlas = None  # just do differ from atlas instance in run.py
    map_size = (0, 0)

    def __init__(self, screen_dimensions: tuple[int,int], map_size: tuple[int,int]):
        # Hardcoded
        # self.tile_size = get_tile_size(pieces.folder_cakes+"Field"+".png")
        #
        self.tile_size = C.TILE_SIZE
        self.map_size = map_size

        self.scale = get_scale(screen_dimensions, self.tile_size, self.map_size)
        self.w = screen_dimensions[0] // self.scale
        self.h = screen_dimensions[1] // self.scale
        self.surf_board = pygame.Surface((self.w, self.h))
        print("Info: main_surface: scale, W, H:", self.scale, self.w, self.h)

    def set_atlas(self, s_atlas: Atlas):
        self.s_atlas = s_atlas

    # def set_map_size(self, n, m):


    def create(self):
        # !!! surface init
        pass

    def scale_by(self, scale=None):
        if scale is None:
            scale = self.scale
        self.surf_board = pygame.transform.scale_by(
            self.surf_board, (scale, scale)
        )
        print("Info: main_surface: \"Scaling by factor of\"", scale)

    def blit_pix(self, image: pygame.Surface, pix_coord: PixCoord):  # image type?
        # Is this function necessary?
        # Only to extract (x, y) from PixCoord.
        # And to shorten of '.surf_board.'.
        self.surf_board.blit(image, pix_coord.xy)

    def place_hex(self, tile_type: TileType, hex_coord: HexCoord):
        """ Docstring """
        """ Should tile type's plate & cake always be the same? """
        plate, cake = tile_type.tuple
        # Convert name into image:
        plate = self.s_atlas.a_dict[PLATES][plate]
        cake = self.s_atlas.a_dict[CAKES][cake]
        self.blit_pix(plate, transforms.tile_hex2pix(hex_coord, self.tile_size))
        self.blit_pix(cake, transforms.tile_hex2pix(hex_coord, self.tile_size))

    """ UNIFY the below ones  repeating code! """

    def put_text(self, pix_coord: PixCoord, text: str,
                 font_size: int = 32, font_color: tuple[int, int, int] = (180, 180, 100)):
        """ Docstring """
        """ Merge place yield and place coord into put_text """
        my_font = pygame.font.SysFont(C.DEFAULT_FONT, font_size)
        text_surface = my_font.render(text, False, font_color)
        self.blit_pix(text_surface, pix_coord)

    def put_yield(self, hex_coord: HexCoord, yield_number):
        dest_pix_coord = transforms.tile_hex2pix(hex_coord, self.tile_size)
        my_font = get_font(C.TileYieldOverlay.FONT_SIZE)
        text_surface = my_font.render(str(yield_number), False, C.TileYieldOverlay.FONT_COLOR)
        xy_offset = PixCoord(C.TileYieldOverlay.X_OFFSET, C.TileYieldOverlay.Y_OFFSET)
        dest_pix_coord.add(xy_offset)
        self.blit_pix(text_surface, dest_pix_coord)

    def put_coord(self, hex_coord: HexCoord):
        r, c = hex_coord.rc
        my_font = get_font(C.TileCoordOverlay.FONT_SIZE)
        text_surface = my_font.render(f"({r}, {c})", False, C.TileCoordOverlay.FONT_COLOR)
        dest_pix_coord = transforms.tile_hex2pix(hex_coord, self.tile_size)
        xy_offset = PixCoord(C.TileCoordOverlay.X_OFFSET, C.TileCoordOverlay.Y_OFFSET)
        dest_pix_coord.add(xy_offset)
        self.blit_pix(text_surface, dest_pix_coord)

    def put_node_coord(self, node_hex_coord: HexCoord):
        overlay = C.NodeCoordOverlay  # ()??
        rr, cc = node_hex_coord.rc
        my_font = get_font(overlay.FONT_SIZE)
        text_surface = my_font.render(f"({rr}, {cc})", False, overlay.FONT_COLOR)
        dest_pix_coord = transforms.node_hex2pix(node_hex_coord)
        xy_offset = PixCoord(overlay.X_OFFSET, overlay.Y_OFFSET)
        dest_pix_coord.add(xy_offset)
        self.blit_pix(text_surface, dest_pix_coord)

# ---------------------------------------------------------------------


def screen_init():
    pygame.font.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    W, H = screen.get_size()
    print(f"Screen size: {W} x {H}")
    return screen


def get_tile_size(template_tile_file_path):
    img = pygame.image.load(template_tile_file_path).convert_alpha()
    a,b = img.get_size()
    assert a == b
    return a


def get_scale(screen_dimensions: tuple[int,int],
              tile_size_pix: int,
              board_size_hex: tuple[int, int]):
    """ Docstring """
    """ FULLSCREEN: Calculates scale to adjust user's display. """
    w, h = screen_dimensions
    m, n = board_size_hex
    x = m * tile_size_pix
    y = n * tile_size_pix
    x_scale = w // x
    y_scale = h // y
    scale = min(x_scale, y_scale)
    """ Rounded down by integer division. """
    scale = 1 if scale == 0 else scale
    print("Got scale:", scale)
    return scale


def get_font(font_size: int, font_name=C.DEFAULT_FONT):
    # Also just wrap / RENAME function, but I'm perfectly fine with that.
    return pygame.font.SysFont(font_name, font_size)


# ---------------------------------------------------------------------

''' ######     GUI BOTTOM BAR    ######

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
