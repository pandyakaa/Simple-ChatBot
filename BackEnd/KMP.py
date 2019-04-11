# Program untuk striing matching dengan menggunakan algoritma KMP
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary

# Sebelum dijalankan, akan melakukan pre-processing dengan menyiapkan KMP Border Function
# Digunakan untuk mencari suffix yang juga prefix dari sebuah string
def preKMP(pat) :
    temp = 0

    res = [0] * len(pat)
    i = 1

    while ( i < len(pat) ) :
        if (pat[temp] == pat[i]) : 
            temp = temp + 1
            res[i] = temp
            i = i + 1
        else :
            if ( temp != 0 ) :
                temp = res[temp-1]
            else :
                res[i] = 0
                i = i + 1
    
    return res

# Algoritma KMP, memanfaatkan prekomputasi sebelumnya
def KMP(pat,txt) :

    m = len(pat)
    n = len(txt)

    res = preKMP(pat)

    i = 0
    j = 0

    while ( i < n ) :
        if (pat[j] == txt[i]) :
            i = i + 1
            j = j + 1

        if ( j == m ) :
            return float(m/n*100)

        elif i < n and pat[j] != txt[i]: 
            if ( j != 0 ) : 
                j = res[j-1] 
            else: 
                i = i + 1
    
    return 0

def subsKMP(pat,txt) :
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
            if (KMP(substring,txt) > 0) :
                temp = temp + len(substring)
            substring = ''
        i = i + 1

    final = float(temp/len(txt))*100

    return final
    
# Fungsi untuk generate stopwords
def generateStopWords(pat,txt) :
    # Ambil Stopword bawaan
    stop_factory = StopWordRemoverFactory().get_stop_words()
    more_stopwords = [' ?' , '?']
    # Merge stopword
    data = stop_factory + more_stopwords

    dictionary = ArrayDictionary(data)
    str = StopWordRemover(dictionary)

    return str.remove(pat),str.remove(txt)

# Main Programs
txt = "Apakah chatbot itu manusia ?"
pat = "Apakah chatbot ?"
pat,txt = generateStopWords(pat,txt)
print(max(KMP(pat,txt),subsKMP(pat,txt)))