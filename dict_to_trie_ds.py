import os;
from ReadFromDictionary import *

PATH = os.getcwd();
FILE_NAME = "filtered_dictionary.txt"
# PATH += "/"+FILE_NAME
print PATH

dictionary = {}

file = open(PATH+"/"+FILE_NAME, 'r');
content = file.readlines()
file.close();
# node = Node()
dictionary = {}
def addWord(word, index, subDict):
    if(index == len(word)):
        subDict["isLeaf"] = True
        return
    newSubDict = {}
    letter = word[index]
    if(word[index] in subDict.keys()):
        newSubDict = subDict[letter]
    else:
        newSubDict["isLeaf"] = False
        subDict[letter] = newSubDict

    addWord(word, index+1, newSubDict)


for i in range(len(content)):
    currentWord = content[i].rstrip()
    # currentWord = currentWord.rstrip()
    if(len(currentWord)<1):
        continue
    # print content[i], "   ->",currentWord
    addWord(word=currentWord, index=0, subDict=dictionary)

# print dictionary
setDictionary(dictionary)
str = ""
while True:
    val = "Enter partial word -->  "+str
    str += raw_input(val)
    print str
    getWordPreProcess(str)


# updated_JSON_Dictionary = json.dumps(dict)
# file = open("Dictionary_JSON_DUMP.json","w+");
# json.dump(updated_JSON_Dictionary, file)
# file.close()
#
# print updated_JSON_Dictionary