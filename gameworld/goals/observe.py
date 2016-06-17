from gameworld.goals.goal import Goal

#is basically a combo of be at location and getinfo goals with a
#  perception filter
class Observe(Goal):
    def __init__(self,_location,_time,_info):
        self.location = _location
        self.time = _time       #Time object. If 0, no time limit specified
        self.info = _info


