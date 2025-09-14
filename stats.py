def get_num_words(text):
    splitText = text.split()
    return f'{len(splitText)} words found in the document'

def freqCounter(text):
    map = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in map:
            map[lower_char] += 1
        else:
            map[lower_char] = 1
    return map
    # map = {}
    # for i in range(0, len(text)):
    #     # char = map.get(text[i]).lower(
    #     char = map[text[i]].lower()
    #     if char is None: char = 1
    #     else: char += 1
    # return map

def countDict(dict):
    dictList = []
    # put the dict in a list
    # first key is char and currKey 
    #

    for i in dict.keys():
        d = {}
        d['char'] = i
        d['num'] = dict[i]
        dictList.append(d)
    # print(dictList)

    dictList.sort(reverse=True, key=getDictKey)
    return dictList
# testDict = {"char": "b", "num": 4868}

def getDictKey(dict):
    return dict['num']