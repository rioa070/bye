
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv(r"C:\Users\User\Downloads\Youtube04-Eminem.csv",encoding = "latin-1")
comment_words=""
stopwords = set(STOPWORDS)

for val in df.CONTENT:
    val = str(val)
    tokens = val.split()
    
    for i in range(len(tokens)):
        tokens =val.split()
        tokens[i]=tokens[i].lower()
        
comment_words +=" ".join(tokens) + " "

wordcloud=WordCloud(width=800,height=800,background_color = 'white',stopwords=stopwords,min_font_size=10).generate(comment_words)
plt.figure(figsize=(8,8),facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()