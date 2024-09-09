from pygame import image as pyg_img

import source.constants as C

PLATES = "plates"
CAKES = "cakes"
CARDS = "cards"


def load_sprite(file_path: str):
    return pyg_img.load(file_path).convert_alpha()


def sprite_list_init(sprites_list, sprite_folder, suffix=C.DEFAULT_IMAGE_SUFFIX):
    # Sprite_list wont be needed in future --> will be obtained from folder scanning
    temp = dict()
    for sprite in sprites_list:
        file_path = sprite_folder + sprite + suffix
        img = pyg_img.load(file_path).convert_alpha()
        temp[sprite] = img
    return temp


class Atlas:
    # class Atlas(dict):  # (?)
    atlas_dict = dict()

    def init_all(self):
        cakes_list = [  # TEMPORARY
            "Clay_pit", "Desert", "Field", "Forest", "Mountains", "Pasture", "Sea"
        ]
        plate_names = ["Sea", "Land"]
        self.atlas_dict[PLATES] = sprite_list_init(plate_names, "textures/plates/")
        self.atlas_dict[CAKES] = sprite_list_init(cakes_list, "textures/cakes/")

        card_names = [
            "Brick", "Rock", "Sheep", "Wood", "Wheat", "Template"
        ]
        self.atlas_dict[CARDS] = sprite_list_init(card_names, "textures/cards/")


if __name__ == "__main__":
    pass
