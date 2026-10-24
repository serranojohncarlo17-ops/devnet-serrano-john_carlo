import requests

url1 = 'https://pokeapi.co/api/v2/pokemon/lapras'

#demonstrate how to use the 'params' parameter:
x = requests.get(url1, params = {"height": 25})

#print the response (the content of the requested file):
print(x.text)

#the file 'demopage.php' looks for a 'model' query string and prints its value.
