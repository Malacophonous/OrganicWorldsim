from gameworld.goals.goal import Goal

class ChangeRelationship(Goal):
    def __init__(self,_target,**kwargs):
        self.changeA = kwargs['A']  #positive means seek relation increase of x
        self.changeR = kwargs['R']  #0 means no change wanted to stat
        self.changeT = kwargs['T']  #negative means seek relation decrease of x
        self.target = _target