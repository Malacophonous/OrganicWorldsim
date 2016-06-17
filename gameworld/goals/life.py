from gameworld.goals.goal import Goal


class SatisfyLifeGoal(Goal):
    def __init__(self,_need):   #high level goal for content existance/power/knowledge/
        self.need = _need       #self-actualization/revenge/or sensation(hedonism/thrillseeking)
