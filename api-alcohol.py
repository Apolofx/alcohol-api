import requests


API_URL = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?{}={}'

def drink_search(drink, method = 's', results=1):
	# drink = input('Ingresa la bebida chorborra: \n')
	results_len = results - 1 #for use in array index format
	resp = requests.get(API_URL.format(method, drink.lower()))
	resp = resp.json()
	elem = resp['drinks']
	avoid = ['strInstructionsDE', 'strDrinkThumb', 'idDrink']
	drinks_found = [{k:v for k,v in i.items() if k not in avoid and v} for i in elem]
	print(drinks_found[results_len])
# print([k for k in primer_elem])
# print([k for k in primer_elem.values()])

drink_search('tequila')