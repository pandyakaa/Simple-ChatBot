from KMP import KMPmain
from regex import regexmain
from BM import BMmain
import random

def readData() :

    with open("question.txt") as f :
        x = f.readlines()
        quest = []
        for words in x :
            quest.append(words.strip())
    
    with open("answer.txt") as f :
        x = f.readlines()
        ans = []
        for words in x :
            ans.append(words.strip())
        

    mat = [ [] for i in range(len(x))]

    for i in range(len(x)) :
        mat[i].append(quest[i])
        mat[i].append(ans[i])

    return mat

def randomQuest(ask,res,method) :
    max = 0
    temp = random.randint(0,len(res)-1)
    arrq = []
    for i in range(len(res)) :
        if (method(ask,res[i][0]) > max ) :
            max = method(ask,res[i][0])
            arrq.append(i)
    
    print("Mungkin maksud Anda : ")
    if (len(arrq) != 0) :
        for i in range(len(arrq)) :
            if ( i < 3 ) :
                print(str(i+1) + ". " + res[arrq[i]][0])
    else :
        print(res[temp][0])

if __name__ == "__main__":

    res = readData()
    foundKMP = False
    foundBM = False
    foundregex = False
    ask = input()

    for i in range(len(res)) :
        if (KMPmain(ask,res[i][0]) > 50 and not(foundKMP)) :
            print(res[i][1])
            foundKMP = True
    
    if (not(foundKMP)) :
        randomQuest(ask,res,KMPmain)
    
    for i in range(len(res)) :
        if (BMmain(ask,res[i][0]) > 50 and not(foundBM)) :
            print(res[i][1])
            foundBM = True
    
    if (not(foundBM)) :
        randomQuest(ask,res,BMmain)
    
    for i in range(len(res)) :
        if (regexmain(ask,res[i][0]) and not(foundregex)) :
            print(res[i][1])
            foundregex = True
    
    if (not(foundregex)) :
        print("Regex Not Found")
    
