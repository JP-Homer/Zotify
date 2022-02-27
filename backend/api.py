#api.py

from re import L
from pip._vendor import requests
import algorithm

def run():
    global spotify
    global create_playlist_token
    global add_items_token
    global song_information

    song_information = {}

    spotify = SpotifyAPI()

    #
    # TOKENS EXPIRE AND MUST BE RESET EVERY FEW HOURS
    #
    get_playlist_token = 'BQAIO6aRrEgBV7ZzMn9M4nfHICF-Xp15aIV9IGw8qj8NPH0Boc56quza1ZbE07deBS39VwXqwPu4cf5GDl1cL-0WmUhaUcDvUmV0ppCVgFbPb9dK3v66Ef1zcZ5enSHuYYdqTWRX1Z1G9iYwPtE46EaG6YW09cYrqe0eApsyZjIFwI7f5sULAKOU9bR-m7CQwNqpkfp43FLHmRNB7YZIORD1FTUH8Sq-PY9wBDfr4OBF7dZ_OOaC6810kxoj'
    spotify.set_token(get_playlist_token)
    create_playlist_token = 'BQAqortNtw0vCILC9Mqi7Ub-EnVOFzksZwcZvBSl9rRrpFZUvkIa-ZmTQINqkF7KOkNqXwGNAMUQ_jo0b2-djkXRzCtdy6KDvagx5E2hYI_T790BaSJ82gGDI9G-o13XMezr_snKx4FfLpnLjo1jyWmHrXbYBQCyzBC4v7hJ3cuBC96N5xmXwFRkmWO4y4VYW9TqAag-_x8ZxSPrWh6aQjb_aY4mo0cL6Re-wRQPdAVd7ZGaDMS1peFFRMmh'
    add_items_token = 'BQCt7E3_wg_NUqQ_NGM2A47AVNB8uxdlPYCJowLKYv4WvyBMkAJcRdcpI6xMW3qwDGG2MhOrNcrwAwWqDxF0y1j5qR9bbNRQH1or4PZ_o2JItBIFI8uSaw6C7kju6CklV8yA5fyuZbfwlKIQYs30yp4tS4BSU1dFGXMfaGM6n7Q6AREOKkuLLSGtdPJef8lGWzcaQX3I341GSM5l6WB1FdSbBVNzEZ9noJ0xTcvq8Yf6BnenN6gavzdNq8rO'
    song_ids = playlist()
    gather_song_data(song_ids)

class SpotifyAPI:
    url = ''
    token = ''

    # Sets url based on what API link is called
    def set_url(self, url):
        self.url = url

    # Sets the token depending on permissions required for a certain call
    def set_token(self, token):
        self.token = token

    # Calls the api itself and returns a json file with data
    def call_api(self):
        response = requests.get(self.url, headers={'Authorization': f'Bearer {self.token}'})
        response = response.json()

        return response

    # Handles creating a playlist
    def create_playlist(self, name, public):
        response = requests.post(self.url, 
        headers=
        {
            "Authorization": f"Bearer {self.token}"
            }, 
        json={
            "name": name, 
            "public": public
        })

        json_resp = response.json()
        return json_resp

    # Handles adding songs to the playlist created above
    def add(self, uris):
        response = requests.post(self.url, 
        headers=
        {
            "Authorization": f"Bearer {self.token}"
            }, 
        json={
            'uris': uris
        })

        json_resp = response.json()
        return json_resp

    # Grabs all songs from a specific playlist
    def get_playlist_songs(self, response):
        id = response['items'][0]['track']['id']
        return id

    # Gathers song information including the energy, the valence of it
    # (how happy/upbeat or sad/angry it sounds), as well as the tempo
    def get_song_info(self, response, id):
        print(response)
        energy = response['energy']
        valence = response['valence']
        tempo = response['tempo']
        
        song_information[id] = {'energy': '', 'valence': '', 'tempo': ''}

        song_information[id]['energy'] = energy
        song_information[id]['valence'] = valence
        song_information[id]['tempo'] = tempo

def playlist():
    # Accesses a specific public playlist and puts ids of songs into a list
    url = 'https://api.spotify.com/v1/playlists/5ABHKGoOzxkaa28ttQV9sE/tracks'
    spotify.set_url(url)
    response = spotify.call_api()

    songs = []

    for index in range(0, 100):
        songs.append(response['items'][index]['track']['id'])

    return songs

def new_playlist(name):
    # Logic for creating a new playlist
    user_id = 'misterepicness'
    url = f'https://api.spotify.com/v1/users/{user_id}/playlists'

    spotify.set_token(create_playlist_token)
    spotify.set_url(url)
    response = spotify.create_playlist(name, True)
    return(response['id'])

def gather_song_data(song_ids):
    # Logic for gathering data from the songs
    for id in song_ids:
        url = f'https://api.spotify.com/v1/audio-features/{id}'
        spotify.set_url(url)
        response = spotify.call_api()
        spotify.get_song_info(response, id)

def add_songs(playlist_id, uris):
    # Logic for adding songs
    url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    spotify.set_url(url)
    spotify.set_token(add_items_token)
    response = spotify.add(uris)
    return response

#These functions are for the buttons
def happy():
    # If user chooses the 'happy' mood, populate playlist above with only
    # happy sounding songs
    global song_information
    possible_playlists = algorithm.algorithm(song_information)
    choice = possible_playlists['happy']
    for index, uri in enumerate(choice):
        choice[index] = 'spotify:track:' + uri

    new_playlist_id = new_playlist('Happy')
    add_songs(new_playlist_id, choice)
    song_information = {}
    return new_playlist_id

def sad():
    # If user chooses the 'sad' mood, populate playlist above with only
    # sad sounding songs
    global song_information
    possible_playlists = algorithm.algorithm(song_information)
    choice = possible_playlists['sad']
    for index, uri in enumerate(choice):
        choice[index] = 'spotify:track:' + uri

    new_playlist_id = new_playlist('Sad')
    add_songs(new_playlist_id, choice)
    song_information = {}
    return new_playlist_id

def angsty():
    # If user chooses the 'angsty' mood, populate playlist above with only
    # angsty sounding songs
    global song_information
    possible_playlists = algorithm.algorithm(song_information)
    choice = possible_playlists['angsty']
    for index, uri in enumerate(choice):
        choice[index] = 'spotify:track:' + uri

    new_playlist_id = new_playlist('Angsty')
    add_songs(new_playlist_id, choice)
    song_information = {}
    return new_playlist_id

def chill():
    # If user chooses the 'chill' mood, populate playlist above with only
    # chill sounding songs
    global song_information
    possible_playlists = algorithm.algorithm(song_information)
    choice = possible_playlists['chill']
    for index, uri in enumerate(choice):
        choice[index] = 'spotify:track:' + uri

    new_playlist_id = new_playlist('Chill')
    add_songs(new_playlist_id, choice)
    song_information = {}
    return new_playlist_id
