import requests
import os
import json

path = "D:/Namizje/penguinz0/"
TCGPLAYER_API_URL = 'https://api.tcgplayer.com'
TCGPLAYER_API_VERSION = 'v1.39.0'
URL = TCGPLAYER_API_URL + '/' + TCGPLAYER_API_VERSION
f = open(path + "token.txt", "r")
TCGPLAYER_ACCESS_TOKEN = f.readline()

def new_access_token():
    f = open(path + "keys.txt", "r")
    TCGPLAYER_PUBLIC_KEY, TCGPLAYER_PRIVATE_KEY = f.read().split("\n")
    payload = {
    'grant_type': 'client_credentials',
    'client_id': TCGPLAYER_PUBLIC_KEY,
    'client_secret': TCGPLAYER_PRIVATE_KEY,
    }
    r = requests.post(
    TCGPLAYER_API_URL + '/token',
    data=payload,
    )
    assert r.status_code == 200
    token_response_data = r.json()
    access_token = token_response_data['token_type'] + ' ' + token_response_data['access_token']
    
    f = open(path + "token.txt", "r+")  
    f.seek(0)  
    f.truncate()
    f.write(access_token)

#new_access_token()
r = requests.get(f'{URL}/catalog/products', headers={'Authorization': f'{TCGPLAYER_ACCESS_TOKEN}'})
r = r.json()
print(r)

#stop
#r = requests.get(f'{URL}/catalog/caragories/{2}', headers={'Authorization': f'{TCGPLAYER_ACCESS_TOKEN}'})
#print(r.json)
