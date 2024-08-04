RED = "\033[91m\033[K"
GRE = "\033[32m\033[K"
YEL = "\033[33m\033[K"
BLU = "\033[34m\033[K"
END = "\033[m\033[K"

FOREST     = 'F' #darkgre
PASTURE    = 'P' #lightgre
MOUNTAINS  = 'M' #gray
CLAYPIT    = 'C' #orange        # HILLS
FIELDS     = 'E' #ellow         # dovymyslim pozdeji
DESERT     = 'D' #sandy, white  # klido bila
SEA        = 'S' #dark blu

# HRACI: ABCD spis tezko, ale slo by R G Y B, resp. budou barevni
# mesto a vesnice, budiz zatim jen to H, pripadne (A) V, M -cool
# CISLA musi zustat cisly na RESOUCES yield
# mala pismenka bych nechal na suroviny (karty) NEBO OZN poli
# ozn poli nebude stacit, kdyby jich bylo pres 26 - souradnice?
# bala pismenka rgby budiz barvy hracu na cestach
# cislo yieldu na barevnem pozadi dle suroviny

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

map_w_coords = """

    012 3 456 7 890
    0 2   4 6   8 10
     1  3  5  7  9

      000 0 000 0 001
      012 3 456 7 890

00    ..H---H
01    ./     \\
02    H   X   H---H
03    .\     /     \\
04    ..H---H   X   H
05    ./     \     /
06    H   X   H---H
07    .\     /
08    ..H---H

"""

map_w_coords_2 = """

      0 2 . 4 6 . 8 0

00    ..H---H
      ./     \\
02    H   X   H---H
      .\     /     \\
04    ..H---H   X   H
      ./     \     /
06    H   X   H---H
      .\     /
08    ..H---H

"""

print(map_templ)