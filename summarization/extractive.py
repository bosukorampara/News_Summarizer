import nltk
from nltk.tokenize import sent_tokenize
from heapq import nlargest

nltk.download('punkt')

def summarize_extractive(text, num_sentences=2):
    sentences = sent_tokenize(text)
    if len(sentences) <= num_sentences:
        return text
    return ' '.join(nlargest(num_sentences, sentences, key=len))