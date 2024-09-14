FOREST     = 'F' #darkgre
PASTURE    = 'P' #lightgre
MOUNTAINS  = 'M' #gray
CLAY_PIT    = 'C' #orange        # HILLS
FIELDS     = 'E' #ellow         # dovymyslim pozdeji
DESERT     = 'D' #sandy, white  # klido bila
SEA        = 'S' #dark blu

F = "forest"
P = "pasture"
M = "mountains"
C = "clay_pit"
E = "fields"
_ = "sea"
X = "desert"


map_example_transpose = [
    [_]*7
    ,[_, _, P, C, P, _, _]
    ,[_, F, M, M, M, _, _]
    ,[_, C, F, E, P, E, _]
    ,[_, F, P, E, X, _, _]
    ,[_, _, E, C, F, _, _]
    ,[_]*7
]


def transpose(old):
    r_new = len(old[0])
    c_new = len(old)
    for row in old: print(row)
    # new = [ ['_']*c_new ]*r_new  # nejaka provazanost...
    new_matrix = []
    for i in range(r_new):
        new_row = []
        for j in range(c_new):
            new_row.append(old[j][i])
        new_matrix.append(new_row)
    for row in new_matrix: print(row)
    return new_matrix


# SIMILARLY WITH YIELD NUMBERS



O = 'O'
I = ' '
X2 = X

map_def_temp = transpose([
       [I,  _,  _,  _,  _,  I,  I]  #
    ,[I,  _,  O,  O,  O,  _,  I]    #
      ,[_,  O,  X,  O,  O,  _,  I]  #
    ,[_,  O,  O,  O,  O,  O,  _]    #
      ,[_,  O,  O,  O,  O,  _,  I]  #
    ,[I,  _,  O,  X2,  O,  _,  I]    #
      ,[I,  _,  _,  _,  _,  I,  I]  #
])

# NEIGHBORS OF X ARE: (RCt=33)
# 23, 24, 32, 34, 43, 44
# Vektory: (-1, 0); (-1, +1); (0, -1); (0; +1); (+1, 0); (+1, +1)  # TRANSPONOVANE!!!
# Budou vsude stejne?? Nekomplikuje to klikaty radek??
# Podle me se bude menit sudy lichy..
# Ale mohlo by byt konsistentni v ramci... sloupec..
# Takze kdyz vezmu X2 na RCt=64
# Sousedi: 53, 54, 63, 65, 73, 74
# (...)
# V zasade (mluvim v transponovanem)
# levy a pravy jsou jasni, horni a dolni vicemene take
# ale paty a sesty soused, bude nalevo/napravo od horniho a dolniho
# v zavislosti na tom, jestli je prave v predbihavem/zpozdenem radku.
# Pak zbyli sousedi budou presne naopak v zpozdenem/predbihavem radku.
# Not so bad actually.
# Alespon tahle reprezentace, narozdil od te zkosene trojuhelnikove,
# ma podstatne blize k vyslednemu vizualu. U trojuhelniku jsou posuny prilis velke.

"""
 * How to programm this?
 *
 * First note:
 * Its vertically symmetrical.
 * (Except the edge seas.)
 *
 * Second note:
 * And it is even MORE symmetrical horizontally
 *
 * Na tomhle asi nemusim zatim nic porgramovat.
 * Ponechal bych to nahardkodene.
 *
 * Prevedu na string a kde je 'O' / '_' dam hex_stack.pop() / Sea, prip. continue
 *
 * Potom mozna otazka, jak z toho ziskat souradnice nod.
 * Two way dictionary.. ;-) (Vlastne staci jen jeden a pak se udela kopie a otocoi naruby.)
"""


