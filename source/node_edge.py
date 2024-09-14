import source.constants as C
from source.main_surface_class import MainSurface
from source.transforms import node_hex2pix


def draw_nodes_rect(my_surface: MainSurface, hex_size: tuple[int,int]):
    for cc in range(hex_size[0] + 1):
        for rr in range((hex_size[1] + 1) * 2):
            if rr != hex_size[1] * 2 + 1 or (cc != 0 and cc != hex_size[0]):
                draw_node(my_surface, (rr, cc))
    return


def draw_node(my_surface: MainSurface, node_hex_coords: tuple[int, int]):#, orient: bool):
    orient = get_node_orient(node_hex_coords)
    if orient:
        node_type = "left"
    else:
        node_type = "right"
    node = my_surface.s_atlas.atlas_dict["nodes"]["node_"+node_type]
    pix_coords = node_hex2pix(node_hex_coords)
    my_surface.blit2(node, pix_coords)
    return


def get_node_orient(node_hex_coords: tuple[int, int]):
    rr, cc = node_hex_coords
    ori = Ori()
    if cc % 2 == 0:  # 2, 4, 6 .. COLUMN
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


O = 'O'
I = ' '
_ = "Sea"

default_map_table_transposed = [
       [I,  _,  _,  _,  _,  I,  I]  #
    ,[I,  _,  O,  O,  O,  _,  I]    #
      ,[_,  O,  O,  O,  O,  _,  I]  #
    ,[_,  O,  O,  O,  O,  O,  _]    #
      ,[_,  O,  O,  O,  O,  _,  I]  #
    ,[I,  _,  O,  O,  O,  _,  I]    #
      ,[I,  _,  _,  _,  _,  I,  I]  #
]

map_nodes_table = []


""" DUAL CODE ???! """


def draw_default_map_nodes(my_surface: MainSurface):
    """ TOHLE HODNE NECHCI HARDCODIT, VELIKA TABULKA """

    hex_size = C.MAP_SIZE

    NODE_COL_START = 1
    NODE_COL_END = hex_size[0]
    NODE_ROW_START = 3
    NODE_ROW_END = hex_size[1] * 2

    for cc in range(NODE_COL_START, NODE_COL_END):
        nro = []
        for rr in range(NODE_ROW_START, NODE_ROW_END):

            if cc in (NODE_COL_START, NODE_COL_END-1):
                if rr in (NODE_ROW_START, NODE_ROW_START+1,
                          NODE_ROW_END-1, NODE_ROW_END-2):  # Uuu, smells like matrix! :D
                    continue

            if cc in (NODE_COL_START+1, NODE_COL_END-2):
                if rr in (NODE_ROW_START, NODE_ROW_END-1):
                    continue

            coord = (rr, cc)
            nro.append(coord)
            draw_node(my_surface, coord)
        map_nodes_table.append(nro)

    for ro in map_nodes_table: print(ro)
    return


def draw_default_map_node(my_surface: MainSurface, node_hex_coords: tuple[int, int]):
    if check_node_coordinates_default_map(node_hex_coords):
        draw_node(my_surface, node_hex_coords)
        return
    raise Exception("Error: node_Edge.py: draw_default_map_node(): Node outside of range.")


def check_node_coordinates_default_map(node_hex_coords: tuple[int, int]) -> bool:

    rr, cc = node_hex_coords

    hex_size = C.MAP_SIZE

    NODE_COL_START = 1
    NODE_COL_END = hex_size[0]
    NODE_ROW_START = 3
    NODE_ROW_END = hex_size[1] * 2

    if ( cc in range(NODE_COL_START, NODE_COL_END)
         and rr in range(NODE_ROW_START, NODE_ROW_END)
    ):
        if cc in (NODE_COL_START, NODE_COL_END - 1):
            if rr in (NODE_ROW_START, NODE_ROW_START + 1,
                      NODE_ROW_END - 1, NODE_ROW_END - 2):
                return False

        if cc in (NODE_COL_START + 1, NODE_COL_END - 2):
            if rr in (NODE_ROW_START, NODE_ROW_END - 1):
                return False

        return True

    return False
