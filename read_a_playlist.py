from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
import sys

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# 2 inputs means that you are passed the username and playlist uri
# 1 input means that you are passed a direct url to the playlist
# Sample input python read_a_playlist.py https://open.spotify.com/user/12186663114/playlist/2XcRigegs6l625qChqARQd
def getTracks(name = None, playlist_input = None):
  if playlist_input is not None:
    username = name
    playlist_id = playlist_input
  elif playlist_input is None:
    url = name
    username = url.split('/')[4]  
    playlist_id = url.split('/')[6] 
  else:
    print ("Usage: %s userid playlist_id ... || %s url" % (sys.argv[0],))
    sys.exit()

  results = sp.user_playlist(username, playlist_id)

  i = 0
  #Compile list of tracks
  tracks = []
  while (i < len(results['tracks']['items'])):
    tracks.append(results['tracks']['items'][i]['track']['id'])
    i += 1

  return tracks

# getTracks(name='1251616626', playlist_input='05glWp9urqIVvIGmD2vbCk')
