from gameworld.goals.goal import Goal

class SatisfySafetyNeeds(Goal):
    def __init__(self,_need):   #high level goal for personal, financial, health, safetynet
        self.need = _need