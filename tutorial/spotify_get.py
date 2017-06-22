import pprint
import sys

import spotipy
import spotipy.util as util

import json


# token = util.prompt_for_user_token(client_id=settings.SPOTIFY_CLIENT_ID)
# spotify = spotipy.Spotify()
with open('spiders/songs.json') as json_data:
    parsed_json = json.load(json_data)
    for index in parsed_json:
        print(index['artist'])
        spotify = spotipy.Spotify()
        results = spotify.search(q='artist:' + index['artist'], type='artist')
        print (results)







