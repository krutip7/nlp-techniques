# https://spacy.io/usage/linguistic-features#dependency-parse

import spacy

nlp = spacy.load("en_core_web_sm")

text = input('\nText: ')
doc = nlp(text)

for chunk in doc.noun_chunks:
    print(f"Chunk: '{chunk.text}' | Root: <{chunk.root.text}> | Dependency: <{chunk.root.dep_}> | Head: <{chunk.root.head.text}>")
