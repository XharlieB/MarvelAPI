import requests

hash="2fa946bf0abb6d21d4b86f59a52ddde1"
publicKey="c3ecdc5724cd07faccd58b04fc493c91"
privateKey="c12c5b36a8d0f7ce7d26b1bd5f84d9e6029a5e31"
url="http://gateway.marvel.com/v1/public/characters"
ts='1'
parameters = {"ts":ts,"apikey":publicKey ,"hash":hash ,'limit':100}

def ObtenerPersonajes():
    resultado = requests.get(url,params=parameters)
    diccionario = resultado.json()
    item = diccionario['data']['results']
    for personaje in item:
        print(personaje['name']+' y su uri es '+personaje['resourceURI']+' y su id es '+str(personaje['id']))



ObtenerPersonajes()
