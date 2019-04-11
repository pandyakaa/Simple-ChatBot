# Program untuk striing matching dengan menggunakan algoritma KMP
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary

# Sebelum dijalankan, akan melakukan pre-processing dengan menyiapkan KMP Border Function
# Digunakan untuk mencari suffix yang juga prefix dari sebuah string
def KMPsp(pat) :
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

    res = KMPsp(pat)

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

# Fungsi untuk generate stopwords
def generateStopWords(pat,txt) :
    # Ambil Stopword bawaan
    stop_factory = StopWordRemoverFactory().get_stop_words()
    more_stopword = ['?']
    
    # Merge stopword
    data = stop_factory + more_stopword
    
    dictionary = ArrayDictionary(data)
    str = StopWordRemover(dictionary)

    return str.remove(pat),str.remove(txt)

# Main Programs
txt = "Apa ibukota negara Filipina?"
pat = "Apa ibukota Filipina?"
pat,txt = generateStopWords(pat,txt)
print(KMP(pat,txt))