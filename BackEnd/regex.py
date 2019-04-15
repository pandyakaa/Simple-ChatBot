import re
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary

# Fungsi untuk string matching dengan menggunakan regex
def regex(pat,txt) :
	x = re.search(pat,txt,flags=re.IGNORECASE)
	if ( x != None) :
			return True
	else :
			return False

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

# Fungsi untuk melakukan pengecekan setiap katanya
def subsregex(pat,txt) :
	x = re.split(" ",pat)
	count = 0
	for words in x :
		if (regex(words,txt)) :
			count = count + 1
	if (count == len(x)) :
		return True
	
	return False

# Fungsi yang akan dipanggil 
def regexmain(pat,txt) :
	if (regex(pat,txt)) :
		return True
	else :
		return (subsregex(pat,txt))