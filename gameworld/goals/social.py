from gameworld.goals.goal import Goal

class SatisfySocialNeeds(Goal):
    def __init__(self,_need):   #high level goal for love and belonging needs
        self.need = _need