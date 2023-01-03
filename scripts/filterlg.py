import json
import glob, re
import pprint as pp
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
import pickle
from langdetect import detect


with open('neologisme_new.json') as json_file:
    prev_neo = json.load(json_file)

entries2del = ['pédopsychiatrie', 'comportementalistes', 'comportementaliste', 'post-traumatique', 'médico-social', 'neuroscientifique', 'neuroscientifiques', 'neuro', 'comportementaliste', 'psychodynamique', 'neuroscience' 'psychodynamiques', 'psycho-dynamique', 'cognitivo-comportementale','cognitivo-comportementales', 'cognitivo-comportementalisme' ,'psychopathologique', 'psychopathologie', 'neuro-paradigme', 'autisme', 'autiste', 'autistes', 'psychologisme', 'neurogénétique', 'neurogénétiques', 'neuropédiatre', 'neurotypique', 'neurotypiques', 'neurogenèse', 'neurogenèses', 'psychosociales', 'psychosociaux','pharmacologiques', 'médico-psychologique','neurodéveloppement','neuro-développemental', 'pédiatre', 'neurobiologiques', 'neurobiologique', 'physico-chimique', 'psychosystème', 'psychomécanique', 'psychosémiologique']

for entry in prev_neo:
	print(entry)

	nonfr = 0

	for w in prev_neo[entry]:
		try:
			if detect(w) != 'fr':
				nonfr+=1
		except:
			continue

	if nonfr >= 50:
		print(prev_neo[entry])
		entries2del.append(entry)


for entry in entries2del:
	del prev_neo[entry]


with open('neologisme_real.json', 'w') as outfile:
    json.dump(prev_neo, outfile)





