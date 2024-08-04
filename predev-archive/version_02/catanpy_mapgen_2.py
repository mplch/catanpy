# INPUT PARAMETERS
"""
int height;
int width;
bool hex OR rect;
"""


"""
DIMENSIONs of ARRAY
1x1: 5r9c --> 5r10c

"""

def generate(W, H):
    assert(W>0, H>0)
    w = (9-2)*W + 2
    h = (5-1)*H + 1
    map_templ = """
      H---H
     /     \\
    H   X   H---H
     \     /     \\
      H---H   X   H
     /     \     /
    H   X   H---H
     \     /
      H---H
    """
    """
    row types: (4)
    a) offside
    b) rising
    c) atbegin
    d) falling
    -) offside (...)
    """
    print("  H---H")
    print(" /     \\")
    print("H   X   H---H")
    print(" \     /     \\")
    print("  H---H   X   H")

    print(SPACER*2 + NODE + EDGE*3 + NODE + "\n")
    print(NODE + SPACER*3 + TILE + SPACER*3 + NODE + EDGE*3 + NODE + "\n")
    print(SPACER*1 + RISING + SPACER*5 + FALLING + FALLING + "\n")
    print(SPACER*1 + FALLING + SPACER*5 + RISING + SPACER*5 + FALLING + FALLING + "\n")

    def print_row_nodes():
        # ARG:  bool TILE_ODD
        # UFFF, its just sooo COMPLEX.. :/
        # and i suppose mapgen is not needed right now for MVP - minimum value product
        # co tedy potrebuji?
        # example mapu mam
        # ... HRATELNOST
        # e.g. moznost POKLADAT FIGURKY na mapu
        pass

    def print_row_edges():
        pass


#-----------------------------------

"""
base tiles (percentage)
1+6+12 = desert + 18
3 ORE (STONE)
3 BRICKS
4 WOOD
4 SHEEP
4 WHEAT
3/18 = 1/6 = 16.67 %
             33.34 %
        rem: 66.66 %  // (not.67)
split by 3 : 22.22 %
split by 4 : 5.555 %
---
3/18 -> per tile:
    1/18 = 1/6/3 = 16.67/3 = 5.553
... zajímavá čísla
RESP: 5.553% a 5.555%
Spočítal jsem to správně?

Nicméně, to asi není tak podstatné
 - byť vím, k čemu jsem je chtěl.
Ale per 1 tile mě vlastně nezajímá. :D

ORE     (16.67%)
BRICKS  (16.67%)
WOOD    (22.22%)
SHEEP   (22.22%)
WHEAT   (22.22%)
SUM    (100.00%)
desert  (...) -> nutné přepočítat
"""