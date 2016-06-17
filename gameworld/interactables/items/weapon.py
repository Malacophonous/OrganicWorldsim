from gameworld.interactables.items.item import Item

class Weapon(Item):
    def __init__(self, _size, _weight, _type):
#        super().__init__(_name, _x, _y)
        self.size = _size
        self.weight = _weight
        self.quality = 0
        self.type = _type