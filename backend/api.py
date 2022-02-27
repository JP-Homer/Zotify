#api.py

from re import L
from pip._vendor import requests
import algorithm

#Protocol order: sign in, assign moods to types of music, create playlist, pull songs from their playlists, add to new playlist, return playlist

def run():
    global spotify
    global create_playlist_token
    global add_items_token
    global song_information

    song_information = {}

    spotify = SpotifyAPI()
    get_playlist_token = 'BQBN40lnyx_r1koTdgUoMNzdXtYTxjiVTFqYnBWecnJYisxoOUkeAZc5xPc_lL7dxWgiuFPfv1-fALfgLy0q53Y0A9d2oMRMdTVgo5TDxKlqXWoDier9VzCkJ6ke_r8m2kojUxF7Nf5mdVPNRszXQyEsUxLVwOJXcMueDyvk-2BEl6aXhmLOoTKmOAsbuDK5hT7Q1ynDIETH9KqAdwNBDvLHb7uYOMHPqGjJDRtL7Kl3ECi1xycQ3sH5TP4j'
    spotify.set_token(get_playlist_token)
    create_playlist_token = 'BQATxuFDj7TP_PBE8LMmtBLuNiZMLMEL_V2W_v9sfKfTRVdSmwxnmzoyeAWKooPYfDNoXF5b6hwm5UGqwb1KvdseFCk70mjLdkSMBTpXIpPHltIO9_DpkHQ9ITrAq9jkm8mAUJMnA-cJUjt0JrjditvAVdCql3f5KjdwYn5RaynQnkRedax4DyZvB90XWZllzLlctmP5JFrGy9nb6JgqzarD-mjq0OzvBCX1mOiJXK8MrCMle9_pqrce-oES'
    add_items_token = 'BQC9c8JRi84-5Ph1mxuV4U0UJP_SWHcokV0JzC-oyk8k1YLOLDBl-NExZ6Now6UssbyXFPxZy2MsxszoAVddzFQay1gMsWUZZpZdd7RdC23-XIZ_N4aErkueKnDit6-7zIeY7MURXVyO8LKKLE4kLtGRuQeWdjgEapwo80w6GC6X_8trWoSwc2S_m6aB6tIHSWR13i8z9ftV2cDC10BCI8tN_vRiu9PFJCve6EK5tbK7sFDukhFG-p2Oa_eM'
    song_ids = playlist()
    gather_song_data(song_ids)

class SpotifyAPI:
    url = ''
    token = ''

    def set_url(self, url):
        self.url = url

    def set_token(self, token):
        self.token = token

    def call_api(self):
        response = requests.get(self.url, headers={'Authorization': f'Bearer {self.token}'})
        response = response.json()

        return response

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

    # def get_users_playlist_id(self, response):
    #     playlist_id = response['items'][0]['uri']
    #     playlist_id = playlist_id[playlist_id.find('spotify:playlist:') + 17:]
    #     self.playlist_id = playlist_id
    #     return playlist_id

    def get_playlist_songs(self, response):
        id = response['items'][0]['track']['id']
        return id

    def get_song_info(self, response, id):
        print('WHORE')
        print(response)
        energy = response['energy']
        valence = response['valence']
        tempo = response['tempo']
        
        song_information[id] = {'energy': '', 'valence': '', 'tempo': ''}

        song_information[id]['energy'] = energy
        song_information[id]['valence'] = valence
        song_information[id]['tempo'] = tempo

def playlist():
    # CHRISTIAN spotify:playlist:1BqjQjBheHGLEG5pDcrhVv
    # JIMMY spotify:playlist:7g4MAij8qTKger93yqnuqx
    # Big songs spotify:playlist:37i9dQZF1DX5Vy6DFOcx00
    # Top 50 USA spotify:playlist:37i9dQZEVXbLRQDuF5jeBp
    # Top 100 most streamed spotify:playlist:5ABHKGoOzxkaa28ttQV9sE
    url = 'https://api.spotify.com/v1/playlists/5ABHKGoOzxkaa28ttQV9sE/tracks'
    spotify.set_url(url)
    response = spotify.call_api()

    songs = []

    for index in range(0, 100):
        songs.append(response['items'][index]['track']['id'])

    return songs

def new_playlist(name):
    user_id = 'misterepicness'
    url = f'https://api.spotify.com/v1/users/{user_id}/playlists'

    spotify.set_token(create_playlist_token)
    spotify.set_url(url)
    response = spotify.create_playlist(name, True)
    return(response['id'])

def gather_song_data(song_ids):
    for id in song_ids:
        url = f'https://api.spotify.com/v1/audio-features/{id}'
        spotify.set_url(url)
        response = spotify.call_api()
        spotify.get_song_info(response, id)

def add_songs(playlist_id, uris):
    url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    spotify.set_url(url)
    spotify.set_token(add_items_token)
    response = spotify.add(uris)
    return response

#These functions are for the buttons
def happy():
    global song_information
    possible_playlists = algorithm.algorithm(song_information)
    choice = possible_playlists['happy']
    for index, uri in enumerate(choice):
        choice[index] = 'spotify:track:' + uri

    new_playlist_id = new_playlist('Happy')
    add_songs(new_playlist_id, choice)
    song_information = {}


def sad():
    global song_information
    possible_playlists = algorithm.algorithm(song_information)
    choice = possible_playlists['sad']
    for index, uri in enumerate(choice):
        choice[index] = 'spotify:track:' + uri

    new_playlist_id = new_playlist('Sad')
    add_songs(new_playlist_id, choice)
    song_information = {}

def angsty():
    global song_information
    possible_playlists = algorithm.algorithm(song_information)
    choice = possible_playlists['angsty']
    for index, uri in enumerate(choice):
        choice[index] = 'spotify:track:' + uri

    new_playlist_id = new_playlist('Angsty')
    add_songs(new_playlist_id, choice)
    song_information = {}

def chill():
    global song_information
    possible_playlists = algorithm.algorithm(song_information)
    choice = possible_playlists['chill']
    for index, uri in enumerate(choice):
        choice[index] = 'spotify:track:' + uri

    new_playlist_id = new_playlist('Chill')
    add_songs(new_playlist_id, choice)
    song_information = {}



#Testing code

# url = 'https://api.spotify.com/v1/me/playlists'
# spotify.set_url(url)
# response = spotify.call_api()

# playlist_id = spotify.get_users_playlist_id(response)

# url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
# spotify.set_url(url)
# response = spotify.call_api()


# id = spotify.get_playlist_songs(response)

# url = f'https://api.spotify.com/v1/audio-features/{id}'
# spotify.set_url(url)
# response = spotify.call_api()

# song_info = spotify.get_song_info(response, id)