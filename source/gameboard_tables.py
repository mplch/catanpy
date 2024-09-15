
# F = "forest"
# P = "pasture"
# M = "mountains"
# C = "clay_pit"
# E = "fields"
# _ = "sea"
# X = "desert"

""" Capitalise first letter ?? """

F = "Forest"
P = "Pasture"
M = "Mountains"
C = "Clay_pit"
E = "Field"
_ = "Sea"
X = "Desert"


map_example_transposed = [
    [_]*7
    ,[_, _, P, C, P, _, _]
    ,[_, F, M, M, M, _, _]
    ,[_, C, F, E, P, E, _]
    ,[_, F, P, E, X, _, _]
    ,[_, _, E, C, F, _, _]
    ,[_]*7
]

# SIMILARLY WITH YIELD NUMBERS


O = 'O'
I = ' '

default_map_table_transposed = [
       [I,  _,  _,  _,  _,  I,  I]  #
    ,[I,  _,  O,  O,  O,  _,  I]    #
      ,[_,  O,  O,  O,  O,  _,  I]  #
    ,[_,  O,  O,  X,  O,  O,  _]    #
      ,[_,  O,  O,  O,  O,  _,  I]  #
    ,[I,  _,  O,  O,  O,  _,  I]    #
      ,[I,  _,  _,  _,  _,  I,  I]  #
]

default_map_table_transposed = [
       [I,  _,  _,  _,  _,  I,  I]  #
    ,[I,  _,  C,  C,  C,  _,  I]    #
      ,[_,  E,  F,  M,  P,  _,  I]  #
    ,[_,  E,  F,  X,  M,  P,  _]    #
      ,[_,  E,  F,  M,  P,  _,  I]  #
    ,[I,  _,  E,  F,  P,  _,  I]    #
      ,[I,  _,  _,  _,  _,  I,  I]  #
]


A = 5
B = 2
C = 6
D = 3
E = 8
F = 10
G = 9
H = 12
I = 11
J = 4
K = 8
L = 10
M = 9
N = 4
O = 5
P = 6
Q = 3
R = 11

_ = "Sea"
q = ' '
X = 0

default_yield_table_transposed = [
       [q,  _,  _,  _,  _,  q,  q]  #
    ,[q,  _,  A,  B,  C,  _,  q]    #
      ,[_,  L,  M,  N,  D,  _,  q]  #
    ,[_,  K,  R,  X,  O,  E,  _]    #
      ,[_,  J,  Q,  P,  F,  _,  q]  #
    ,[q,  _,  I,  H,  G,  _,  q]    #
      ,[q,  _,  _,  _,  _,  q,  q]  #
]

# Vektory: (A)
# (0, -1); (0; +1);
# (-1, 0); (+1, 0);
# (-1, +1); (+1, +1)  # These change

# Vektory: (B)
# (0, -1); (0; +1);
# (-1, 0); (+1; 0);
# (-1, -1); (-1, +1);  # These change

### UNDO TRANSPOSE ###

# Vektory: (A)
# (-1, 0); (+1, 0);  # SWAP
# (0, -1); (0; +1);  # SWAP
# (+1, -1); (+1, +1)  # First change, second same

# Vektory: (B)
# (-1, 0); (+1; 0);  # SWAP
# (0, -1); (0; +1);  # SWAP
# (-1, -1); (+1, -1);  # First same, second change

# Je zvlastni a zajimave, ze se meni pouze jedna souradnice..
