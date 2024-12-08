# https://spacy.io/usage/linguistic-features#named-entities

import spacy

nlp = spacy.load("en_core_web_sm")

text = input('\nText: ')
doc = nlp(text)

for ent in doc.ents:
    print(f"{ent.text} <{ent.label_}> at position ({ent.start_char}, {ent.end_char})")
