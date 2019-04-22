from KMP import KMPmain
from regex import regexmain
from BM import BMmain
import random
import json

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

# Digunakan untuk load JSON yang berisi sinonim
def loadJSON():	
	with open('dict.json') as data_file:
		data = json.load(data_file)

	return data

# Digunakan untuk mendapatkan apakah sinonim ada di database
def getSinonim(word,datasin):
	if word in datasin.keys():
		return datasin[word]
	else:
		return []

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
        
        return ("Mungkin maksud kamu = \n \n" + tempres[0] + "\n \n" + tempres[1] + "\n \n" + tempres[2])
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
    foundKMPsinon = False
    foundBM = False
    foundBMsinon = False
    foundregex = False
    foundregexsinon = False
    sinonim = loadJSON()

    if (method == 'KMP') :
        for i in range(len(res)) :
            if (KMPmain(pat,res[i][0]) > 90 and not(foundKMP)) :
                return (res[i][1])

        if (not(foundKMP)) :
            temp = pat.split(" ")
            for words  in temp :
                listsin = getSinonim(words,sinonim)
                if (len(listsin) != 0 ) :
                    for sinon in listsin :
                        for i in range(len(res)) :
                            tempp = pat
                            ask = tempp.replace(words,sinon)
                            if (KMPmain(ask,res[i][0]) > 90 and foundKMPsinon == False) :
                                return (res[i][1])
        
        if (not(foundKMPsinon)) :
            return randomQuest(pat,res,KMPmain)

    elif (method == 'BM') :
        for i in range(len(res)) :
            if (BMmain(pat,res[i][0]) > 90 and not(foundBM)) :
                return (res[i][1])
        
        if (not(foundBM)) :
            temp = pat.split(" ")
            for words  in temp :
                listsin = getSinonim(words,sinonim)
                if (len(listsin) != 0 ) :
                    for sinon in listsin :
                        for i in range(len(res)) :
                            tempp = pat
                            ask = tempp.replace(words,sinon)
                            if (BMmain(ask,res[i][0]) > 90 and foundBMsinon == False) :
                                return (res[i][1])
        
        if (not(foundBMsinon)) :
            return randomQuest(pat,res,BMmain)
    
    else :
        for i in range(len(res)) :
            if (regexmain(pat,res[i][0]) and not(foundregex)) :
                return (res[i][1])
        
        if (not(foundregex)) :
            temp = pat.split(" ")
            for words  in temp :
                listsin = getSinonim(words,sinonim)
                if (len(listsin) != 0 ) :
                    for sinon in listsin :
                        for i in range(len(res)) :
                            tempp = pat
                            ask = tempp.replace(words,sinon)
                            if (regexmain(ask,res[i][0]) == True and foundregexsinon == False) :
                                return (res[i][1])
        
        if (not(foundregexsinon)) :
            return randomQRegex(pat,res)