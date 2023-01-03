import requests
from lxml import html
import re
import time
from bs4 import BeautifulSoup as bs
import urllib
from urllib.request import urlretrieve
import json
import pprint as pp
import time as theTime
import json
from tika import parser	
import os

def isError(title):
	if "português" in title:
		return True
	if "n°118" in title:
		return True
	if "version bilingue" in title:
		return True

	return False

def writeError(href):
	with open('errors.txt', 'a') as fp:
		fp.write(href)
		fp.write('\n')
	fp.close()


def writePDF(pdfhref,fname):
	urlretrieve(pdfhref, "temp.pdf")
	#treat pdf
	raw = parser.from_file('temp.pdf')
	path = 'corpusLQ/' + fname + '.txt'

	with open(path, 'w') as fp:
		fp.write(raw['content'])
	fp.close()

	os.remove("temp.pdf") 

	print('wrote '+ fname)


def writeARTICLE(article,fname):

	path = 'corpusLQ/' + fname + '.txt'

	with open(path, 'w') as fp:
		fp.write(article)
	fp.close()

	print('wrote '+ fname)


def scrap_page(articles_div):
	global ID

	for titre in articles_div:

		spandate =  titre.findAll('span', {'class': "date time published"})[0]["title"]
		fname = spandate.split('T')[0] + '_'+str(ID)
		#print(fname)
		ID +=1

		ahref = titre.find_all('a', href=True)
		
		href = ahref[2]
		title = ahref[0]['title']

		if isError(title):
			continue

		try:
			if "Lacan Quotidien n°" in title:

				ahref = titre.find(lambda tag:tag.name=="a" and "LQ" in tag.text)
				pdfurl = ahref['href']

				print(pdfurl)
				writePDF(pdfurl,fname)
			else:

				articleURL = ahref[0]['href']
				print(articleURL)
				page2 = requests.get(articleURL.strip())
				soup2 = bs(page2.content, features="lxml")

				article =  soup2.find('div', {'class': "entry_wrap fix"}).text

				writeARTICLE(article,fname)
		except:
			print("\nERROR AT " + str(href) + "\n")
			writeError(str(href))
			continue


def scrap_by_date(url):

	pagination = True
	while pagination:
		print(url)

		page = requests.get(url.strip())
		soup = bs(page.content, features="lxml")
		
		articles_div = soup.findAll('div', {'class': "post-meta fix"})
		scrap_page(articles_div)

		try:
			prevURL = soup.findAll('div', {'id': "pagination"})

			prevahref = prevURL[0].find_all('a', href=True)
			href = prevahref[0]['href']

			if "Previous Entries" not in prevahref[0].text:
				pagination = False

			url = href
		except:
			pagination = False


ID = 0
baseurl = 'https://www.lacanquotidien.fr/blog/'

year = 2011

for i in range(9):

	print('\n'+str(year)+'\n')

	newurl = baseurl + str(year)
	scrap_by_date(newurl)

	print('\n'+str(year)+' FINISHED\n')

	year+=1



