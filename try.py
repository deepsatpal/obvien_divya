from bs4 import BeautifulSoup
import requests
from nltk.corpus import wordnet
from nltk.stem import  WordNetLemmatizer
from urllib.request import urlopen 

search_str = "CEO"

lemma = WordNetLemmatizer()

var = f"https://en.wikipedia.org/wiki/Lisa_Su"
webp= urlopen(var).read()

r = requests.get(var)

Wiki_Url = {}
search_type_wiki = {}
get_title = {}
title_lis = []
title_val = []
checkvalid = {}
many_res = {}
invalid_results ={}
synonyms_search = []




if r.status_code == 200:
	print(var)
	soup = BeautifulSoup(r.text  , 'html.parser')
	r.encoding = "utf-8"
	checkvalid['Check'] = soup.select(".infobox")
	for k ,  v in checkvalid.items():
		if v != [ ]:
			search_type_wiki['label']= soup.select(".infobox-label")
			for label in search_type_wiki['label']:
					title_lis.append(label.get_text())
			search_type_wiki['Data'] = soup.select(".infobox-data")
			for i in search_type_wiki['Data']:
				title_val.append(i.get_text())
			Wiki_Url["wikipedia_url"]= var
			count = 0
			for i in title_lis:
				get_title[i] = title_val[count]
				count += 1
			for key , val in get_title.items():
				if key == "Title":
					check2= val.split(" ")
					for syn in wordnet.synsets(search_str):
						for l in syn.lemmas():
							synonyms_search.append([webp.find(l.name())])
					print(synonyms_search)

		else:
			print("INVALID HERE")
			many_res['check'] = soup.select(".mw-parser-output > ul > li")
			for res in many_res['check']:
				key = res.get_text()
				invalid_results[key] = key.split(' ')
			for i , j in invalid_results.items():
				for k in synonyms_search:
					if k in j:
						print("ok Here it works" , k)
					else:
						print("No it's not there" , k)

elif 400 <= r.status_code < 50:
	print(r.status_code , "NOT WORKING", var )      
else:
	print(r.status_code,  "NOT FOUND", var)









