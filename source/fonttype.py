# from pygame.font import Font


class FontType:

    # Is the below thing -needed- necessary??
    name = ""
    size = 0
    color = (0, 0, 0)

    # def __init__(self, font: Font, size, color):
    def __init__(self, font_name: str, size: int, color: tuple[int, int, int]):
        self.name = font_name
        self.size = size
        self.color = color
