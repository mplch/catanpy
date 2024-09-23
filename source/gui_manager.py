from pygame.transform import scale_by
from random import randint

from source.constants import CARD_WIDTH, CARD_HEIGHT

from source.main_surface_class import MainSurface
from source.transforms import HexCoord, PixCoord
from source.custom_type_classes import Resource


def draw_card_deck_prototype(inner_surface: MainSurface):

    CARD_BOTTOM_OFFSET = 5  # NOMENCLATURE: Margin + Padding
    CARD_BETWEEN_OFFSET = 5
    # ATLAS
    # card_wh = inner_surface.s_atlas.a_dict["cards"]["Brick"].get_size()
    # print("cards wh", card_wh)

    x = inner_surface.w // 3 + 20
    y = inner_surface.h - CARD_BOTTOM_OFFSET - CARD_HEIGHT
    for name, card in inner_surface.s_atlas.a_dict["cards"].items():
        x = x + CARD_WIDTH + CARD_BETWEEN_OFFSET
        card_pix_coord = PixCoord(x, y)
        inner_surface.blit_pix(card, card_pix_coord)
    return 


def assign_card(inner_surface: MainSurface,
                resource: Resource,
                player_no: int,
                ) -> PixCoord:
    """ ---
    TODO:
    FIRST ASSIGN PROGRAMATICALLY TO SOME DICT
    --> ONLY THEN DRAW --> no inner surface paramater..
    """

    # I'd need card_dimensions parameter here. :/
    # x_start = inner_surface.w // 2
    # x = randint(x_start, inner_surface.w)
    # y = randint(0, inner_surface.h)

    # Tohle by tu v pozdejsi fazi nemelo vubec byt!!
    # Scalovani na jedinem miste POUZE!
    x *= inner_surface.scale
    y *= inner_surface.scale
    return PixCoord(x, y)


def show_resource_card(inner_surface: MainSurface,
                       resource: Resource,
                       pix_coords: PixCoord):
    card = inner_surface.s_atlas.a_dict["cards"][resource]
    card_scale = (inner_surface.scale, inner_surface.scale)
    card = scale_by(card, card_scale)

    inner_surface.blit_pix(card, pix_coords)

#----------------------------------------------------------------------

def show_card_decks(inner_surface: MainSurface,
                   player_number: int):
    card_deck = inner_surface.s_atlas.a_dict["gui"]["card_deck"]
    # AGAIN !! Vyresim holt nejak nepekne..
    CARD_H = 50  # konstanta actually??
    POSITION_X = 0.60
    OFFSET_Y = 35
    x = inner_surface.w * POSITION_X
    y = 5  # RELATIVE!
    y_add = 0 + OFFSET_Y + CARD_H
    # CHECK PLAYER NUMBER!
    for _ in range(player_number):
        inner_surface.blit_pix(card_deck, PixCoord(x, y))
        y += y_add
