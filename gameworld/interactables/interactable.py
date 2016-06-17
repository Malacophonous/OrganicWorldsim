class Interactable():
    def __init__(self, _name, _x, _y):
        self.x = _x
        self.y = _y
        self.name = _name
    def PrintStatus(self):
        print(self.name, ' is at x:',self.x,' y:',self.y)