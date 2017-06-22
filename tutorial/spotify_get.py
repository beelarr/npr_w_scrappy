import pprint
import sys

import spotipy
import spotipy.util as util

import json


with open('spiders/songs.json') as json_data:
        parsed_json = json.load(json_data)


token = util.prompt_for_user_token(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)
spotify = spotipy.Spotify(auth=token)

if token:
    for index in parsed_json:
        print(index['artist'])
        results = spotify.search(q='artist:' + index['artist'], type='artist')
        print (results)






