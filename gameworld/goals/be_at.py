from gameworld.goals.goal import Goal


class BeAtLocation(Goal):
    def __init__(self,_location,_time):
        self.location = _location
        self.time = _time       #Time object. If 0, no time limit specified
    def calculateTravel(self,World,NPCLocation,NPCMapKnowledge):
        """
        calculates travel time based on npc's location an map knowledge and weather and stuff
        :return: amount of time needed to travel to location. If impossible, returns negative number
        """
        pass