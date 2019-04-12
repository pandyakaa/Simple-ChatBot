import re
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary

# Fungsi untuk string matching dengan menggunakan regex
def regex(pat,txt) :
    x = re.search(pat,txt,flags=re.IGNORECASE)

    if ( x != None ) :
        print(x.group())

# Fungsi untuk generate stopwords
def generateStopWords(pat,txt) :
    # Ambil Stopword bawaan
    stop_factory = StopWordRemoverFactory().get_stop_words()
    more_stopwords = [' ?' , '?', ' .', '.' , ' ,' , ',']
    # Merge stopword
    data = stop_factory + more_stopwords

    dictionary = ArrayDictionary(data)
    str = StopWordRemover(dictionary)

    return str.remove(pat),str.remove(txt)

# Main Programs
if __name__ == "__main__":
        txt = "Apa ibukota negara Filipina?"
        pat = "Apa ibukota Filipina ?"
        pat,txt = generateStopWords(pat,txt)
        regex(pat,txt)