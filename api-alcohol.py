import requests

API_URL = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?{}={}'

def drink_search(drink, method = 's', results=1):
	# drink = input('Ingresa la bebida chorborra: \n')
	resp = requests.get(API_URL.format(method, drink.lower()))
	resp = resp.json()
	elem = resp['drinks']
	avoid = ['strInstructionsDE', 'strDrinkThumb', 'idDrink']
	drinks_found = [{k:v for k,v in i.items() if k not in avoid and v} for i in elem]
	return drinks_found
# print([k for k in primer_elem])
# print([k for k in primer_elem.values()])

drink = input("Ingresa la bebida que estas buscando \n")
num_de_resultados =int(input("cuantos resultados queres?\n"))
response = drink_search(drink, results=num_de_resultados)
for i in range(num_de_resultados):
	print(response[i])