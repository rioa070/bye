import nltk
from nltk.stem.snowball import SnowballStemmer

show_stemmer = SnowballStemmer(language="english")

words=['cared','university','fairly','easily','singing','sings','sung','singer','sportingly']

stem_words=[]

for w in words:
    x=show_stemmer.stem(w)
    stem_words.append(x)
    
    
for e1,e2 in zip(words,stem_words):
    print(e1+'--->' +e2)