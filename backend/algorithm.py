#algorithm.py
def algorithm(song_info):
    song_moods = {'happy': [], 'sad': [], 'angsty': [], 'chill': []}
    for index, (key, value) in enumerate(song_info.items()):
        # START EDIT
        if value["energy"] >= .7 and value["valence"] >= .7:
            song_moods['happy'].append(key)
        if value["energy"] <= .4 and value["valence"] <= .5:
            song_moods['sad'].append(key)
        if value["valence"] <= .4 and value["energy"] >= .5:
            song_moods['angsty'].append(key)
        if value["energy"] <= .5 and value["valence"] <= .5:
            song_moods['chill'].append(key)
    return song_moods

