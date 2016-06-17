from gameworld.interactables.interactable import Interactable

class Door(Interactable):
    def __init__(self, _name, _x, _y):
        super().__init__(_name, _x, _y)
        self.locked = False
        self.open = False