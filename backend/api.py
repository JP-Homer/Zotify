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
    get_playlist_token = 'BQA6OnT2vXlYa0I_Wfectz_TRFLelRa7Bkd8bh7UevskaEA0EOYlY_S59nlkJEicLLWCtFYcA-U8NAXT37RTChDr6qCs3LGmbYp8gnHVk-xQaMpkdh9zul4PDobVorIFcdw2j_56wrnjE0UkKw-5qVc-B7_R5JTGADYY4cHd9njZ98ayJoUggx95Q75LBmL18Nw3X8LtXDKUuq7u5bVawfZavQ3V3w2oP9SOqoR92PhpO0YN7AQ2_OHTU3JI'
    spotify.set_token(get_playlist_token)
    create_playlist_token = 'BQD-Pw5C1A7dH9wUq7VAn_tUesbLTrM984qd3rVOmFFvvS0Y2yKTLZBlTuCatSULfUpNWELL0w97kfX7A7vEh_SkheWVVhx27UYSxfrUOhSW-qpxhhzdIrgxSvMr2t5osWZNXjKCyqRSRV-RrzVPJiuCA9r95_RQ_9wELd1Hd_yaqkHKrqa_rGyR_QssrQ9NkcPS048BQgeX87EffELnxVwQejNlsz-hlhFd24F3TJ7EPTxR3_l1XQKz_vu0'
    add_items_token = 'BQApKoAHmtooFjzz2baTLzGHahkAcZweygvhTXoksqvsZZo2ssJCYcCD2AXtRGmdBB1MezU3NzjV0v845wg6O_yYgrrOpdPtLSRMB2YcyWeJNPBNZeT9-EOQbuxqafeb67cdGfc8kdi8uYHltMk8fNHyS_JTGgnLHuebUnjd_fHBm4amaXWAnJnrsPzTc2dgcmJdRFWv2KnChj4rX1mPLx9_nKg6g2vMyywXK3pNISm-yXBZmh_XKCLaGBgW'
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
