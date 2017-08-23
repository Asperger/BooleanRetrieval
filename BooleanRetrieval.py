import os, sys
table = [[],[]]
filelist = []
f = open(os.path.join(sys.path[0],'StopwordList.txt'), 'r')
StopwordList = f.read().split()
f.close()
f = open(os.path.join(sys.path[0],'SuffixList.txt'), 'r')
SuffixList = f.read().split()
f.close()

def NOT(boollist):
    newlist = []
    for boolean in boollist:
        newlist.append(not boolean)
    return newlist
        
def AND(list1, list2):
    newlist = []
    assert list1.len() == list2.len()
    for i in range(list1.len()):
        newlist[i] = list1[i] and list2[i]
    return newlist

def OR(list1, list2):
    newlist = []
    assert list1.len() == list2.len()
    for i in range(list1.len()):
        newlist[i] = list1[i] or list2[i]
    return newlist
    
def XOR(list1, list2):
    newlist = []
    assert list1.len() == list2.len()
    for i in range(list1.len()):
        newlist[i] = list1[i] != list2[i]
    return newlist

# stem word and filter stopword
def Stemmer(word):
    lower_word = word.lower()
    if (lower_word in StopwordList):
        return ""
    else:
        for suffix in SuffixList:
            end = lower_word.rfind(suffix)
            if (end != -1):
                lower_word = lower_word[0:end]
        return lower_word

# word = the keyword
def FindIndex(word):
    for index, item in enumerate(table[0]):
        if (item == word):
            return index
    return -1

# listname = the name of the file with all the file names of articles
def BuildTable(listname):
    listf = open(os.path.join(sys.path[0],listname), 'r')
    filelist = listf.read().split()
    listf.close()
    for fileindex, filename in enumerate(filelist):
        docf = open(os.path.join(sys.path[0],filename), 'r')
        Document = docf.read().split()
        docf.close()
        for word in Document:
            word = Stemmer(word)
            if (word != ""):
                index = FindIndex(word)
                if (index == -1):
                    table[0].append(word)
                    table[1].append([0] * filelist.len())
                    table[1][table[1].len()-1][fileindex] = 1
                else:
                    table[1][index][fileindex] = 1

# word = the keyword you want
# return the query result of all the articles w/o the keyword
def SearchDocument(word):
    word = Stemmer(word)
    if (word != ""):
        index = FindIndex(word)
        if (index == -1):
            return [0] * filelist.len()
        else:
            return table[1][index]

# boollist = a list with the same format as table[1][index]
# return a list with the file names
def RetrieveDocument(boollist):
    Documentlist = []
    for index, boolean in enumerate(boollist):
        if (boolean):
            Documentlist.append(filelist[index])
    return Documentlist