from pygame.transform import rotate

from source.main_surface_class import MainSurface
from source.transforms import node_hex2pix


def draw_nodes(my_surface: MainSurface, hex_size: tuple[int,int]):

    # node = my_surface.s_atlas.atlas_dict["nodes"]["node_right"]
    ori = Ori()  # Parantheses NEEDED here
    
    for c in range(hex_size[0] + 1):
        for r in range((hex_size[1] + 1) * 2):
            draw_node(my_surface, (r, c), ori.a)
            ori.flip()
        ori.flip()
  
    return


def draw_node(my_surface: MainSurface, hex_coords: tuple[int, int], orient: bool):

    if orient:
        node_type = "left"
    else:
        node_type = "right"

    # orient = get_node_orient(hex_coords)
    # no param orient would be needed

    node = my_surface.s_atlas.atlas_dict["nodes"]["node_"+node_type]
    pix_coords = node_hex2pix(hex_coords)
    my_surface.blit2(node, pix_coords)

    return

def get_node_orient(hex_coords: tuple[int, int]):
    """ HOW TO DETERMINE THIS?? """
    pass


class Ori:
    a: bool = False

    def flip(self):
        if self.a:
            self.a = False
        else:
            self.a = True
