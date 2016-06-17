from gameworld.goals.goal import Goal


class ConverseWith(Goal):
    def __init__(self,_person):
        self.target = _person
