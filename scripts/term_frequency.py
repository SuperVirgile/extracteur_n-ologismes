import json
import glob, re
import pprint as pp
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
import string
import pickle
import operator
from langdetect import detect


with open("neologolist_filterd.txt", "rb") as fp:   # Unpickling
	neologolist = pickle.load(fp)



global_freq = {}

for filepath in sorted(glob.glob('corpusLQ/*.txt')): 
	print(filepath)

	f = open(filepath)
	text = f.read()

	mots = word_tokenize(text, language = "french")

	for w in mots:

		if w in neologolist:
			if w in global_freq:
				global_freq[w] +=1
			else:
				global_freq[w] = 1


	f.close()




with open('global_freq.json') as json_file:
    prev_neo = json.load(json_file)



prev_neo = sorted(prev_neo.items(), key=operator.itemgetter(1))
pp.pprint(prev_neo	)



