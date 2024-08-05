from random import shuffle

stack = []


##########################x
hexes = "textures/hexes/"
hextypes = "Claypit.png  Desert.png  Field.png  Forest.png  \
Mountains.png  Pasture.png  Sea.png  Template_vert".split('  ')
# odeber png (a zpet pridej) --> hexes + type + ".png"
hexlands = "Claypit.png  Field.png  Forest.png  \
Mountains.png  Pasture.png".split('  ')
for t in hexlands: print(">",t,"<")
############################


hexdir = {
    "Claypit" : 3,
    "Desert": 1,
    "Field" : 4,
    "Forest" : 4,
    "Mountains" : 3,
    "Pasture" : 4,
    "Sea" : 0,
}

for key, val in hexdir.items():
    for _ in range(val):
        stack.append(key)

shuffle(stack)