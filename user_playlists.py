# shows a user's playlists (need to be authenticated via oauth)

import pprint
import sys
import os
import subprocess
from spotipy.oauth2 import SpotifyClientCredentials

import spotipy

import spotipy.util as util

results = {}

def getPlaylists(username=None):
	if username is None:
	    print("Whoops, need your username!")
	    print("usage: python user_playlists.py [username]")
	    sys.exit()

	# token = util.prompt_for_user_token(username)
	client_credentials_manager = SpotifyClientCredentials()
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

	playlists = sp.user_playlists(username)
	for playlist in playlists['items']:
		#print(playlist['name'], playlist['id'])
		results[playlist['name']] = playlist['id']

	#print results.keys()
	# os.remove(".cache-" + username)
	print results.keys()
	return results

	# if token:
	#     sp = spotipy.Spotify(auth=token)
	#     playlists = sp.user_playlists(username)
	#     for playlist in playlists['items']:
	#     	#print(playlist['name'], playlist['id'])
	#         results[playlist['name']] = playlist['id']
	# else:
	# 	print("Can't get token for", username)
    #
	# #print results.keys()
	# os.remove(".cache-" + username)
	# print results.keys()
	# return results

getPlaylists(username='12186663114')
