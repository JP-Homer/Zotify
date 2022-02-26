import requests

playlist_url = 'https://api.spotify.com/v1/users/12134804575/playlists'
token = 'BQDEcdVThdhdm0V_hR5uaizAOu7TlFph2I6My838nAqixjwbnCnvG3wJqa8629-YXXVpl_Qcmmvqj0zEnCxKdUu2DZ3j_2BMt_frrbZmiptBh0cfMLr26mKJe90dCTCO6pLGattd5E0bjbhrrwjNbIjEwBeCKYfxhOkNudyX3b39xbvt-Sugh38A_gdfLijIRRX1MVQ4ObX9EYY'

pause_url = 'https://api.spotify.com/v1/me/player/pause?device_id=0d1841b0976bae2a3a310dd74c0f3df354899bc8'

player_url = 'https://api.spotify.com/v1/me/player'

juice_uri = '4MCBfE4596Uoi2O4DtmEMz'

'''
def create_playlist(name, public):
    response = requests.post(playlist_url, 
    headers=
    {
        "Authorization": f"Bearer {playlist_token}"
        }, 
    json={
        "name": name, 
        "public": public
    })

    json_resp = response.json()

    return json_resp

'''

def playback_state():
    response = requests.get(player_url, headers={'Authorization': f'Bearer {token}'})

    resp = response.json()

    return resp


def main():
    name = "New Playlist"
    public = False

    '''
    playlist = create_playlist(name, public)

    print(playlist)
    '''

    state = playback_state()

    album = state['item']['album']['name']
    song = state['item']['name']

    print(f"\n\nUser is currently playing the song {song} from the album {album}\n")


if __name__ == "__main__":
    main()
