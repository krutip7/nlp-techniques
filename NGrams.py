# https://medium.com/swlh/language-modelling-with-nltk-20eac7e70853

from nltk import bigrams, word_tokenize
from collections import defaultdict

with open('corpus.txt', 'r', encoding='utf8') as f:
    corpus = f.read()

model = defaultdict(lambda: defaultdict(lambda: 0))

generateBigrams = lambda text: bigrams(word_tokenize(text),
                                       pad_left=True, left_pad_symbol='<s>',
                                       pad_right=True, right_pad_symbol='</s>')

# Count frequency of co-occurrence
for sentence in corpus.split('\n'):
    for w1, w2 in generateBigrams(sentence):
        model[w1][w2] += 1


# Transform counts to probabilities
for w1 in model:
    total_count = float(sum(model[w1].values()))
    for w2 in model[w1]:
        model[w1][w2] /= total_count

# Probability of a sentence
sentence = input("\nText: ")
print()
probability = 1
for w1, w2 in generateBigrams(sentence):
    probability *= model[w1][w2]
    print(w1, w2, '\t\t\t', model[w1][w2])

print("\nProbability of the entered text is ", probability)
print("Corpus used: 1st chapter of Alice in Wonderland")
