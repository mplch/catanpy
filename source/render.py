import pygame
import source.constants as C

class surface():
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def create(self):
        pass



###############################################################
def screen_init():
    pygame.font.init()
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    W, H = screen.get_size()
    print(f"Screen size: {W} x {H}")
    return screen#, surf_board  # objekty??? +metody
#################################################################

def surf_init(dims):
    W, H = dims
    """
    * HANDLE FULLSCREEN LOGIC,
    * calculate 'SCA' scalar accordingly to user's display
    """
    mindim = min(W, H)
    SCALE = mindim / C.TILES_RANGE // C.TILE_SIZE  # round_down  # capitals?
    print("scale:", SCALE)
    # test! vary! check tiling!
    surf_board = pygame.Surface((W // SCALE, H // SCALE))
    print(surf_board.get_size())
    return surf_board

def get_font():
    return pygame.font.SysFont('Comic Sans MS', C.COORD_TILES_FONT_SIZE)


############################################
def window_postinit(screen, surf_board):
    """ ---> This is the correct approach, but need to downscale bar.png
    # bottom_bar
    img = pygame.image.load("textures/gui/bar.png").convert_alpha()
    w, h = img.get_size()
    surf_board.blit(img, ((1920-w)//2, 1080-h))
    """

    surf_board = pygame.transform.scale_by(surf_board, (C.SCALE, C.SCALE))
    screen.blit(surf_board, (0, 0))

    """ this should go away """
    img = pygame.image.load("textures/gui/bar.png").convert_alpha()
    w, h = img.get_size()
    screen.blit(img, ((1920 - w) // 2, 1080 - h))

    pygame.display.flip()