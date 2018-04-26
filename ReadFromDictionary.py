dictionary = {}
list = []
def setDictionary(dic):
    global dictionary
    dictionary = dic.copy()

def getWordPreProcess(word):
    global dictionary, list
    word = fetchLastWord(word)
    subDict = dictionary.copy()
    copySubWord = "";
    if(len(word)>0):
        for i in range(len(word)):
            letter  = word[i]
            letter = letter.lower();
            if(letter in subDict.keys()):
                copySubWord += word[i]
                subDict = subDict[letter]
            else:
                break
    list = []
    if(len(subDict)<1):
        print "None"
        return;
    getWord(levels=0, word=copySubWord, dict=subDict)
    checkNRemoveWordFromList()
    print list

def getWord(levels, word, dict):
    global list
    if("isLeaf" in dict.keys()):
        if(dict["isLeaf"] and levels>0):
            list.append(word)
        # print word
    if(levels>4):
        return;

    for i in dict.keys():
        if (i is "isLeaf"):
            continue

        smallestLength = getSmallestWordInList()
        if (levels > smallestLength):
            return;
        newWord = word + i
        getWord(levels + 1, newWord, dict[i])
    return;

def getSmallestWordInList():
    global list
    if (len(list) < 5):
        return 10
    else:
        checkNRemoveWordFromList()
        list.sort()
        list.sort(key=len)
        return len(list[len(list) - 1])


def checkNRemoveWordFromList():
    global list
    if (len(list) > 4):
        list.sort()
        list.sort(key=len)
        list = list[:4]

def fetchLastWord(str):
    index = len(str) - 1
    while(index>-1):
        if(not str[index].isalpha()):
            break
        index -=1
    word = str[index + 1:]
    return word


