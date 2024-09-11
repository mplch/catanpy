HEX_MAP_SIZE = 7

TILE_SIZE = 46  # DYNAMIC ... BUT SHOULD BE??
                # Musel bych udelat dynamicke i ostatni konstanty
                # NO LONGER DYNAMIC
STRIP_HEIGHT = 6
HEX_HEIGHT = TILE_SIZE - STRIP_HEIGHT
HEX_HORI_EDGE_X = 26
HEX_RISING_EDGE_X = 10
HEX_RISING_EDGE_Y = 20

HEX_OVERLAP_X = 10 #8
HEX_OVERLAP_Y = 6 #4
REMOVE = 0 #1


DO_SHIFT_FIRST_COLUMN_DOWN = False

""" Map offset in pixels (before scaling up) """
MAP_OFF_PIX_X = 200  # need to make DYNAMIC
MAP_OFF_PIX_Y = 5
MAP_OFF_PIX_X = 8
MAP_OFF_PIX_Y = 8


YIELDS_DO_RANDOM_SHUFFLE = True

DEFAULT_IMAGE_SUFFIX = ".png"

DEFAULT_FONT = "Comic Sans MS"


# class CoordTiles(Enum):
class CoordTiles:
    FONT_SIZE: int = 18
    FONT_COLOR: tuple[int,int,int] = (0, 0, 0)
    X_OFFSET: int = 9
    Y_OFFSET: int = 20


class TileYield:
    OVERLAY_FONT_SIZE = 24  # NESIKOVNY NAZEV
    OVERLAY_FONT_COLOR = (100, 0, 0)
    OVERLAY_X_OFFSET = 14
    OVERLAY_Y_OFFSET = 20


