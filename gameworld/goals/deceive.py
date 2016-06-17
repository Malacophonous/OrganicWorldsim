from gameworld.goals.goal import Goal


class Decieve(Goal):    #TODO convert to keyword arguments? NPC target can be group
    def __init__(self,_NPCtarget, _info, _event, _person,_location,_item):
        self.npc = _NPCtarget
        self.event = _event
        self.info = _info
        self.person = _person
        self.location = _location
        self.item = _item