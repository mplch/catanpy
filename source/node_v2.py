import source.constants as C
from source.main_surface_class import MainSurface
from source.transforms import HexCoord, PixCoord
from source.transforms import node_hex2pix, transpose

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

    # table = list(list(" "))  ## Seems like this works??
    table: list[list[str]]
    w = SHADOW_NODE_COL_END
    h = SHADOW_NODE_ROW_END

    def __init__(self, node_list: list[HexCoord]):
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

    def fill_from_list(self, node_list: list[HexCoord]):
        for node_hex_coord in node_list:
            rr, cc = node_hex_coord.rc
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
                draw_node_type(my_surface, HexCoord(r, c), "village_red")
            if node == 'R':
                draw_node_type(my_surface, HexCoord(r, c), "city_red")

    return

# ---------------------------------------------------------------------

def draw_node_type(my_surface: MainSurface,
                   node_coord: HexCoord,
                   node_type="default"
                   ):
    node = my_surface.s_atlas.atlas_dict["nodes"][node_type]
    pix_coord: PixCoord = node_hex2pix(node_coord)
    my_surface.blit_pix(node, pix_coord)
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

            my_map_nodes_list.append( HexCoord(rr, cc) )

    return my_map_nodes_list


def draw_inner_nodes(my_surface: MainSurface):
    for node_hex_coord in get_valid_nodes_list():
        draw_node_type(my_surface, node_hex_coord)
    return

# ---------------------------------------------------------------------

def get_hex_neighbour_node_coords(tile_coord: HexCoord):
    # Opet nejaky hrozny problem v inkonzistenci rc a cr souradnic.

    neigh_candidates = []  # 6 members

    c, r = tile_coord.rc  # WHYYYYYY
    r *= 2
    r += C.NODE_TABLE_OFFSET_Y

    if c % 2 == 0:
        r += 1

    """ Ale ted uz to vypada, ze to dela co by melo, tak co resiim?? """

    vector_list = []
    for i in [-1, 0, +1]:
        for j in [0, +1]:
            vector_list.append((i,j))

    for a, b in vector_list:
        node_coord = HexCoord(r+a, c+b)  # rr, cc
        neigh_candidates.append(node_coord)

    # print("neighs: ", neigh_candidates)  # Vypisuje blbost object<at:0x>
    return neigh_candidates


def highlight_hex_neighbour_nodes(my_surface: MainSurface,hex_coord: HexCoord):
    my_surface.put_coord(hex_coord)
    print("Highlighting hex at:", hex_coord)
    print("Nodes coords: (rr, cc)")
    for node_coord in get_hex_neighbour_node_coords(hex_coord):
        print(node_coord)
        draw_node_type(my_surface, node_coord, "free")
