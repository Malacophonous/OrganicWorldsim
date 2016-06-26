

def skipToLine(linenum,filecontext):
    filecontext.seek(0)
    for i in range(linenum):
        filecontext.readline()


def buildOffsetMap(label,filecontext):
    """
    creates list of known locations of label string in filecontext
    :param label: string that appears at the start of a new block of data
    :param filecontext: filestream like object
    :return: list of offsets used for skipping to locations in the file
    """
    result = []
    flag = True
    label = ''.join((label, '\n'))
    while flag:
        offset = filecontext.tell()
        line = filecontext.readline()
        if line == label:
            result.append(offset)
        if line == '':
            flag = False
    return result


def convert(tuplestring):
    # USE ast.literal_eval(string) for integer or numeric tuples
    # use this method for handling tuples of names that have no quotes
    return tuplestring.strip('()').split(', ')


def readBlock(endpoint, filecontext):    # be careful with large files
    """Read a number of lines of a TextIO stream.
    :param endpoint: stopping point of intended block. Pass int to read int lines, pass str to use str as a flag
    :param filecontext: the thing you use in the with statement, a context managar reference
    returns result -- a list of lines, in order, read from the file, terminating with theempty string
    """
    if isinstance(endpoint,str):
        endpoint = endpoint+'\n'#beware of local newline characters like \r or \r\n
        return _readblockStr(endpoint,filecontext)
    elif isinstance(endpoint,int):
        return _readblockInt(endpoint,filecontext)


def _readblockStr(endpoint,filecontext,includeOffset = False):
    result = []
    flag = True
    while flag:
        line = filecontext.readline()
        offset = filecontext.tell()
        if line == endpoint:
            flag = False
            result.append('')#add empty string to keep compatibility with readline()
        else:
            if includeOffset:
                result.append((line,offset))
            else:
                result.append(line)
            if line == '':
                flag = False
    return result


def _readblockInt(endpoint,filecontext, includeOffset = False):
    result = []
    flag = True
    while flag:
        line = filecontext.readline()
        offset = filecontext.tell()
        if len(result) == endpoint:
            flag = False
            result.append('')#add empty string to keep compatibility with readline()
        else:
            if includeOffset:
                result.append((line,offset))
            else:
                result.append(line)
            if line == '':
                flag = False
    return result


def sanitize(line):     #possible line endings: None, '', '\n', '\r', '\r\n'
    if line[-1:] == '\n':
        line = line[:-1]
    if line[-1:] == '\r':
        line = line[:-1]
    return line


def main():
    with open('a.txt') as A: #TextIOWrapper
        #for line in A:      #does not load entire file in memory, garbage collects each line after reading if no references are stored
        #    #do something with line
        #    print(line, A.tell())
        print(readBlock('a',A))
        print(A.tell())
        for entry in readBlock(6,A):
            print(sanitize(entry[0]))
            print(entry[1])

    '''with open('npcdata.txt') as test:
        linenum = 0
        locations = dict()
        for i,line in enumerate(test):
            if line[0:3] == 'NPC':
                locations[i] = int(line[3])
        skipToLine(6+1,test)
        print(test.readline())
    print(locations)'''


if __name__ == '__main__':
    main()
