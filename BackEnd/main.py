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

def randomQRegex(ask,res) :
    temp = random.randint(0,len(res)-1)
    print("Mungkin maksud Anda : ")
    print(res[temp][0])

def askMain(pat,res,method) :

    foundKMP = False
    foundBM = False
    foundregex = False

    if (method == 'KMP') :
        for i in range(len(res)) :
            if (KMPmain(pat,res[i][0]) > 50 and not(foundKMP)) :
                return (res[i][1])

        if (not(foundKMP)) :
            randomQuest(pat,res,KMPmain)
    
    elif (method == 'BM') :
        for i in range(len(res)) :
            if (BMmain(pat,res[i][0]) > 50 and not(foundBM)) :
                return (res[i][1])
        
        if (not(foundBM)) :
            randomQuest(pat,res,BMmain)
    
    else :
        for i in range(len(res)) :
            if (regexmain(pat,res[i][0]) and not(foundregex)) :
                return (res[i][1])
        
        if (not(foundregex)) :
            randomQRegex(pat,res)
    
