from gameworld.goals.goal import Goal

class SatisfySurvivalNeeds(Goal):
    def __init__(self,_need): #High level goal for food, drink, clothing, shelter
        self.need = _need