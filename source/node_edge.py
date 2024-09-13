from pygame.transform import rotate

from source.main_surface_class import MainSurface
from source.transforms import node_hex2pix


def draw_nodes(my_surface: MainSurface, hex_size: tuple[int,int]):
    """ Rozpada se pri shift column, ale to neni nutne resit,
    protoze ve vysledku se vykreslovani nod bude resit stejne jinak. """
    for c in range(hex_size[0] + 1):
        for rr in range((hex_size[1] + 1) * 2):
            # if c == 0 or c == hex_size[0] and rr == hex_size[1]: continue
            if (rr == hex_size[1] * 2 + 1
                    and (c == 0 or c == hex_size[0])):
                continue
            draw_node(my_surface, (rr, c))
    return


def draw_node(my_surface: MainSurface, hex_coords: tuple[int, int]):#, orient: bool):
    orient = get_node_orient(hex_coords)
    if orient:
        node_type = "left"
    else:
        node_type = "right"
    node = my_surface.s_atlas.atlas_dict["nodes"]["node_"+node_type]
    pix_coords = node_hex2pix(hex_coords)
    my_surface.blit2(node, pix_coords)
    return


def get_node_orient(hex_coords: tuple[int, int]):
    rr, c = hex_coords
    ori = Ori()
    if c % 2 == 0:  # 2, 4, 6 .. COLUMN
        ori.flip()
    if rr % 2 == 1:  # 2, 4, 6 .. ROW
        ori.flip()
    return ori.a


class Ori:
    a: bool = True

    def flip(self):
        if self.a:
            self.a = False
        else:
            self.a = True
