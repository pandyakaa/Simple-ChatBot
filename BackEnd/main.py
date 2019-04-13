from KMP import KMPmain
from regex import regexmain
from BM import BMmain

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
        print("KMP Not Found")
    
    for i in range(len(res)) :
        if (BMmain(ask,res[i][0]) > 50 and not(foundBM)) :
            print(res[i][1])
            foundBM = True
    
    if (not(foundBM)) :
        print("BM Not Found")
    
    for i in range(len(res)) :
        if (regexmain(ask,res[i][0]) and not(foundregex)) :
            print(res[i][1])
            foundregex = True
    
    if (not(foundregex)) :
        print("Regex Not Found")
    
