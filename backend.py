#backend.py

import json
from pip._vendor import requests

class SpotifyAPI:
    url = ''
    token = ''
    playlist_id = ''

    def __init__(self) -> None:
        pass

    def get_response(self):
        response = requests.get(self.url, headers={'Authorization': f'Bearer {self.token}'})

        resp = response.json()

        return resp

    def get_users_playlist_id(self):
        self.url = "https://api.spotify.com/v1/me/playlists"
        playlist_id = self.get_response()['items'][0]['uri']
        playlist_id = playlist_id[playlist_id.find('spotify:playlist:') + 17:]
        self.playlist_id = playlist_id
        return playlist_id

    def set_token(self):
        self.token = 'BQCN-zPRU-lWXt5NBUO7RPqHzD8r8M49VKRs3CMoAlKYSmZUd1p8wW5lp9eiHfr7jdUhlf6DNu5BnkWU2Nsef6Qyb2k44g_3cuh7GDqSnTX-TpswIEPXOc5yuuJdxgC8_XFfOJbPAQPR483Gdo2VQG8kajxdw4BRKw'

    def get_playlist_songs(self):
        self.url = f'https://api.spotify.com/v1/playlists/{self.playlist_id}/tracks'
        songs = []
        for index in range(1,11):
            songs.append(self.get_response()['items'][index]['track']['name'])
        return songs


spotify = SpotifyAPI()
token = spotify.set_token()
playlist_id = spotify.get_users_playlist_id()
songs = spotify.get_playlist_songs()
print(songs)