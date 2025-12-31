import nltk
from nltk.corpus import stopwords
from collections import Counter
import string

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return [w for w in words if w not in stop_words]

def most_common_words(reviews, top_n=10):
    all_words = []
    for review in reviews:
        all_words.extend(clean_text(review))
    return Counter(all_words).most_common(top_n)
