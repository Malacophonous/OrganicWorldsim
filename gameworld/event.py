# TODO: Questions for consideration:
# What is the level of significance to cause an event record
# How do you determine when an event has ended
# or for that matter, when it starts


class Event():
    def __init__(self, _location, _time, _observer, _wss1, _wss2):
        self.location = _location
        self.time = _time
        self.observer = _observer
        self.participants = []
        self.actionsByParticipants = dict()     #keyed to particpants' id, with values of SAI
        self.wss1 = _wss1
        self.wss2 = _wss2

    def compareSame(self,Event):    #True/False
        #Determines if two events are identical based on time and location
        pass

    def compareLocation(self,Event,distance = 0): #True/False
        #compare if events were within distance of each other,
        #otherwise if they were in the same place
        pass

    def compareTime(self,Event, timeElapsed = None):    #True/False
        #compare if events were within an amount of time of each other
        #Time elapsed should be a time object
        #otherwise compare if events occured at the same time
        pass

    def updateEvent(self,data):
        #updates information and incorporates it into this event log
        pass