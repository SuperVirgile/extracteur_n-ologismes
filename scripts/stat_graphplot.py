import json
import glob, re
import pprint as pp
import nltk
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt



stats = {}
neologo =  ['lgbt','trans', 'transexuelle','transsexuel', 'transsexuel', 'transsexualiste', 'transsexualisme', 'hétéronormativité', 'transsexualisation','transgenre', 'transgenres', 'queer', 'hétérosexisme','hétérocentrisme', 'lesbianisme', 'lgbt', 'lgbtq', 'pallocratie','intersexuel','intersexe', ' intersexué','intersexuées', 'hétéro-normatif', 'hétéro-normatifs', 'pharmacopornographique', 'biohommes', 'biohomme', 'biofemme', 'biofemmes', 'pharmakon', 'preciado', 'pornotopie', 'pornotopies', 'hétérotopie', 'lgbtqi+', 'lgbtqi']


for filepath in sorted(glob.glob('corpusLQ/*.txt')): 
	print(filepath)

	f = open(filepath)

	anneemois = filepath.split('-')[0]+ '/'+ filepath.split('-')[1]

	text = f.read()
	mots = word_tokenize(text, language = "french")
	mots = [x.lower() for x in mots]

	for w in mots:
		if w in neologo:
			if anneemois not in stats:
				stats[anneemois] =1
			else:
				stats[anneemois] +=1

	f.close()

pp.pprint(stats)

with open('psycho-lgbt.json', 'w') as outfile:
    json.dump(stats, outfile)


x = []
names = []
annees = []

for jour in stats:
	x.append(stats[jour])
	names.append(jour.split('Q/')[1])


plt.xticks(range(len(names)), names)
plt.xticks(fontsize=9, rotation=75)
plt.plot(x)
plt.show()


"""
with open('neologisme_real.json') as json_file:
    prev_neo = json.load(json_file)

x = []
names = []

for entry in prev_neo:
	x.append(len(prev_neo[entry]))

	names.append(entry.split('/')[1].split('_'))
	
#plt.xticks(range(len(names)), names)
#plt.xticks(fontsize=9, rotation=75)
plt.plot(x)
plt.show()
"""