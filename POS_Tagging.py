import nltk

sentence = input('\nText: ')

tokens = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(tokens)

print('\nPOS Tags:', *list(f"<{word}, {tag}>" for word, tag in tags))
