from gameworld.goals.goal import Goal


class GetInformation(Goal): #TODO convert to keyword arguments?
    def __init__(self,_info,_location,_item,_event,_person,_leads):
        self.event = _event
        self.info = _info
        self.person = _person
        self.leads = _leads
        self.location = _location
        self.item = _item