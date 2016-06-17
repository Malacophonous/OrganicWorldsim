from gameworld.location import Location


class Nation(Location):
    def __init__(self, _x, _y, _name):
        self.x = _x
        self.y = _y
        self.name = _name
        self.towns = []
        self.citizens = []
        self.rulers = []
        self.mapgrids = []
        self.locations = []
