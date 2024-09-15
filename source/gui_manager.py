from source.main_surface_class import MainSurface
from source.transforms import HexCoord, PixCoord

def testing_cards(inner_surface: MainSurface):
    CARD_BOTTOM_OFFSET = 5  # NOMENCLATURE: Margin + Padding
    CARD_BETWEEN_OFFSET = 5
    card_wh = inner_surface.s_atlas.atlas_dict["cards"]["Brick"].get_size()
    # print("cards wh", card_wh)
    x = inner_surface.w // 3 + 20
    y = inner_surface.h - CARD_BOTTOM_OFFSET - card_wh[1]
    for name, card in inner_surface.s_atlas.atlas_dict["cards"].items():
        x = x + card_wh[0] + CARD_BETWEEN_OFFSET
        card_pix_coord = PixCoord(x, y)
        inner_surface.blit_pix(card, card_pix_coord)
    return 
