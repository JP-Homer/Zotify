#backend.py

import json
from pip._vendor import requests

class SpotifyAPI:

    url_:str = ''
    tokn:str = ''

    def __init__(self, url, token) -> None:
        self.url_ = url
        self.tokn = token

    def authenticate(self):
        response = requests.get(url, headers={'Authorization': f'Bearer {token}'})

        resp = response.json()

        return resp

def get_users_playlists():
    url = "https://api.spotify.com/v1/me/playlists"
    return url

def get_token():
    token = 'BQCN-zPRU-lWXt5NBUO7RPqHzD8r8M49VKRs3CMoAlKYSmZUd1p8wW5lp9eiHfr7jdUhlf6DNu5BnkWU2Nsef6Qyb2k44g_3cuh7GDqSnTX-TpswIEPXOc5yuuJdxgC8_XFfOJbPAQPR483Gdo2VQG8kajxdw4BRKw'
    return token

url = get_users_playlists()
token = get_token()

spotify = SpotifyAPI(url, token)

print(spotify.authenticate()['items'])