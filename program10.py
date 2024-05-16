import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
stop_words = set(stopwords.words("english"))

txt= "Sukanya, Rajib and Naba are my good friends." \
    "sukanya is getting married next year"\
        "Marriage is a big step in one's life"\
     "It is both exciting and frightening"\
    "But friendship is a second bond between people"\
    "It is a special kind of bond between us."\
    "Many of you must have tried searching for a friend"\
    "But never found the right one."
    
tokenized=sent_tokenize(txt)

for i in tokenized:
    wordlist = nltk.word_tokenize(i)
    wordlist =[w for w in wordlist if not w in stop_words]
    tagged = nltk.pos_tag(wordlist)
    
    print(tagged)