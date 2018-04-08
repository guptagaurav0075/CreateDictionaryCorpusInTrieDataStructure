import os;

PATH = os.getcwd();
FILE_NAME = "dict_copy.txt"
# PATH += "/"+FILE_NAME
print PATH

file = open(PATH+"/"+FILE_NAME, 'r');
content = file.readlines()
file.close();
# node = Node()
dict = {}


for wrd in content:
    wrd =  wrd.rstrip();
    wrd =wrd.lstrip();
    if(len(wrd)!=0):
        if(len(wrd) in dict.keys()):
            list = dict[len(wrd)]
            list.append(wrd)
        else:
            list = []
            list.append(wrd)
            dict[len(wrd)] = list

for i in dict.keys():
    print i," -> ", dict[i]

file = open(PATH+"/filtered_dictionary.txt", 'w+')
for i in dict.keys():
    list = dict[i]
    for wrd in list:
        file.write(wrd)
        file.write("\n")
file.close();