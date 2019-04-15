from KMP import KMPmain
from regex import regexmain
from BM import BMmain
import random

# Digunakan untuk membaca file eksternal
# Sebagai representasi database pertanyaan dan jawaban
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

# Digunakan untuk me-return pertanyaan random
# Untuk algoritma KMP dan BM
def randomQuest(ask,res,method) :
    temp = random.randint(0,len(res)-1)
    arrq = []
    for i in range(len(res)) :
        if (method(ask,res[i][0]) > 30 ) :
            arrq.append(i)

    tempres = [" "," "," "]

    if (len(arrq) != 0) :
        for i in range(len(arrq)) :
            if ( i < 3 ) :
                tempres[i] = (str(i+1) + ". " + res[arrq[i]][0])
        
        return ("Mungkin maksud kamu = " + tempres[0] + " " + tempres[1] + " " + tempres[2])
    else : 
        return ("Mungkin maksud kamu = " + res[temp][0])

# Digunakan untuk me-return pertanyaan random
# Untuk algoritma regex
def randomQRegex(ask,res) :
    temp = random.randint(0,len(res)-1)
    return ("Mungkin maksud kamu = " + res[temp][0])

# Akan dipanggil untuk melakukan proses string matching dan pencarian jawaban
def askMain(pat,res,method) :

    foundKMP = False
    foundBM = False
    foundregex = False

    if (method == 'KMP') :
        for i in range(len(res)) :
            if (KMPmain(pat,res[i][0]) > 70 and not(foundKMP)) :
                return (res[i][1])

        if (not(foundKMP)) :
            return randomQuest(pat,res,KMPmain)
    
    elif (method == 'BM') :
        for i in range(len(res)) :
            if (BMmain(pat,res[i][0]) > 70 and not(foundBM)) :
                return (res[i][1])
        
        if (not(foundBM)) :
            return randomQuest(pat,res,BMmain)
    
    else :
        for i in range(len(res)) :
            if (regexmain(pat,res[i][0]) and not(foundregex)) :
                return (res[i][1])
        
        if (not(foundregex)) :
            return randomQRegex(pat,res)
    
