import json
import glob, re
import pprint as pp
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
import string

def enlever_nombres(texte):
    texte = re.sub("[0-9\.]*", "", texte)
    texte = re.sub('[«•»←“”…€?°/+~‘=@#]', '', texte)
    texte = re.sub('http\S+', '', texte)
    texte = re.sub('https\S+', '', texte)
    texte = re.sub('www.\S+', '', texte)

    return texte.lower()

def cleanWord(word):
    if ('https' in word) or ('www.' in word) or ('http' in word):
        word = 'url'
    return word


def get_vocabulaire(texte):
    global get_vocabulaire

    texte = enlever_nombres(texte)
    mots = word_tokenize(texte, language = "french")
    set_mots = set(mots)
    dejavu = set(vocabulaire).intersection(set_mots)
    nouveau = set_mots.difference(vocabulaire)
    for x in set_mots:
        vocabulaire.append(cleanWord(x))

    return vocabulaire, dejavu, nouveau


vocabulaire = []
neoglogisme = {}

for filepath in sorted(glob.glob('corpusLQ/*.txt')): 
	print(filepath)

	f = open(filepath)
	text = f.read()

	vocabulaire, dejavu, nouveau = get_vocabulaire(text)

	neoglogisme[filepath] = list(nouveau)
	f.close()



pp.pprint(neoglogisme)

with open('neologisme_raw.json', 'w') as outfile:
    json.dump(neoglogisme, outfile)







