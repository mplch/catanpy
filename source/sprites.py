from pygame import image as pyg_img


def load_sprite(file_path: str):
    return pyg_img.load(file_path).convert_alpha()


# ---

# worldlist = dict()

# -----

atlas = dict()

""" for all in wordlist: load sprite and add to atlas"""
""" load all images in folder with respective names """
""" a to je duvod, proc wordlist ani nepotrebuji..."""
""" SCAN FOLDER """

cake_folder = "textures/cakes/"
suffix = ".png"
cakes_list = [  # TEMPORARY
    "Clay_pit", "Desert", "Field", "Forest", "Mountains", "Pasture"
    ]

temp = []
for cake in cakes_list:
    file_path = cake_folder + cake + suffix
    img = pyg_img.load(file_path).convert_alpha()
    temp.append(img)

atlas["cakes"] = temp

print(atlas)

 """
 
   File "/home/marek/f-catanpy/source/sprites.py", line 30, in <module>
    img = pyg_img.load(file_path).convert_alpha()
pygame.error: cannot convert without pygame.display initialized

:///
"""