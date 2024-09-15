class TileType:
    plate: str
    cake: str
    tuple: tuple[str, str]

    def __init__(self, plate, cake):
        self.plate = plate
        self.cake = cake
        self.tuple = (plate, cake)

    def __str__(self):
        return str(self.tuple)
