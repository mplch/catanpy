class TileType():
    plate = None
    cake = None
    tuple = (None, None)
    
    def __init__(self, plate, cake):
        self.plate = plate
        self.cake = cake
        self.tuple = (plate, cake)

    # str / repr methods
