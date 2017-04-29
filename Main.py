import sys
import spotipy
import spotipy.util as util
import json
import re
import os
from spotipy.oauth2 import SpotifyClientCredentials


from read_a_playlist import getTracks
from merge import merge
from user_playlists import getPlaylists

scope = 'playlist-modify-public'
clientID = "ec548750929f4ba7925acbe76d9b0abe"
secret = "b9ca5d242fd240d6900a49443e2b379d"
returnuri = "http://localhost:8888/callback"


#Initial Call Main.py Userid 
#Receives a userid, will return a hash of h{songName} = songId
def findPlayLists(username = None):
    if username is not None:
        #note username is actually the userid
        playlist_options = getPlaylists(username)
        #print playlist_options
        return playlist_options
    else:
        print("Usage: %s username ..." % (sys.argv[0],))
        sys.exit()
        return

def makePlaylist(username, playlist_options, playlist_name, playlist_url):
    #Display options -> Front end
    keys = playlist_options.keys()
    r = re.compile(".*"+playlist_name+".*")
    playlist_id = filter(r.match, keys)
    #incorrect key
    playlist_id = playlist_options[playlist_id[0]]
    #print(playlist_id)  #this is incorrect
    #Track 1 = Playlist id -> need to use id to get list of tracks
    #saying that it doesn't exist
    track1 = getTracks(name=username, playlist_input="1mLcnbKN3MnvTEkwTpDKz5")
    #print(track1)
    #Track 2 = url -> need to use url to get list of tracks

    # also wrong
    track2 = getTracks(name= "12186663114",  playlist_input="76wWOIbVfP1O6U0nUmCKXO") #playlist_url
    #print(track2)

    #merge playlists
    # get a list of songs that will be added into the new playlist
    track_ids = merge(track1, track2)
    #print(track_ids)

    token = util.prompt_for_user_token(username, scope, clientID, secret, returnuri)

    # os.remove(".cache-" + username)s
    if token:

        sp = spotipy.Spotify(auth=token)
        sp.trace = False

        # # #create a new playlist for yourself
        playlists = sp.user_playlist_create(username, playlist_name, public=True)
        # get playlist id
        plid = playlists['id']
        #print(plid)

        # # Add songs
        results = sp.user_playlist_add_tracks(username, plid, track_ids)
        #print(playlists['external_urls']['spotify'])
        return(playlists['external_urls']['spotify'])

    else:
        print("Can't get token for", username)

makePlaylist(username='1251616626', playlist_options=findPlayLists(username='1251616626'),playlist_name='test',playlist_url='https://open.spotify.com/user/12186663114/playlist/5iBkCrMuq3XB6ti9ZfjhuX')
