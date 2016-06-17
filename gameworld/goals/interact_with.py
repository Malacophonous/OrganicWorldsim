from gameworld.goals.goal import Goal


class InteractWithWorld(Goal):
    def __init__(self,_interactable, **kwargs):
        self.interactable = _interactable
        '''
        if 'take' in kwargs.keys():
            self.item = kwargs['take']
        elif 'drop' in kwargs.keys():
            self.item = kwargs['drop']
        elif 'use' in kwargs.keys():
            self.interactable = kwargs['use']
        else:
            #what do?
            pass
        self.location = kwargs['at']
        self.time = kwargs['when']
        '''
    def determineToolsNeeded(self):
        pass