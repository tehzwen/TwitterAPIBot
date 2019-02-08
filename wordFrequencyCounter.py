import re

def removePuncuation(stringData, userName):
    fixed = stringData.replace(",", "")
    fixed = fixed.replace('\"', "")
    fixed = re.sub(r'\.+', " ", fixed)

    commonWords = ["my", "me", "by", "he", "this", "that", "they", "have", "not", "in", "a", "of", "and", "be", "&amp",
    "on", "for", "will", "with", "is", "in", "to", "the", "so", "or", "just", "you", "been", "than", "only", "do", "from",
    "are", "i", "&amp;", "has", "it", "was", "we", "\"", "our", "all", "more", "now", "very", "at", "no", "yes", "after",
    "about", "but", "much", "their", "back", "up", "his", "her", "she", "want", "said", "these", "an", "rt", "am", "any",
    "who", "-", "go", "if", "what", "as", "two", "how", "like", "s" ]

    finalWordList = []
    wordList = fixed.split(" ")

    for word in wordList:
        word = word.lower()
        word = removeUnicodeQuotes(word)
        if (word[:4] != "http" and word != "" and word != " " and word.find("/") == -1 
            and word.find("@"+userName) == -1 and
             word not in commonWords):


            finalWordList.append(word)
        

    return ' '.join(finalWordList)


#receives a list (data) and counts the frequency of words in it
def countFrequency(data):
    wordDict = {}
    
    #go through each sentence in the list
    for stringVal in data:
        wordList = stringVal.split(" ")

        #go through each word in the string
        for word in wordList:
            
            #if the word exists in the dictionary already
            if (word in wordDict):
                tempVal = wordDict[word]
                tempVal += 1
                wordDict[word] = tempVal
            
            #word doesn't exist
            else:
                wordDict[word] = 1

    x = sorted(wordDict.items(), key=lambda x: x[1], reverse=True)
    return x


def removeUnicodeQuotes(stringVal):
    charList = []

    for i in range(len(stringVal)):
        if (ord(stringVal[i]) != 8220 and ord(stringVal[i]) != 8221):
            charList.append(stringVal[i])

    return ''.join(charList)

def test(stringData):
    removeUnicodeQuotes(stringData)

#test("“great”")

