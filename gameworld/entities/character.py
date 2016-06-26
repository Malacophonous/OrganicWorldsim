from gameworld.entities.entity import Entity
from gameworld.entities.entitysnapshot import EntitySnapShot

class Character(Entity):
    def __init__(self,_name):
        super().__init__()
        #important game variables
        self.name = _name
        self.nodenumber = 0

        #character variables
        self.age = 0
        self.race = None
        self.sex = 0    #0 is male, 1 is female
        self.orientation = 0
        self.job = ''
        self.appearance = ''
        self.history = ''
        self.home = None

        #character basic stats
        self.agility = 0
        self.curiosity = 0
        self.determination = 0
        self.perception = 0
        self.strength = 0
        self.sociability = 0

        self.skills = []

        self.inventory = []

        self.equipped = dict()
        self.alive = 1  #0 is dead, 1 is alive, 2 is sleeping
        self.limbstatus = {'head':0,'torso':0,'larm':0,'rarm':0,'lleg':0,'rleg':0,'lhand':0,'rhand':0,'lfoot':0,'rfoot':0}
        #0 is healthy, 1 recovering, 2 is broken, 4 is bleeding, 8 is diseased, 16 is frostbitten -1 is amputated




    def CreatePublicESS(self):
        return EntitySnapShot(self.name,self.age,self.race,self.sex,self.nodenumber,self.equipped,self.alive,self.limbstatus)
