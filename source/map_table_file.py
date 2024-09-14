from source.transforms import transpose

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
E = "Fields"
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
    ,[_,  O,  O,  O,  O,  O,  _]    #
      ,[_,  O,  O,  O,  O,  _,  I]  #
    ,[I,  _,  O,  O,  O,  _,  I]    #
      ,[I,  _,  _,  _,  _,  I,  I]  #
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
