from collections import Counter
# in Tibetan its called Tsak
spliter = "་"
dataSet = ""
# unigram
def getEachWord(text):
    items = []
    text = text.split(spliter)
    return text


# bigram
def bigram(text):
    bgram = []
    text = getEachWord(text)
    combinedWord = ""
    for i in range(len(text)):
        if i + 1 < len(text):
            firstWord = text[i]
            secondWord = text[i + 1]
            # " " is equal to ་ in Tibetan language
            combinedWord = firstWord + " " + secondWord
            # print(combinedWord)
        bgram.insert(i, combinedWord)
    return bgram


def countWords():
    cnt = Counter()
    for word in getEachWord(dataSet):
        cnt[word] += 1
    return cnt


# word frequency
print("REQUENCY OF WORDS  : \n", countWords())


def getProbabilityOf(word):
    textarr = bigram(dataSet)
    wordAndGivenWordArr = Counter(textarr)
    cnt = countWords()
    print("######################")
    maxprob = 0
    predictedWord = ""
    for eachWord in getEachWord(dataSet):
        wordAndGivenWord = word + " " + eachWord
        # gives the count of A and B
        # print(wordAndGivenWordArr[wordAndGivenWord])
        # print(wordAndGivenWord)
        # gives the count of A
        # print(cnt[word])
        prob = (wordAndGivenWordArr[wordAndGivenWord]) / cnt[word]
        wordAndGivenWordprob = wordAndGivenWord + "  :" + str(prob)
        print(wordAndGivenWordprob)
        if maxprob < prob:
            maxprob = prob
            predictedWord = eachWord

    print("\n#####################\n")
    print("next word predicted  is ", predictedWord)
    print("\n#####################")


def getInput():
    inputWord = input("Enter a word in Tibetan language : ")
    getProbabilityOf(inputWord)


getInput()
