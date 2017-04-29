# shows a user's playlists (need to be authenticated via oauth)

import pprint
import sys
import os
import subprocess

import spotipy

import spotipy.util as util
import glob

results = {}

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Whoops, need your username!")
    print("usage: python user_playlists.py [username]")
    sys.exit()

token = util.prompt_for_user_token(username)

if token:
    sp = spotipy.Spotify(auth=token)
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        results[playlist['name']] = playlist['id']
else:
	print("Can't get token for", username)

print results.keys()
os.remove(".cache-" + username)
