import source.constants as C
from source.main_surface_class import MainSurface
from source.mapgen_v2 import OCCUPIED
from source.transforms import node_hex2pix, transpose


SHADOW_NODE_COL_START = 0
SHADOW_NODE_COL_END   = C.MAP_SIZE[0] + 1
SHADOW_NODE_ROW_START = 0
SHADOW_NODE_ROW_END   =(C.MAP_SIZE[1] + 1) * 2

VALID_NODE_COL_START = SHADOW_NODE_COL_START + 1
VALID_NODE_COL_END   = SHADOW_NODE_COL_END   - 1
VALID_NODE_ROW_START = SHADOW_NODE_ROW_START + 3
VALID_NODE_ROW_END   = SHADOW_NODE_ROW_END   - 2


def draw_nodes_rect(my_surface: MainSurface, map_size: tuple[int,int]):
    for cc in range(map_size[0] + 1):
        for rr in range((map_size[1] + 1) * 2):
            if rr != map_size[1] * 2 + 1 or (cc != 0 and cc != map_size[0]):
                draw_node_old(my_surface, (rr, cc))
    return


def draw_node_old(my_surface: MainSurface, node_hex_coords: tuple[int, int]):#, orient: bool):
    orient = get_node_orient(node_hex_coords)
    if orient:
        node_type = "left"
    else:
        node_type = "right"
    node = my_surface.s_atlas.atlas_dict["nodes"]["node_"+node_type]
    pix_coords = node_hex2pix(node_hex_coords)
    my_surface.blit2(node, pix_coords)
    return


def draw_node_new(my_surface: MainSurface, node_hex_coords: tuple[int, int]):#, orient: bool):
    node = my_surface.s_atlas.atlas_dict["nodes"]["village_red"]
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


""" DUAL CODE ???! """

def draw_inner_nodes(my_surface: MainSurface):
    for node_hex_coords in get_default_map_nodes_list():
        cc, rr = node_hex_coords
        # cc, rr = rr, cc
        node_hex_coords = cc, rr
        draw_node_new(my_surface, node_hex_coords)

def get_default_map_nodes_list():

    my_map_nodes_list = []

    for rr in range(VALID_NODE_ROW_START, VALID_NODE_ROW_END):
        for cc in range(VALID_NODE_COL_START, VALID_NODE_COL_END):

            if cc in (VALID_NODE_COL_START, VALID_NODE_COL_END-1):
                if rr in (VALID_NODE_ROW_START, VALID_NODE_ROW_START+1,
                          VALID_NODE_ROW_END-1, VALID_NODE_ROW_END-2):  # Uuu, smells like matrix! :D
                    continue

            if cc in (VALID_NODE_COL_START+1, VALID_NODE_COL_END-2):
                if rr in (VALID_NODE_ROW_START, VALID_NODE_ROW_END-1):
                    continue

            my_map_nodes_list.append( (rr, cc) )

    return my_map_nodes_list


def init_default_node_table():

    node_table = []

    # print("rr", (SHADOW_NODE_ROW_START, SHADOW_NODE_ROW_END))
    # print("cc", (SHADOW_NODE_COL_START, SHADOW_NODE_COL_END))

    for rr in range(SHADOW_NODE_ROW_START, SHADOW_NODE_ROW_END):
        ncol = []
        for cc in range(SHADOW_NODE_COL_START, SHADOW_NODE_COL_END):
            ncol.append(' ')
        node_table.append(ncol)
    return node_table


def fill_node_table(table: list[list[str]], node_list: list[tuple[int,int]]):
    for rr, cc in node_list:
        table[rr][cc] = OCCUPIED
    return table


def draw_default_map_node(my_surface: MainSurface, node_hex_coords: tuple[int, int]):
    if check_node:
        draw_node_old(my_surface, node_hex_coords)
        return
    raise Exception("Error: node_Edge.py: draw_default_map_node(): Node outside of range.")


# def check_node_coordinates_default_map(node_hex_coords: tuple[int, int]) -> bool:
# 
#     rr, cc = node_hex_coords
# 
#     VALID_NODE_COL_START = 1
#     VALID_NODE_COL_END = C.MAP_SIZE[0]
#     VALID_NODE_ROW_START = 3
#     VALID_NODE_ROW_END = C.MAP_SIZE[1] * 2
# 
#     if ( cc in range(VALID_NODE_COL_START, VALID_NODE_COL_END)
#          and rr in range(VALID_NODE_ROW_START, VALID_NODE_ROW_END)
#     ):
#         if cc in (VALID_NODE_COL_START, VALID_NODE_COL_END - 1):
#             if rr in (VALID_NODE_ROW_START, VALID_NODE_ROW_START + 1,
#                       VALID_NODE_ROW_END - 1, VALID_NODE_ROW_END - 2):
#                 return False
# 
#         if cc in (VALID_NODE_COL_START + 1, VALID_NODE_COL_END - 2):
#             if rr in (VALID_NODE_ROW_START, VALID_NODE_ROW_END - 1):
#                 return False
# 
#         return True
# 
#     return False


# ---------------------------------------------------------------------

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

map_nodes_list = get_default_map_nodes_list()
for occ in map_nodes_list: print(occ)

map_nodes_table = init_default_node_table()  # Class ??
map_nodes_table = fill_node_table(map_nodes_table, map_nodes_list)

for col in map_nodes_table: print(col)




