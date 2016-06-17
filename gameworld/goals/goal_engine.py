from gameworld.goals import *

'''
GoalEngine is a class for containing a tree-like structure of goals for
use in the action evaluation system and the memory system.
Each high level goal (survival, safety, social, esteem, life) spawns a
number of goals below it that could be simple actions,
such as interacting with an item at their feet, to complicated concepts
such as getting to a location across the country or deceiving another NPC.
Complicated goals get broken down into smaller subgoals, and
once the best is chosen, others are pruned from the tree.
One of the key components to the action evaluation system is determining
the goals/actions needed to get from the current situation to the desired one,
(desired situation usually being spit out by a maslows evaluation).
'''
class GoalEngine():
    def __init__(self):
        pass