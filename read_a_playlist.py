from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
import sys

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# 2 inputs means that you are passed the username and playlist uri
# 1 input means that you are passed a direct url to the playlist
# Sample input python read_a_playlist.py https://open.spotify.com/user/12186663114/playlist/2XcRigegs6l625qChqARQd

if len(sys.argv) > 2:
  username = sys.argv[1]
  playlist_id = sys.argv[2]
elif len(sys.argv) > 1:
  url = sys.argv[1]
  username = url.split('/')[4]  
  playlist_id = url.split('/')[6] 
else:
  print ("Usage: %s userid playlist_id ... || %s url" % (sys.argv[0],))
  sys.exit()


results = sp.user_playlist(username, playlist_id)

i = 0
while (i < len(results['tracks']['items'])):
  print results['tracks']['items'][i]['track']['name']
  i += 1
