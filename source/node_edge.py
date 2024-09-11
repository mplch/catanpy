from pygame.transform import rotate

# from source.constants import TILE_SIZE
from source.main_surface_class import MainSurface
import source.constants as C


def get_node_pix_coord(hex_coord, orientation):
    pass

"""
Jedna vec je pristup z tily,
jina vec je pristup z cele mapy.
Kreje se to.

Takze bych mozna udelat nejprve celkovy overlay,
pak bych udelal overlay jednotlivych hexu.
A pak bych nejakym zpusobem nachazel prunik.

Bez toho celkového pohledu se nehnu
a navic by to bylo peklo zkoordinovat.

Pripomina mi to, ze stale nemam reprezentaci ani mapy.

Dejme tomu, ze se budou postupne, asi po radach (sloupcich)
- snad to hexy prilis nerozbori svou "clenitosti" -
- no a pak budu mít funkci, ktera se mi "zepta", jake hexy jsou v okoli.

Potrebuji pix_coordy vsech nod ( cest )...


Jo, jenze jeste je ale vtipne, ze...necentricke souradnice.
Jako teoreticky, v pripade ctvercovych spritu,
nejde o nic jineho, nez o pricteni poloviny hrany v obou smerech,
respektive naopak v pripade pokladani.
Otazka zni, jestli se ma v pripade nody a cesty bavit o stredu...
...kdyz velikost jejich hrany je SUDE cislo.

Mozna to vidim tak, ze zas proste experimentalne vyladim offsety..

"""






NODE_H = 12
NODE_W = 10
NODE_STRIP = 2
NODE_OVERLAP_X = 7
NODE_GAP_X = 12
# lol.. to ver_con a hor_con byly asi CONSTANTY :D
NODE_PULL_BACK = -12
ROWS = 3
COLS = 1


def draw_nodes(my_surface: MainSurface):
# def draw_nodes(surface: pygame.Surface):
    node = my_surface.s_atlas.atlas_dict["nodes"]["node_left"]
    node = rotate(node, 180)  # IF SHIFT 1ST COL
    for node_coords in get_node_coords(my_surface.tile_size):
        my_surface.blit2(node, node_coords)
        node = rotate(node, 180)


# DO_SHIFT_COLUMN !!!
def get_node_coords(tile_size):
    res = []
    for c in range(COLS + 1):
        for i in range(ROWS * 2 + 1):

            x = C.MAP_OFF_PIX_X + NODE_OVERLAP_X

            if c%2 == 0:  # 1, 3, 5 ..
                x += (i % 2) * NODE_PULL_BACK
            else:
                x -= (i % 2) * NODE_PULL_BACK

            x += c * C.HEX_HORI_EDGE_X
            x -= (c+1) * NODE_STRIP
            y = C.MAP_OFF_PIX_Y - C.STRIP_HEIGHT + i * C.HEX_HEIGHT//2



            res.append((x, y))
            print("Added: c, r, x, y:", c, i, x, y)

    # print("Node coords:", res)
    return res


# def flip(a):
#     if a:
#         return False
#     return True
