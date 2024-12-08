sentence = input('\nText: ')

# Tokenization

from nltk.tokenize import word_tokenize

tokens = word_tokenize(sentence)

print('\nTokens: ', *list(f"<{token}>" for token in tokens))


# Stemming

from nltk.stem import PorterStemmer

ps = PorterStemmer()

for token in tokens:
    print(token, " : ", ps.stem(token))


# Lemmatization

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

for token in tokens:
    print(token, " : ", lemmatizer.lemmatize(token))


# Stop Word Removal
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
filtered_sentence = [w for w in tokens if w not in stop_words]
