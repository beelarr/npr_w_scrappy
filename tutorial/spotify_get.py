import pprint
import sys

import spotipy
import spotipy.util as util

import json


with open('spiders/songs.json') as json_data:
        parsed_json = json.load(json_data)
        print(parsed_json)

token = util.prompt_for_user_token('SPOTIPY_CLIENT_ID', 'SPOTIPY_CLIENT_SECRET', 'SPOTIPY_REDIRECT_URI')
spotify = spotipy.Spotify(auth=token)

if token:
    for index in parsed_json:
        print(index['artist'])
        r = spotify.search(q='track:' + index['song'] + ' ' + 'artist:' + index['artist'], limit=1, type='track')
        print (r)

# Example return of this search
# {
#   "artists" : {
#     "href" : "https://api.spotify.com/v1/search?query=%27Aurora+Nigel+Stanford%27&type=artist&market=US&offset=0&limit=2",
#     "items" : [ ],
#     "limit" : 2,
#     "next" : null,
#     "offset" : 0,
#     "previous" : null,
#     "total" : 0
#   },
#   "tracks" : {
#     "href" : "https://api.spotify.com/v1/search?query=%27Aurora+Nigel+Stanford%27&type=track&market=US&offset=0&limit=2",
#     "items" : [ {
#       "album" : {
#         "album_type" : "album",
#         "artists" : [ {
#           "external_urls" : {
#             "spotify" : "https://open.spotify.com/artist/4Jyb0l1PTSn1VxNmiFxSf4"
#           },
#           "href" : "https://api.spotify.com/v1/artists/4Jyb0l1PTSn1VxNmiFxSf4",
#           "id" : "4Jyb0l1PTSn1VxNmiFxSf4",
#           "name" : "Nigel Stanford",
#           "type" : "artist",
#           "uri" : "spotify:artist:4Jyb0l1PTSn1VxNmiFxSf4"
#         } ],
#         "available_markets" : [ "AD", "AR", "AT", "AU", "BE", "BG", "BO", "BR", "CA", "CH", "CL", "CO", "CR", "CY", "CZ", "DE", "DK", "DO", "EC", "EE", "ES", "FI", "FR", "GB", "GR", "GT", "HK", "HN", "HU", "ID", "IE", "IS", "IT", "JP", "LI", "LT", "LU", "LV", "MC", "MT", "MX", "MY", "NI", "NL", "NO", "NZ", "PA", "PE", "PH", "PL", "PT", "PY", "SE", "SG", "SK", "SV", "TR", "TW", "US", "UY" ],
#         "external_urls" : {
#           "spotify" : "https://open.spotify.com/album/244wbAAm5TyMZiInLGbYUb"
#         },
#         "href" : "https://api.spotify.com/v1/albums/244wbAAm5TyMZiInLGbYUb",
#         "id" : "244wbAAm5TyMZiInLGbYUb",
#         "images" : [ {
#           "height" : 640,
#           "url" : "https://i.scdn.co/image/37c03c453533668f59b2fe741df5e8a3c05b17ed",
#           "width" : 640
#         }, {
#           "height" : 300,
#           "url" : "https://i.scdn.co/image/179090d5fcb5cc19c0e4b92601fb2e4ea724251f",
#           "width" : 300
#         }, {
#           "height" : 64,
#           "url" : "https://i.scdn.co/image/c55f6165819d7c6797ccacddae87de8a65dc700d",
#           "width" : 64
#         } ],
#         "name" : "Solar Echoes",
#         "type" : "album",
#         "uri" : "spotify:album:244wbAAm5TyMZiInLGbYUb"
#       },
#       "artists" : [ {
#         "external_urls" : {
#           "spotify" : "https://open.spotify.com/artist/4Jyb0l1PTSn1VxNmiFxSf4"
#         },
#         "href" : "https://api.spotify.com/v1/artists/4Jyb0l1PTSn1VxNmiFxSf4",
#         "id" : "4Jyb0l1PTSn1VxNmiFxSf4",
#         "name" : "Nigel Stanford",
#         "type" : "artist",
#         "uri" : "spotify:artist:4Jyb0l1PTSn1VxNmiFxSf4"
#       } ],
#       "available_markets" : [ "AD", "AR", "AT", "AU", "BE", "BG", "BO", "BR", "CA", "CH", "CL", "CO", "CR", "CY", "CZ", "DE", "DK", "DO", "EC", "EE", "ES", "FI", "FR", "GB", "GR", "GT", "HK", "HN", "HU", "ID", "IE", "IS", "IT", "JP", "LI", "LT", "LU", "LV", "MC", "MT", "MX", "MY", "NI", "NL", "NO", "NZ", "PA", "PE", "PH", "PL", "PT", "PY", "SE", "SG", "SK", "SV", "TR", "TW", "US", "UY" ],
#       "disc_number" : 1,
#       "duration_ms" : 599146,
#       "explicit" : false,
#       "external_ids" : {
#         "isrc" : "TCACB1462196"
#       },
#       "external_urls" : {
#         "spotify" : "https://open.spotify.com/track/4xwuyl6rPGtPbjGTKB2sso"
#       },
#       "href" : "https://api.spotify.com/v1/tracks/4xwuyl6rPGtPbjGTKB2sso",
#       "id" : "4xwuyl6rPGtPbjGTKB2sso",
#       "name" : "Aurora",
#       "popularity" : 24,
#       "preview_url" : "https://p.scdn.co/mp3-preview/f7ac7a50e6932c8107b6c6080d4680e4115cbbc8?cid=8897482848704f2a8f8d7c79726a70d4",
#       "track_number" : 7,
#       "type" : "track",
#       "uri" : "spotify:track:4xwuyl6rPGtPbjGTKB2sso"
#     } ],
#     "limit" : 2,
#     "next" : null,
#     "offset" : 0,
#     "previous" : null,
#     "total" : 1
#   }
# }




