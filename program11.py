import spacy

def extract_noun_phrases(text):
    nlp=spacy.load("en_core_web_sm")
    dec=nlp(text)
    noun_phrases=[chunk.text for chunk in dec.noun_chunks]
    return noun_phrases

text = "The quick brown fox jumps over the lazy dog"

noun_phrases = extract_noun_phrases(text)

print("Noun Phrases: ",noun_phrases)