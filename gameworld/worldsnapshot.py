class WorldSnapShot():
    def __init__(self, _time, _location, _World, _observer):
        self.time = _time
        self.location = _location
        self.observer = _observer
        self.people = dict()    #entity snapshot of people around keyed by node number
        self.interactables = dict() #status of interactables
        self.items = dict()     #local items keyed by npc node number
        self.structures = None  #local structure's status

    def __add__(self, other):
        pass

    #This is for making world state vectors in a local area for determining just
    #what changes when events occur
    def __sub__(self, other):
        pass