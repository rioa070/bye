from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

porter_stemmer = PorterStemmer()

lists_of_lists = ["consult","consultant","consultancy","consultative","consults"]

for word in lists_of_lists:
    print(word," : ",porter_stemmer.stem(word))
    
    
    
    
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

porter_stemmer = PorterStemmer()

sentence="He visits consultancy to consuslt the consultant"
lists_of_lists=word_tokenize(sentence)

for word in lists_of_lists:
    print(word," : ",porter_stemmer.stem(word))
    
    
    
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from functools import reduce

ps=PorterStemmer()

sentence="Programmers program with programming language"

word = word_tokenize(sentence)
stemmed_sentence = reduce(lambda x,y:x+" "+ps.stem(y),word," ")
print(stemmed_sentence)
    