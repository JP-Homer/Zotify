#api.py

from re import L
from pip._vendor import requests
import algorithm

#Protocol order: sign in, assign moods to types of music, create playlist, pull songs from their playlists, add to new playlist, return playlist

song_information = {}

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
        energy = response['energy']
        valence = response['valence']
        tempo = response['tempo']
        
        song_information[id] = {'energy': '', 'valence': '', 'tempo': ''}

        song_information[id]['energy'] = energy
        song_information[id]['valence'] = valence
        song_information[id]['tempo'] = tempo

spotify = SpotifyAPI()
get_playlist_token = 'BQDxaPVgCv3jryCRGp7ETFGhezX6lxwk9jS8Xai50x9W_6TNqGyVoW4bP1AOu7cvGzOmcYHOKg_aQylajwJpjBtpUUya3UZQ2FBjxkQ5AVW9xucZpVl2DgWptVeP7AkLu5dJRE2-XcFyBHwVc1Tc-ReWdkZ_EbmjfghKzkflMKa3asydsExTyQZeO55f0xip8IEwbYWtAdP_sf9ObKpYFMQVicdRChAblBmV8LkJlg-g-jdWVswTdWXshmG9'
spotify.set_token(get_playlist_token)
create_playlist_token = 'BQD0Gl7nne54XvBESawrbiTTB-F6AWH9Q_m-wYEkhsOyJvFd8cPdjoywUlnqOC6zHg31aBZPjZSJaj1ZiPvvkk3BGvR3N16fwGBrRHZKzGnUq0XWinfLHK2FP3RO-NqhwAC3tLgG8J7rnIBkiLmp6aQbfoOcCjVbE2jf2vLRf1517JiUtK--rQHfWIHc6dWNJuFMqU4G50YvxSCbnA'
add_items_token = 'BQBFQZJc5Rxg7vclOa3yv4Gc5ADKmiRtUbxa7Hwn4C0LqO-6OP6rdhCMouXIEIF1lZNA66dhmsGMTwKrPt0wM3EiFNGBRpo961mfp_oIKFIERNtievfyqTywBy-sW-oxLqNNNdnEP6eJJxml2eNrelDRbAEXOTqB3NjnC-4QTiat5yfvvsLYdrNYHNY8JAzDGNz7dJq2Jo0_DL-0zNdPTcg4cAhB0okQ0Z07QjbKAm9xbmCfQbt6z3ZohlpO'


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

def new_playlist():
    user_id = 'misterepicness'
    url = f'https://api.spotify.com/v1/users/{user_id}/playlists'

    spotify.set_token(create_playlist_token)
    spotify.set_url(url)
    response = spotify.create_playlist('testing', True)
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



song_ids = playlist()
gather_song_data(song_ids)
possible_playlists = algorithm.algorithm(song_information)
happy = possible_playlists['chill']
for index, uri in enumerate(happy):
    happy[index] = 'spotify:track:' + uri



new_playlist_id = new_playlist()
add_songs(new_playlist_id, happy)



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