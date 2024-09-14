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


def draw_node(my_surface: MainSurface, node_hex_coords: tuple[int, int]):#, orient: bool):
    node = my_surface.s_atlas.atlas_dict["nodes"]["village_red"]
    pix_coords = node_hex2pix(node_hex_coords)
    my_surface.blit2(node, pix_coords)
    return


def get_valid_nodes_list():

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


def draw_inner_nodes(my_surface: MainSurface):
    for node_hex_coords in get_valid_nodes_list():
        cc, rr = node_hex_coords
        # cc, rr = rr, cc
        node_hex_coords = cc, rr
        draw_node(my_surface, node_hex_coords)

# ---------------------------------------------------------------------

def init_default_node_table():

    node_table = []

    # print("rr", (SHADOW_NODE_ROW_START, SHADOW_NODE_ROW_END))
    # print("cc", (SHADOW_NODE_COL_START, SHADOW_NODE_COL_END))

    for rr in range(SHADOW_NODE_ROW_START, SHADOW_NODE_ROW_END):
        new_col = []
        for cc in range(SHADOW_NODE_COL_START, SHADOW_NODE_COL_END):
            new_col.append(' ')
        node_table.append(new_col)
    return node_table


def fill_node_table(table: list[list[str]], node_list: list[tuple[int,int]]):
    for rr, cc in node_list:
        table[rr][cc] = OCCUPIED
    return table


def check_node(hex_coord: tuple[int, int]) -> bool:
    # TODO
    return False

