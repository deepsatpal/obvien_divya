# import requests

# url = "https://curp-renapo.p.rapidapi.com/v1/curp"

# payload = {
	# "paternal_surname": "BENITEZ",
	# "entity_birth": "MN",
	# "birthdate": "09/16/1988",
	# "names": "JUAN",
	# "sex": "H",
	# "mothers_maiden_name": "HERNANDEZ"
# }
# headers = {
	# "content-type": "application/json",
	# "X-RapidAPI-Key": "d845ed9377msh78dc49ec37cee65p1451d4jsna552c5892621",
	# "X-RapidAPI-Host": "curp-renapo.p.rapidapi.com"
# }

# response = requests.request("POST", url, json=payload, headers=headers)

# print(response.text)


import requests

url = "https://joj-web-search.p.rapidapi.com/"

querystring = {"query":"list of ceo's","limit":"10","related_keywords":"true"}

headers = {
	"X-RapidAPI-Key": "d845ed9377msh78dc49ec37cee65p1451d4jsna552c5892621",
	"X-RapidAPI-Host": "joj-web-search.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)