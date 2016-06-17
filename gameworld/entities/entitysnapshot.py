

#TODO: be on the lookout for bugs from referencing, not copying the dictionaries
#records visisble status of an npc, ie: armor, frostbitten limbs, live/dead
class EntitySnapShot():
    def __init__(self, _name, _age, _race, _sex, _nodenumber, _equipped, _alive, _limbstatus):
        self.name = _name
        self.age = _age
        self.race = _race
        self.sex = _sex

        self.nodenumber = _nodenumber
        self.equipped = _equipped
        self.alive = _alive
        self.limbstatus = _limbstatus
