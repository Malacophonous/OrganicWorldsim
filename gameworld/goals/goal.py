

# acts as base class for goals
# also used as way to keep goal hierarchy structured
# subclasses inherit this class's ability to act as nodes on the goal tree
# which is iterated over by the goal engine
class Goal():
    def __init__(self, _parent, _importance, *_conditions):
        """
        Base Goal class for GoalEngine tree structure
        :param _parent: parent node for this goal
        :param _importance: integer from 0-100, defines how important this goal is to the NPC
        :param _conditions: other conditions to the goal (seldom used I hope)
        :return:
        """
        self.conditions = _conditions
        self.parent = _parent
        self.children = []
        self.importance = _importance

