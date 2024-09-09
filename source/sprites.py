from pygame import image as pyg_img

import source.constants as C

def load_sprite(file_path: str):
    return pyg_img.load(file_path).convert_alpha()


def cakes_init(cakes_list):
    temp = dict()
    for cake in cakes_list:
        file_path = cake_folder + cake + suffix
        img = pyg_img.load(file_path).convert_alpha()
        temp[cake] = img
    return temp


def sprite_list_init(sprites_list, sprite_folder, suffix=C.DEFAULT_IMAGE_SUFFIX):
    # Sprite_list wont be needed in future --> will be obtained from folder scanning
    temp = dict()
    for sprite in sprites_list:
        file_path = sprite_folder + sprite + suffix
        img = pyg_img.load(file_path).convert_alpha()
        temp[sprite] = img
    return temp


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
    "Clay_pit", "Desert", "Field", "Forest", "Mountains", "Pasture", "Sea"
]  # Missing "Sea" (!)

# mozna lepsi z atlasu udelat Classu ?
# a pristupovat tak pres botku ?

print(atlas)


"""
    File "/home/marek/f-catanpy/source/sprites.py", line 30, in <module>
    img = pyg_img.load(file_path).convert_alpha()
pygame.error: cannot convert without pygame.display initialized

:/
"""


if __name__ == "__main__":
    pass
