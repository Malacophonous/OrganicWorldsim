# high level construction of the gamelogic's view of the game world
# gives a coordinate system for the location class

from gameworld.time import Time
import networkx as nx
from gameworld.entities.character import Character
from gameworld.worldsnapshot import WorldSnapShot



class World():
    def __init__(self):
        self.width = 1024
        self.height = 1024
        self.chunksize = 64
        self.time = Time(0,0,0)
        self.nations = []
        self.npcs = dict()      # points npc node number to npc object
        self.npcnames = dict()  # points npc name string to an npc object
        self.SG = nx.DiGraph()
        self.items = dict()     #keyed by location tuple, for items in plain view only IE not in chests or inventories
        self.interactables = dict() #keyed by location tuple

    def addNPC(self, _NPC):
        n = len(self.SG.node)
        _NPC.nodenumber = n
        self.npcs[n] = _NPC
        self.npcnames[_NPC.name] = _NPC
        self.SG.add_node(n, npc=_NPC)

    def addRelationship(self, _NPC1, _NPC2, _art=(0, 0, 0), _label=None):
        n1 = self.lookupNodeNumber(_NPC1)
        n2 = self.lookupNodeNumber(_NPC2)
        self.SG.add_edge(n1, n2, a=_art[0], r=_art[1], t=_art[2], label=_label)

    def _getperson(self, infoIn, desiredType):
        """
        private method for getting specific npc or pc data or objects from identifiers
        :param infoIn: object, nodenumber(int), or name(string)
        :param desiredType: 'o', 'i', 's'
        :return: data of desired type referencing the infoIn
        """
        if desiredType == 'i':
            if isinstance(infoIn,int):
                return infoIn
            elif isinstance(infoIn,str):
                return self.npcnames[infoIn].nodenumber
            elif isinstance(infoIn, Character):
                return infoIn.nodenumber
            else:
                raise TypeError
        elif desiredType == 's':
            if isinstance(infoIn,int):
                return self.npcs[infoIn].name
            elif isinstance(infoIn,str):
                return infoIn
            elif isinstance(infoIn, Character):
                return infoIn.name
            else:
                raise TypeError
        elif desiredType == 'o':
            if isinstance(infoIn,int):
                return self.npcs[infoIn]
            elif isinstance(infoIn,str):
                return self.npcnames[infoIn]
            elif isinstance(infoIn, Character):
                return infoIn
            else:
                raise TypeError
        else:
            print('you have problem', infoIn, desiredType)

    def lookupNodeNumber(self, _person):
        try:
            return self._getperson(_person,'i')
        except TypeError as E:
            print('you have problem')
            print(E)
            return 0

    def lookupName(self, _person):
        try:
            return self._getperson(_person,'s')
        except TypeError as E:
            print('you have problem')
            print(E)
            return ''

    def lookupObject(self, _person):
        try:
            return self._getperson(_person,'o')
        except TypeError as E:
            print('you have problem')
            print(E)
            return None

    def determineSituation(self, observer, location, time):
        """
        checks LOS and hearing for local situation from observer's perspective
        :param _observer: Who's perspective this is, NPC object or nodenumber or name
        :param _location: either observer's location or one within LOS
        :param _time: probably current time, other times won't be implemented for awhile
        :return: world snapshot object of local world variables at the time
        """
        observer = self.lookupObject(observer)
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
        observer = self.lookupObject(observer)
        minX = observer.x - observer.perception # Todo: make perception a bit more complicated
        maxX = observer.x + observer.perception # and involve line of sight and illumination
        minY = observer.y - observer.percpetion
        maxY = observer.y + observer.perception
        result = []
        for target in targets:
            if isinstance(target, Character):
                target = self.lookupObject(target)
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