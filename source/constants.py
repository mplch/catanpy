# from enum import Enum

# TILE_SIZE = 46  # shouldn't be needed
TILES_RANGE = 7

PLACE_HEX_MAGIC = 3  # magic number 3 ?!

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


