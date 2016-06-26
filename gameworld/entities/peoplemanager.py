import resourcefetch as rf
import networkx as nx
import ast
from gameworld.entities.character import Character
from gameworld.entities.npcs.npc import NPC

class PeopleManager():
    def __init__(self,World):
        self.configfile = 'Data-Files\\peopleValues.txt'
        self.initialdata = 'Data-Files\\people.txt'
        self.SG = nx.DiGraph()
        self.npcs = dict()      # points npc node number to npc object
        self.npcnames = dict()  # points npc name string to an npc object

        with open(self.initialdata) as P:
            self.offsetMap = rf.buildOffsetMap('NPC',P)
            #builds a list of seek offsets in the file for all NPC labels

        self.npcConfig = []     # obtain first by calling _loadNPCConfig()

    def loadPerson(self, name):
        """
        gives a list of lines defining npc data of the named npc
        :param name:
        :return:
        """
        result = []
        with open(self.initialdata) as P:
            for i in self.offsetMap:
                P.seek(i,0)
                P.readline()    #reads the label line of the Offsetmap
                line = P.readline()     #line of data after the label
                if line == ''.join([name, '\n']): #if the line matches the name with the newline character
                    result.append(line)
                    result.append(rf.readBlock('NPC',P))
                    for i,v in enumerate(result):
                        result[i] = rf.sanitize(v)
                    return result
            else:
                print('unable to find person in ',self.initialdata)

    def loadNextPerson(self,filecontext):
        """
        Trying to use a generator here to allow one to grab blocks of npc data
        :param filecontext: file context
        :return:    a list of lines as strings with empty strings on the end I think
        """
        '''with open(self.initialdata) as P:
            while True:
                result = []
                data = rf.readBlock('NPC', P)

                for line in data:
                    line = rf.sanitize(line)
                    if line.startswith('#') or line == '':       # ignore comments in file
                        continue
                    result.append(line)

                yield result'''
        while True:
            result = []
            data = rf.readBlock('NPC', filecontext)
            if data == '':
                break
            for line in data:
                line = rf.sanitize(line)
                if line.startswith('#') or line == '':       # ignore comments in file
                    continue
                result.append(line)
            yield result

    def loadNPCConfig(self):
        """
        Grabs NPC instance variable names from the 'peopleValues.txt' file
        :return: None, but sets the self.npcConfig variable for later
        """
        with open(self.configfile) as C:
            data = rf.readBlock('', C)
        result = []
        for v in data:     # iterates over each entry in the list readblock returns
            if v.startswith('#'):       # ignore comments in file
                continue
            line = rf.sanitize(v)       # turns 'v' into 'line', removes newline characters
            if '=' in line:             # if there's an equals, it means theres a dictionary of possible values there
                line = line.split(' = ')    # remove the equals and its surrounding spaces
                line[1] = ast.literal_eval(line[1])     # turn the 2nd part of the line into a proper dictionary
            elif line.startswith('{'):                # if the line is a tuple
                line = line.strip('{}').split(', ')     # strip the parenthesis, turn line into a list of variable names
            elif '$' in line:             # if this variable corresponds to npc data in the form of several tuples
                pass                        #
            result.append(line)

        self.npcConfig = result

    def buildNPC(self,npcdata):
        """
        takes a list of lines of Npc data and turns them into an NPC object
        :param data: lines of '\n' sanitized data strings in a list
        :return:
        """
        # Create NPC and iterate over attr, var in zip(npcConfig, npcdata)
            # if attr has a $,
                # its multi entry dictionary based data
                # if attr is relationships,
                    # build relationships with desired values
            # if attr is a list of length 2 and 2nd entry is a dict
                # its a case/if situation converting the string in val to a number for the NPC.attr
            # if attr is a list,
                # val is a tuple of numbers matching variables in attr
            # if attr is a single string with no special characters
                # val is a basic value to be set
        N = self.addEmptyNPC(npcdata[0])
        for attr, val in zip(self.npcConfig,npcdata):
            if '$' in attr:     # if attr is one with val data that has multiple parts
                a = val.split('; ')     # split those into separate tuples
                for b in a:             # for each stringtuple entry
                    data = b.strip('()').split(',')     # strip parenthesis ant turn into a list of data
                    if attr == 'relationships$':        # if this is relationship data
                        if len(data) == 5:              # if all relationship parameters are present
                            self.addRelationship(N.name,data[0],(int(data[1]),int(data[2]),int(data[3])),data[4])
                        elif len(data) == 4:            # if name and ART but not label are present
                            self.addRelationship(N.name,data[0],(int(data[1]),int(data[2]),int(data[3])))
                        elif len(data) == 1:            # if only name is available
                            self.addRelationship(N.name,data[0])
                        else:                           # else print error report
                            print('you have problem. NPC ', N.name, 'is not loading relationship with ',data[0],' correctly. Probable malformed people.txt entry')
                    else:   # if not relationship data
                        N.__dict__[attr[:-1]][data[0]] = [int(i) for i in data[1:]]
                        # Grabs the attr name (minus the $), locates N.attr, which should be a dictionary
                        # inserts the data into N.attr at data[0] as ints (cause they were still strings of numbers)
            elif isinstance(attr,list):     # if attr is a list
                if isinstance(attr[1],dict) and len(attr) == 2:    # if 2nd entry in attr is a dict and attr has length2
                    # this is indicative of N.attr being a case statement
                    N.__setattr__(attr[0],attr[1][val]) # make N.attr[0] = number returned from using val as key in attr[1]
                else:   # if this is where the data is packed into tuples, but with distinct variable names
                    for a,b in zip(attr, val.strip('()').split(',')):
                        N.__setattr__(a, int(b))

            else:
                N.__setattr__(attr, val)

    def addEmptyNPC(self, _name):
        """
        Creates and registers an unintialized NPC object with the peoplemanager and the Social Graph
        :param _name:   name of new npc
        :return:    NPC object with that name, either the new one or an existing one
        """
        if _name not in self.npcnames.keys():   # If npc is not created yet
            _NPC = NPC(_name)                       # instantiate NPC
            n = len(self.SG.node)                   # determines next available node number
            _NPC.nodenumber = n                     # gives new npc the next available node number
            self.npcs[n] = _NPC                     # registers npc to that nodenumber within the peoplemanager
            self.npcnames[_NPC.name] = _NPC         # registers npc to its name within the peoplemanager
            self.SG.add_node(n, npc=_NPC)           # inserts a new node on the social graph, with attribute pointing to npc object
            return _NPC                             # return new npc
        else:                                   # If npc name is taken already
            return self.npcnames[_name]             # return that npc

    def addRelationship(self, _NPC1name, _NPC2name, _art=(0, 0, 0), _label=None):
        """
        Constructs edge between npc1 and npc2 in the social directed graph
        :param _NPC1name: source node, given as name
        :param _NPC2name: target node, given as name
        :param _art: 3tuple determining attitude, respect and trust
        :param _label: string for readability describing relationship
        :return: None
        """
        if _NPC1name not in self.npcnames.keys():
            NPC1 = self.addEmptyNPC(_NPC1name)
        else:
            NPC1 = self.npcnames[_NPC1name]
        if _NPC2name not in self.npcnames.keys():
            NPC2 = self.addEmptyNPC(_NPC2name)
        else:
            NPC2 = self.npcnames[_NPC2name]
        self.SG.add_edge(NPC1.nodenumber, NPC2.nodenumber, a=_art[0], r=_art[1], t=_art[2], label=_label)

    def _getperson(self, infoIn, desiredType):
        """
        private method for getting specific npc or pc data or objects from identifiers
        :param infoIn: object, nodenumber(int), or name(string)
        :param desiredType: 'o', 'i', 's'
        :return: data of desired type referencing the infoIn
        """
        if desiredType == 'i':
            if isinstance(infoIn,int):
                return infoIn
            elif isinstance(infoIn,str):
                return self.npcnames[infoIn].nodenumber
            elif isinstance(infoIn, Character):
                return infoIn.nodenumber
            else:
                raise TypeError
        elif desiredType == 's':
            if isinstance(infoIn,int):
                return self.npcs[infoIn].name
            elif isinstance(infoIn,str):
                return infoIn
            elif isinstance(infoIn, Character):
                return infoIn.name
            else:
                raise TypeError
        elif desiredType == 'o':
            if isinstance(infoIn,int):
                return self.npcs[infoIn]
            elif isinstance(infoIn,str):
                return self.npcnames[infoIn]
            elif isinstance(infoIn, Character):
                return infoIn
            else:
                raise TypeError
        else:
            print('you have problem', infoIn, desiredType)

    def lookupNodeNumber(self, _person):
        try:
            return self._getperson(_person,'i')
        except TypeError as E:
            print('you have problem')
            print(E)
            return 0

    def lookupName(self, _person):
        try:
            return self._getperson(_person,'s')
        except TypeError as E:
            print('you have problem')
            print(E)
            return ''

    def lookupObject(self, _person):
        try:
            return self._getperson(_person,'o')
        except TypeError as E:
            print('you have problem')
            print(E)
            return None

    def populateWorld(self):
        """
        Iterates while there is data coming from loadNextPerson
        :return:
        """
        with open(self.initialdata) as P:
            comments = self.loadNextPerson(P).__next__()
            for npcdata in self.loadNextPerson(P):
                if len(npcdata) == 0:
                    break
                self.buildNPC(npcdata)


            '''
            comments = self.loadNextPerson(P)   #returns nothing because comments at top of file before NPC label
            npcdata = self.loadNextPerson(P).__next__()
            print(npcdata)'''
        #
