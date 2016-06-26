# high level construction of the gamelogic's view of the game world
# gives a coordinate system for the location class

from gameworld.time import Time
from gameworld.worldsnapshot import WorldSnapShot
from gameworld.entities.peoplemanager import PeopleManager
from gameworld.entities.character import Character



class World():
    def __init__(self):
        self.width = 1024
        self.height = 1024
        self.chunksize = 64
        self.time = Time(0,0,0)
        self.PM = PeopleManager(self)
        self.nations = []
        self.items = dict()     #keyed by location tuple, for items in plain view only IE not in chests or inventories
        self.interactables = dict() #keyed by location tuple


    def determineSituation(self, observer, location, time):
        """
        checks LOS and hearing for local situation from observer's perspective
        :param _observer: Who's perspective this is, NPC object or nodenumber or name
        :param _location: either observer's location or one within LOS
        :param _time: probably current time, other times won't be implemented for awhile
        :return: world snapshot object of local world variables at the time
        """
        observer = self.PM.lookupObject(observer)
        WSS = WorldSnapShot(time, location, self, observer)     #generate a worldsnapshot for the given location and time

        #create Entity snapshots for npcs/pcs visible from perceive area
        visiblePeople = self.PerceiveArea(observer)[3]  #get npcs/pcs from perceive area method
        for person in visiblePeople:
            WSS.people[person.nodenumber] = person.CreatePublicESS()

        #do the same thing for items/interactables, and structures
        #keeping track of ownership as well




        return WSS



    def addNation(self,Nation):
        # check to see if nations will have overlapping mapgrid/chunks
        self.nations.append(Nation)

    def update(self):
        self.time += Time(1,0,0)

    def isObservable(self, observer, *targets):
        """
        determines if npc1 can see any others. Implementation is specific to game details like LOS
        :param observer: Observing npc
        :param targets: any npc, pc, item, interactable, location, or entity in the world
        :return: sublist of targets visible
        """
        observer = self.PM.lookupObject(observer)
        minX = observer.x - observer.perception # Todo: make perception a bit more complicated
        maxX = observer.x + observer.perception # and involve line of sight and illumination
        minY = observer.y - observer.percpetion
        maxY = observer.y + observer.perception
        result = []
        for target in targets:
            if isinstance(target, Character):
                target = self.PM.lookupObject(target)
            if minX <= target.x <= maxX:
                if minY <= target.y <= maxY:
                    result.append(target)
        return result

    def PerceiveArea(self, observer):
        """
        returns lists of all plain view items, interactables, entities and npc/pcs in observer's perception
        :param observer: observing npc
        :return: List of [[items],[interactables],[entities],[npcs/pcs]]
        """
        pass