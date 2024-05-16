import nltk
nltk.download('brown')
from nltk.corpus import brown
cfd=nltk.ConditionalFreqDist(
    (genre,word)
    for genre in brown.categories()
    for word in brown.words(categories = genre))
    
categories = ["hobbies","romance","humor"]
searchwords = ["may","might","must","will"]

cfd.tabulate(conditions=categories, samples=searchwords)