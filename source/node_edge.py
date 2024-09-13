from pygame.transform import rotate

# from source.constants import TILE_SIZE
from source.main_surface_class import MainSurface
import source.constants as C
from source.transforms import node_hex2pix


def draw_nodes(my_surface: MainSurface, r_c: tuple[int,int]):
    """ Is independent of first map colum shift. Its just shift. :)"""
    node = my_surface.s_atlas.atlas_dict["nodes"]["node_right"]
    # node = rotate(node, 180)  # IF SHIFT 1ST COL


    for c in range(r_c[0] + 1):
        for r in range((r_c[1] + 1) * 2):
            node_pix_coords = node_hex2pix((r, c))
            my_surface.blit2(node, node_pix_coords)
            node = rotate(node, 180)  # NAH!
        node = rotate(node, 180)  # NAH!
  
    return


def draw_node(my_surface: MainSurface, hex_coords: tuple[int, int]):
    """ HOW TO DETERMINE THIS?? """
    node_type = "right"
    node = my_surface.s_atlas.atlas_dict["nodes"]["node_"+node_type]
    pix_coords = node_hex2pix(hex_coords)
    my_surface.blit2(node, pix_coords)

    return
