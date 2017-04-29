#takes in a playlist url as input
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import spotipy
import spotipy.util as util
import json
from urlparse import urlparse

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_image(userid):
	user = sp.user(userid)
	return (user['images'][0]['url'])

def get_name(playlist_id, user_id):
	playlist = sp.user_playlist(user_id, playlist_id)
	return playlist['name']

def getDetails(url=None):
	scope = 'playlist-modify-public'

	if url is not None:
	    URL = url
	else:
	    print("Usage: playlist url ")
	    sys.exit()

	temp = urlparse(URL)
	temp = temp.path
	temp = temp.split('/')

	#userid and playlistid stored as strings
	userid = temp[2]
	playlistid = temp[4]

	#get user image
	user_image = get_image(userid)

	#get name of playlist
	list_name = get_name(playlistid, userid)
	#return (user_image, namePlaylist)	
	return (user_image, list_name)

getDetails(sys.argv[1])
