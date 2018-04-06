import json
import os

dictionary = {}
PATH =  os.getcwd()
FILENAME = 'Dictionary_JSON_DUMP.json'


def createMapFromJSONData(file):
    global dictionary
    print file
    file1 = open(file)
    dictionary = json.loads(file1.read());
    print dictionary["a"]

def getWordPreProcess(word):
    global dictionary
    word = fetchLastWord(word)
    subDict = dictionary.copy()
    copySubWord = "";
    if(len(word)>0):
        for i in range(len(word)):
            letter  = word[i]
            letter = letter.lower();
            if(subDict[letter]):
                copySubWord = word[i]
                subDict = subDict[letter]
            else:
                break
    list = []
    list= getWord(list=list, levels=0, word=copySubWord, dict=subDict)
    print list

def getWord(list, levels, word, dict):
    smallestLength = getSmallestWordInList(list)
    if (levels > smallestLength):
        return list;

    checkNRemoveWordFromList(list)
    for i in dict.keys():
        newWord = word + i
        dict[i].getWord(list, levels + 1, newWord)

    return list;


def getSmallestWordInList(list):
    if (len(list) < 4):
        return 100
    else:
        list.sort()
        list.sort(key=len)
        return len(list[len(list) - 1])


def checkNRemoveWordFromList(list):
    list.sort()
    list.sort(key=len)
    if (len(list > 4)):
        list = list[:4]

def fetchLastWord(line):
    index = len(line)-1
    while(index>-1):
        if(not str[index].isalpha()):
            break
        index -=1
    word = line[index+1:]
    return word

createMapFromJSONData(PATH+"/"+FILENAME)
# print dictionary


# while True:
#     str = raw_input("Enter a character -->  ")
#     getWordPreProcess(str)

