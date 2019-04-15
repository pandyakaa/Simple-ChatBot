# Program untuk string matching dengan menggunakan Boyer-Moore Algorithm
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary

NumberOfChar = 256
# Sebelum dijalankan, akan melakukan pre-processing dengan menyiapkan BM table
# Digunakan untuk mencari index terakhir dari char yang ada di pattern
def preBM(pat) :
    res = [-1] * NumberOfChar

    for i in range(len(pat)) :
        res[ord(pat[i])] = i
    
    return res

# Algoritma BM, memanfaatkan prekomputasi sebelumnya
def BM(pat,txt) :
    m = len(pat)
    n = len(txt)

    res = preBM(pat)

    s = 0
    found = False
    while(s <= n-m and not(found)): 
        j = m-1
  
        while (j>=0 and pat[j] == txt[s+j]) : 
            j = j - 1

        if (j<0): 
            found = True
        else: 
            s = s + max(1, j-res[ord(txt[s+j])]) 
    
    if (found) :
        return float(m/n*100)
    else :
        return 0

# Fungsi untuk menghitung substring yang sama antara pattern dengan text
def subsBM(pat,txt) :
    substring = ''
    i = 0
    temp = 0

    if (pat[len(pat)-1] != ' ') :
        pat = pat + ' '

    if (txt[len(txt)-1] != ' ') :
        txt = txt + ' '

    while ( i < len(pat) ) :
        if (pat[i] != ' ') :
            substring = substring + pat[i]
        else :
            if ( i != len(pat) - 1) :
                substring = substring + ' '
            if (BM(substring,txt) > 0) :
                temp = temp + len(substring)
            substring = ''
        i = i + 1

    final = float(temp/len(txt))*100

    return final

# Fungsi untuk generate stopwords
def generateStopWords(pat,txt) :
	# Ambil Stopword bawaan
	stop_factory = StopWordRemoverFactory().get_stop_words()
	more_stopwords = [' ?' , '?', ' .', '.' , ' ,' , ',']
	# Merge stopword
	data = stop_factory + more_stopwords

	dictionary = ArrayDictionary(data)
	str = StopWordRemover(dictionary)

	temppat = str.remove(pat)
	if (temppat == '' or temppat == None) :
		temppat = pat

	temptxt = str.remove(txt)
	if (temptxt == '' or temptxt == None) :
		temptxt = txt 

	return temppat,temptxt

# Fungsi yang akan dipanggil
def BMmain(pat,txt) :
    pat,txt = generateStopWords(pat,txt)
    if (BM(pat,txt) != 0) :
        return (BM(pat,txt))
    else :
        return (subsBM(pat,txt))