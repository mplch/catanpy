# from enum import Enum

# TILE_SIZE = 46  # shouldn't be needed
TILES_RANGE = 7

TO_BE_REMOVED = 3  # !!

DO_SHIFT_FIRST_COLUMN_DOWN = 1  # bool 0 or 1

STRIP_HEIGHT = 6  # I believe I am correct.

""" Map offset in pixels (before scaling up) """
MAP_OFF_PIX_X = 200
MAP_OFF_PIX_Y = 5

""" What was the MEANING of the name?! """
HOR_CON = 10
VER_CON = 6

YIELDS_DO_RANDOM_SHUFFLE = True


DEFAULT_IMAGE_SUFFIX = ".png"


# class CoordTiles(Enum):
class CoordTiles:
    FONT_SIZE: int = 18
    FONT_COLOR: tuple[int,int,int] = (0, 0, 0)
    X_OFFSET: int = 9
    Y_OFFSET: int = 20


class TileYield:
    OVERLAY_FONT_SIZE = 24
    OVERLAY_FONT_COLOR = (100, 0, 0)
    OVERLAY_X_OFFSET = 14
    OVERLAY_Y_OFFSET = 20


