from gameworld.location import Location

class Town(Location):
    def __init__(self, _x,_y):
        self.x = _x
        self.y = _y
        self.buildings = []
        self.residents = []
        self.locations = []