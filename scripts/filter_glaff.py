import json
import glob, re
import pprint as pp
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
import pickle

#CODE POUR FILTRER LES NEOLOGISMES CANDIDATS AVEC LE GLAFF

with open("glaff_reduced.txt", "rb") as fp:   # Unpickling
	glaff = pickle.load(fp)


with open('neologisme_raw.json') as json_file:
    prev_neo = json.load(json_file)



neologisme_new = {}


for entry in prev_neo:

	neologisme_new[entry] = []
	print(entry)
	for w in prev_neo[entry]:
		if not w in glaff:
			neologisme_new[entry].append(w)


pp.pprint(neologisme_new)

with open('neologisme_new.json', 'w') as outfile:
    json.dump(neologisme_new, outfile)
