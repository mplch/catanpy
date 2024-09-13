from pygame import image as pyg_img

import source.constants as C

TEXTURES = "textures"
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


def get_sprite_folder(sprite_type: str):
    return TEXTURES + '/' + sprite_type + '/'


class Atlas:
    # class Atlas(dict):  # (?)
    atlas_dict = dict()

    def init_all(self):
        
        # NAME LISTS ARE TEMPORARY
        
        self.atlas_dict[PLATES] = sprite_list_init(
            ["Sea", "Land", "TemPlate"],
            get_sprite_folder(PLATES)
        )
        
        self.atlas_dict[CAKES] = sprite_list_init(
            ["Clay_pit", "Desert", "Field", "Forest", "Mountains", "Pasture", "Sea"],
            get_sprite_folder(CAKES)
        )

        self.atlas_dict[CARDS] = sprite_list_init(
            ["Brick", "Rock", "Sheep", "Wood", "Wheat", "Template"],
            get_sprite_folder(CARDS)
        )
        
        self.atlas_dict["nodes"] = sprite_list_init(
            ["node_left", "node_right"],
            get_sprite_folder("nodes")
        )


if __name__ == "__main__":
    pass
