import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
set(stopwords.words('english'))

text = """He determined to stop his litigation with the monastry and relinguish his claims to the wood_cutting and fishery rights at once. He was the more ready to do this because the rights had became much less valuable, and he had indeed the vaguest idea where the wood and river in question. """

stop_words=set(stopwords.words("english"))

word_tokens=word_tokenize(text)
filtered_sentence=[]
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
        
print("\n\n Original Sentence \n\n")
print(" ".join(word_tokens))
print("\n\n Filtered Sentence \n\n")
print(" ".join(filtered_sentence))

