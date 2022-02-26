#api.py

from re import L
from pip._vendor import requests
import moods

#Protocol order: sign in, assign moods to types of music, create playlist, pull songs from their playlists, add to new playlist, return playlist

class SpotifyAPI:
    url = ''
    token = ''

    def __init__(self) -> None:
        pass

    
    def login(self):
        pass

    def set_url(self, url):
        self.url = url

    def set_token(self):
        self.token = 'BQBqI1odks4IfBGiN0QMyBwDtLN0WsDe8LpMZMj7MT1-y0ib-EjrsaM4Noevvtm2RgmfB9ktjPJi7RZSIWAViDXPD7lHDEisZTvig0AslxxCWr_XzMCu_3sj1xbS-QCzmq-ut4vDDBN67SFguBHq9gk5tTxEX_IcjA'

    def call_api(self):
        response = requests.get(self.url, headers={'Authorization': f'Bearer {self.token}'})
        response = response.json()

        return response

    def get_users_playlist_id(self, response):
        playlist_id = response['items'][0]['uri']
        playlist_id = playlist_id[playlist_id.find('spotify:playlist:') + 17:]
        self.playlist_id = playlist_id
        return playlist_id

    def get_playlist_songs(self, response):
        id = response['items'][0]['track']['id']
        return id

    def get_song_info(self, response, id):
        energy = response['energy']
        valence = response['valence']
        tempo = response['tempo']
        
        information = {id: {}}

        information[id]['energy'] = energy
        information[id]['valence'] = valence
        information[id]['tempo'] = tempo

        return information


# Creates Spotify API Instance
# Sets token
# Sets URL to get playlist id
# Calls API to receive json with information of all playlists
# Changes URL to get songs within playlist
# Calls API to receive json with information of songs within playlist

spotify = SpotifyAPI()
token = spotify.set_token()

url = 'https://api.spotify.com/v1/me/playlists'
spotify.set_url(url)
response = spotify.call_api()

playlist_id = spotify.get_users_playlist_id(response)

url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
spotify.set_url(url)
response = spotify.call_api()


id = spotify.get_playlist_songs(response)

url = f'https://api.spotify.com/v1/audio-features/{id}'
spotify.set_url(url)
response = spotify.call_api()

song_info = spotify.get_song_info(response, id)
print(song_info)


