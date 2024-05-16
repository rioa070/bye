
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
sentence = "Hi,My name is Aman & hope you likr my work. You can follow me on instagram for more resources my username is 'the.cleaver.programmer.'"
print(sent_tokenize(sentence))
from nltk.tokenize import TreebankWordTokenizer
word_token = TreebankWordTokenizer()

print(word_token.tokenize(sentence))

