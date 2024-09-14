import source.constants as C
from source.main_surface_class import MainSurface
# from source.mapgen_v2 import OCCUPIED
from source.transforms import node_hex2pix, transpose
from source.transforms import HexCoord

# ---------------------------------------------------------------------

FREE_NODE = '_'
ERROR_RANGE = 99

SHADOW_NODE_COL_START = 0
SHADOW_NODE_COL_END   = C.MAP_SIZE[0] + 1
SHADOW_NODE_ROW_START = 0
SHADOW_NODE_ROW_END   =(C.MAP_SIZE[1] + 1) * 2

VALID_NODE_COL_START = SHADOW_NODE_COL_START + 1
VALID_NODE_COL_END   = SHADOW_NODE_COL_END   - 1
VALID_NODE_ROW_START = SHADOW_NODE_ROW_START + 3
VALID_NODE_ROW_END   = SHADOW_NODE_ROW_END   - 2

# ---------------------------------------------------------------------

class NodeTable:

    # table = list(list(" "))
    table: list[list[str]]
    w = SHADOW_NODE_COL_END
    h = SHADOW_NODE_ROW_END

    def __init__(self, node_list: list[tuple[int,int]]):
        self.init_default()
        self.fill_from_list(node_list)

    def __str__(self):
        string = ""
        for row in self.table:
            string += str(row)
            string += '\n'
        return string

    def init_default(self):
        node_table = []
        for rr in range(SHADOW_NODE_ROW_START, SHADOW_NODE_ROW_END):
            new_col = []
            for cc in range(SHADOW_NODE_COL_START, SHADOW_NODE_COL_END):
                new_col.append(' ')
            node_table.append(new_col)
        self.table = node_table

    def fill_from_list(self, node_list: list[tuple[int, int]]):
        for rr, cc in node_list:
            # self.table[rr][cc] = OCCUPIED
            self.table[rr][cc] = FREE_NODE


    # def check_node_in_table(self, hex_coord: HexCoord) -> bool:
    #     return hex_coord.c < self.w and hex_coord.r < self.h
    #
    # def check_node_on_land(self, hex_coord: HexCoord) -> bool:
    #     return self.get_node(hex_coord) != ' '
    #
    # def check_node_is_free(self, hex_coord: HexCoord) -> bool:
    #     return self.get_node(hex_coord) == FREE_NODE
    #
    # def check_node_complete(self, hex_coord: HexCoord) -> bool:
    #     if self.check_node_in_table(hex_coord):
    #         if self.check_node_on_land(hex_coord):
    #             return self.check_node_is_free(hex_coord)


    def check_node_in_table(self, hex_coord: HexCoord) -> bool:
        return hex_coord.c < self.w and hex_coord.r < self.h

    def check_node_on_land(self, hex_coord: HexCoord) -> bool:
        ### WILL WORK w/o .rc ??? ###
        if self.check_node_in_table(hex_coord):
            return self.get_node(hex_coord) != ' '
        return False

    def check_node_is_free(self, hex_coord: HexCoord) -> bool:
        ### WILL WORK w/o .rc ??? ###
        if self.check_node_on_land(hex_coord):
            return self.get_node(hex_coord) == FREE_NODE
        return False


    def get_node(self, hex_coord: HexCoord):
        if self.check_node_in_table(hex_coord):
            return self.table[hex_coord.r][hex_coord.c]
        print("Error: node_v2.py: get_node(): Accessing node outside of NodeTable range.")
        return ERROR_RANGE

    def add_node(self, hex_coord: HexCoord, node_type: str):
        ret = self.get_node(hex_coord)
        if ret == ERROR_RANGE:
            print("Error: node_v2.py: add_node(): Node placement outside of TABLE range.")
        elif ret == ' ':
            print("Error: node_v2.py: add_node(): Node placement outside of LAND range.")
        elif ret == FREE_NODE:
            # numpy definitely would help
            self.table[hex_coord.r][hex_coord.c] = node_type
            print(f"Info: node_v2.py: add_node(): Added none of type: {node_type}, at: {hex_coord}.")
        else:
            print("Error: node_v2.py: add_node(): ELSE ERROR - likely occupied.")
    #     self.node_overlay_redraw()
    #
    # def node_overlay_redraw(self):
    #     draw_node_from_table(self.table)

# ---------------------------------------------------------------------

def draw_node_table(my_surface: MainSurface, my_node_table: NodeTable):
    for r, row in enumerate(my_node_table.table):
        for c, node in enumerate(row):
            if node == 'r':
                draw_node_type(my_surface, (r, c), "village_red")
            if node == 'R':
                draw_node_type(my_surface, (r, c), "city_red")

    return

# ---------------------------------------------------------------------

def draw_node_type(my_surface: MainSurface,
                   node_hex_coord: tuple[int, int],
                   node_type="default"
                   ):
    node = my_surface.s_atlas.atlas_dict["nodes"][node_type]
    pix_coords = node_hex2pix(node_hex_coord)
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
    for node_hex_coord in get_valid_nodes_list():
        draw_node_type(my_surface, node_hex_coord)
    return

# ---------------------------------------------------------------------

global_node_table = [
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', 'r', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', 'R', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', 'r', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
]

global_node_table = [
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', '_', '_', ' ', ' ', ' '],
[' ', ' ', 'r', '_', '_', '_', ' ', ' '],
[' ', '_', '_', '_', '_', '_', '_', ' '],
[' ', '_', '_', 'R', '_', '_', '_', ' '],
[' ', '_', '_', '_', '_', '_', '_', ' '],
[' ', '_', '_', '_', '_', '_', '_', ' '],
[' ', '_', '_', '_', 'r', '_', '_', ' '],
[' ', '_', '_', '_', '_', '_', '_', ' '],
[' ', '_', '_', '_', '_', '_', '_', ' '],
[' ', ' ', '_', '_', '_', '_', ' ', ' '],
[' ', ' ', ' ', '_', '_', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
]

""" Tohle je hodne memory ineffective.. 
    Zas ale casem toho bude vice
    a navic to bajecne resi kolize. """

def draw_node_from_table(my_surface: MainSurface, my_node_table: list[list[str]]):
    for r, row in enumerate(my_node_table):
        for c, node in enumerate(row):
            if node == 'r':
                draw_node_type(my_surface, (r, c), "village_red")
            if node == 'R':
                draw_node_type(my_surface, (r, c), "city_red")

    return


