from gameworld.entities.character import Character

class NPC(Character):
    def __init__(self,_name):
        super().__init__(_name)
        self.goals = []
        self.memory = []
        self.routine = []


    def GetRelationships(self,_SocialGraph):
        return _SocialGraph[self.nodenumber]    #Should give edges with attributes
    def PrintStatus(self,_SocialGraph):
        print(self.name,' is at x:',self.x,' y:',self.y, 'with items: ', self.inventory, ' and goals of: ', self.goals)
        print(self.GetRelationships(_SocialGraph))

#TODO: remove these perceive methods and make npcs rely on the isObservable method in the World class
    def PercieveAreaItems(self,World):
        result = []
        for (loc,item) in World.items.items():
            if abs(loc[0]-self.x)<self.perception and abs(loc[1]-self.y)<self.perception:
                result.append(item)
        return result

    def PercieveAreaPeople(self,World):
        result = []
        for npc in World.npcs.values():
            if abs(npc.x-self.x)<self.perception and abs(npc.y-self.y)<self.perception:
                result.append(npc)
        return result

    def PercieveInteractables(self, World):
        result = []
        pass

    def ActionOptions(self):
        pass

