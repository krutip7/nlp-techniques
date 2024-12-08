# https://spacy.io/usage/linguistic-features#lemmatization

import spacy

nlp = spacy.load("en_core_web_sm")


text = input('\nText: ')
doc = nlp(text)

for token in doc:
    print(f"<{token}>\t {token.morph}")
