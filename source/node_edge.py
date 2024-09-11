from pygame.transform import rotate

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

def draw_nodes(my_surface: MainSurface):
# def draw_nodes(surface: pygame.Surface):
    node = my_surface.s_atlas.atlas_dict["nodes"]["node_left"]
    for node_locations in get_node_locations(my_surface.tile_size):
        temp_node = node
        if node_locations[1] == True:
            temp_node = rotate(node, 180)
        my_surface.blit2(temp_node, node_locations[0])
    pass


# DO_SHIFT_COLUMN !!!
def get_node_locations(tile_size):
    board_coords = [(0+NODE_STRIP, 0), (26, 0)]
    rotations = [True, False]
    res = []
    for i, (a, rot) in enumerate(zip(board_coords, rotations)):
        x, y = 0, 0
        x = a[0] + C.MAP_OFF_PIX_X + i * NODE_W
        # y = a[1] + C.MAP_OFF_PIX_Y + tile_size//2 - C.STRIP_HEIGHT - NODE_H//2
        y = a[1] + C.MAP_OFF_PIX_Y - C.STRIP_HEIGHT
        # tady to pak asi vidim na novou classu
        res.append(((x, y), rot))
    return res
    pass
