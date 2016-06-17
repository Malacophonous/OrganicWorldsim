from gameworld.interactables.interactable import Interactable

'''
Items are of several statuses:
Owned items     -Have owner tag set
Unowned         -Free to take, no owner
plain view items    -Items visisble on shelves, displaycases, countertops, lying on the ground
items in inventory  -Items in someone's local inventory (pack, ususally invisible)
items in chests/containers  - Items in a chest or container (not mobile in someones inventory, not visible)
items in use    -Items being used/equipped/worn Tagged as visible
'''


class Item(Interactable):
    def __init__(self, _name, _x, _y):
        super().__init__(_name, _x, _y)

    def PrintStatus(self):
        print(self.name, ' is at x:',self.x,' y:',self.y)