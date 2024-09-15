b = "Brick"
o = "Rock" # r,c! # Ore
s = "Sheep"
w = "Wood"
g = "Wheat" # grains

class Cost(dict):
    b: 0
    o: 0
    s: 0
    w: 0
    g: 0

    # def __init__(self):
    #     super().__init__()  # ???

    building_ = {
        "village": 5,
        "city": 4,
        "road": 15,
    }

cost_table = """
xxxxxxxx: b o s w g
village:  1 0 1 1 1
city:     0 3 0 2 0
road:     1 0 0 1 0
act_card: 0 1 1 0 1
"""