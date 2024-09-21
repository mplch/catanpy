from pygame import image as pyg_img

import source.constants as C

TEXTURES = "textures"
PLATES = "plates"
CAKES = "cakes"
CARDS = "cards"


class Sprite:
    """ Placeholder """
    # Will this be to any good?
    pass


class Atlas:
    # class Atlas(dict):  # (?)
    # Jak udelat, aby class mel stejne vlastnosti jako dict,
    # ale nebyl to dict?
    # Je nutne, aby to nebyl dict?
    a_dict = dict()

    def init_all(self):
        
        # NAME LISTS ARE TEMPORARY
        
        self.a_dict[PLATES] = sprite_list_init(
            ["Sea", "Land", "TemPlate", "Desert"],
            get_sprite_folder(PLATES)
        )
        
        self.a_dict[CAKES] = sprite_list_init(
            ["Clay_pit", "Desert", "Field", "Forest", "Mountains", "Pasture", "Sea"],
            get_sprite_folder(CAKES)
        )

        self.a_dict[CARDS] = sprite_list_init(
            ["Brick", "Rock", "Sheep", "Wood", "Wheat", "Template"],
            get_sprite_folder(CARDS)
        )
        
        self.a_dict["nodes"] = sprite_list_init(
            ["node_left", "node_right", "village_red", "free", "select", "city_red", "default"],
            get_sprite_folder("nodes")
        )

        self.a_dict["gui"] = sprite_list_init(
            ["card_deck"],
            get_sprite_folder("gui")
        )


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


if __name__ == "__main__":
    pass
