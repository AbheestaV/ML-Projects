"""
Write a program that reads in a text file and performs the following actions –

    Create a file with some text (about 2 paragraphs long)
    Read in your text
    Tokenise the text
    Optional - Create a new list containing all the words that are more than 4 characters long.
    Tag text with part of speech tags
    Create a list containing all the nouns in the text
    Tag all the named entities such as names of people and places
    Find all words in your text that end with ed, ing or s
    Save output of one of the above functions to a new file

"""
# %%

import nltk
import re
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# %%
with open(r'Lab5text.txt', "r") as f:
    data = f.read()
print(data)

# %%

tokens = nltk.word_tokenize(data)
print(tokens)

#  %%

four_letters = []
for word in tokens:
    if len(word) >= 4:
        four_letters.append(word)
print(four_letters)

# %%
speech_char = nltk.pos_tag(tokens)
print(speech_char[:10])

# %%

nouns = []

for word, tag in speech_char:
    if tag in ['NN', 'NNS']:
        nouns.append(word)
print(nouns)

# %%

entities = nltk.ne_chunk(speech_char)
print(entities)

# %%

for word in tokens:
    if re.search(r'(ed|ing|s)$', word):
        print(word)

# %%
with open('lab5output.txt', 'w') as f:
    f.write(str(entities))